---
name: chainsquad-ledger
description: >
  Produces plain-text hledger/ledger-compatible journal entries for ChainSquad GmbH
  from uploaded PDF invoices. Use this skill whenever the user uploads invoices,
  receipts, insurance letters, or payment confirmations and asks to "add to the ledger",
  "book these", "create journal entries", or similar. Also triggers when the user uploads
  files whose filenames begin with a 4-digit number (the internal invoice number).
---

# ChainSquad Ledger Skill

Converts uploaded invoice PDFs into plain-text accounting entries compatible with
hledger / ledger-cli, following the conventions already established in the existing
ChainSquad GmbH ledger.

---

## Workflow

1. **Extract text from PDFs** using `markitdown` CLI:

   ```bash
   markitdown /path/to/invoice.pdf
   ```

   This produces Markdown output containing all invoice text in a parseable format.

2. **Parse invoice data** from the extracted Markdown:
   - Invoice number (from filename prefix: `1103-Hetzner_...pdf`)
   - Vendor name (from invoice header)
   - Invoice date (invoice date, not scan date)
   - Total amount and currency (EUR/USD)
   - VAT status (19% standard, reverse charge, or 0%)
   - Line items / service category

3. **Format journal entry** following output format below.

4. **Output** to `.journal` file with header block.

---

## Batch processing

When asked to process multiple invoices starting from invoice number X (e.g., 1171):

```bash
cd bills/2025/ && ls *.pdf | sort -n | awk -F '-' '$1 > 1171 {print}'
```

This lists all PDFs in `bills/2025/` where the invoice number prefix exceeds 1171, sorted numerically.

Apply markitdown to each file in the list, then parse and generate journal entries for the batch.

---

## markitdown extraction patterns

The `markitdown` tool reliably converts invoice PDFs to structured Markdown. Parse key fields using these patterns:

| Field          | Search pattern                                                                | Example                  |
| -------------- | ----------------------------------------------------------------------------- | ------------------------ |
| Vendor name    | Company name at top, or `Vendor:`, `Rechnungssteller`, `From`                 | `Hetzner Online GmbH`    |
| Invoice date   | `Rechnungsdatum`, `Invoice date:`, `Date:`, pattern `DD.MM.YYYY`              | `15.01.2026`             |
| Invoice number | `Rechnungsnr:`, `Invoice #`, `Rechnung Nr.`                                   | `1103`                   |
| Total          | `Gesamtbetrag`, `Total:`, `Betrag:`, `EUR`/`USD`                              | `€ 123,45` or `$ 456.78` |
| VAT rate       | `19% MwSt`, `USt 19%`, `VAT 19%`, `Netto`/`Brutto` ratio                      | `19%`                    |
| Reverse charge | `Reverse Charge`, `Steuerschuldnerschaft des Leistungsempfängers`, `EU-Intra` | Text found               |

**Handling date formats:**

- `DD.MM.YYYY` → convert to `YYYY-MM-DD`
- `DD/MM/YYYY` → convert to `YYYY-MM-DD`
- `YYYY-MM-DD` → keep as-is

**Handling number formats:**

- German format: `1.234,56 €` → `1234.56 €`
- English format: `1,234.56 $` → `1234.56 $`
- Remove thousands separators, use `.` as decimal

**Detection rules:**

- **Reverse charge**: Vendor names: `OpenAI`, `Anthropic`, `Stripe`, `Pulumi` OR keywords in text
- **0% VAT**: Keywords: `kein Vorsteuerabzug`, `0% MwSt`, `§29 StVZO`, `Dienstleistungssitz`
- **Split items**: Look for itemized tables with different categories → split into multiple accounts
- **Scanned PDF**: If markitdown output lacks structured invoice data (no date, vendor, amounts detected) → PDF is likely a scanned image, not text-selectable

**Handling extraction failures:**

If markitdown does not produce invoice-style content (detected as scanned PDF):

1. Add a `; NOTE` comment in the output with the invoice filename:

   ```
   ; NOTE: 1171-Vendor.pdf → scanned PDF, manual data extraction required
   ```

2. Skip automatic entry generation for that invoice

3. Inform user: "Invoice 1171-Vendor.pdf appears to be a scanned image. Please manually extract the data from the invoice and provide the details."

---

## Input

- One or more PDF files. The filename prefix is the internal invoice number:
  `1103-Hetzner_...pdf` → `#1103`.
- Optionally, the existing ledger file (provided as a document in context) for
  cross-referencing accounts, creditor codes, and prior entries.

---

## Output format

One journal entry per invoice, in this exact style:

```
YYYY-MM-DD [*] Vendor Name Invoice-Number (#NNNN)
    [; optional comment]
    Account        Amount €/$ [; inline note]
    Account        Amount €/$
    Kreditor:NNNNN-VendorSlug
```

- Use `*` (cleared) for all entries.
- Date = invoice date (not scan date, not payment date).
- Amounts: use `.` as decimal separator. No thousands separator.
- EUR amounts: append `€`. USD amounts: append `$`.
- Always split net amount, `Vorsteuer19`, and creditor on separate lines.
- For reverse-charge invoices (Stripe, OpenAI, Pulumi, Anthropic, etc.):
  omit `Vorsteuer19`; add `; Reverse Charge` comment.
- For pass-through fees with 0% MwSt (e.g. HU-Gebühr §29 StVZO):
  book on a separate line with `; kein Vorsteuerabzug (0% MwSt)`.

---

## Account names

Use these account names consistently:

| Type                         | Account                   |
| ---------------------------- | ------------------------- |
| Server / cloud hosting       | `Serverkosten`            |
| Internet connection          | `Internetanschluss`       |
| Mobile phone                 | `Handy`                   |
| Fuel                         | `Tanken`                  |
| Office rent / co-working     | `Miete`                   |
| Tax advisor                  | `Steuerberater`           |
| Online services (SaaS, APIs) | `OnlineDienst`            |
| Advertising / domains        | `Werbekosten`             |
| Car operating costs          | `KFZBetriebskosten`       |
| Car insurance                | `KFZVersicherung`         |
| Liability insurance          | `Haftpflichtversicherung` |
| Legal / translation          | `RechtsBeratungskosten`   |
| Travel (flights, rail)       | `Reisekosten`             |
| Entertainment / meals        | `Bewirtungskosten`        |
| Association membership       | `Vereinsbeitrag`          |
| Office supplies              | `Bürobedarf`              |
| Computer equipment           | `Computerausstattung`     |
| Shipping costs               | `Versandkosten`           |
| Coffee / consumables         | `Kaffee`                  |
| Fees / penalties             | `Gebühr`                  |
| Input VAT 19%                | `Vorsteuer19`             |

More accounts will be provided in context

---

## Creditor codes

Known creditors (use exact slug):

| Vendor                 | Kreditor                            |
| ---------------------- | ----------------------------------- |
| Hetzner Online GmbH    | `Kreditor:70005-Hetzner`            |
| noris network AG       | `Kreditor:70003-NorisNetworks`      |
| Drillisch / simplytel  | `Kreditor:70006-Simplytel`          |
| Günzel & Günzel GmbH   | `Kreditor:70004-Günzel`             |
| Feser-Biemann          | `Kreditor:70050-FeserBiemann`       |
| SUPOL-Tank             | `Kreditor:70040-Supol`              |
| OpenAI, LLC            | `Kreditor:70085-OpenAI`             |
| Anthropic              | `Kreditor:70089-Anthropic`          |
| Stripe Payments Europe | `Kreditor:70087-Stripe`             |
| Pulumi Corporation     | `Kreditor:70093-Pulumi`             |
| Namecheap              | `Kreditor:70007-Namecheap`          |
| Blockchain Bayern e.V. | `Kreditor:70065-BlockchainBayernEV` |
| Fort Advocaten N.V.    | `Kreditor:70070-FortAdvocaten`      |
| IHK                    | `Kreditor:70008-IHK`                |
| Bundesanzeiger         | `Kreditor:70027-Bundesanzeiger`     |
| Amazon                 | `Kreditor:70012-Amazon`             |
| Alternate GmbH         | `Kreditor:70011-Alternate`          |
| reichelt elektronik    | `Kreditor:70011-Reichelt`           |
| tintenalarm.de         | `Kreditor:70013-Tintenalarm`        |
| Twitter / X            | `Kreditor:70088-Twitter`            |
| KLM                    | `Kreditor:70090-KLM`                |
| IGZ GmbH (rent)        | `IGZ` (no Kreditor: prefix)         |
| Private reimbursements | `FabianPrivatKonto`                 |

More accounts will be provided in context
For new vendors, invent the next available creditor number and slug.

---

## Special cases & flags

### Duplicates

If two uploaded files have different invoice numbers but identical invoice number,
vendor, date, and amount → skip the duplicate; add a comment:

```
; #NNNN → duplicate of #MMMM (Vendor invoice-number) – no entry
```

### Non-invoice documents

Insurance letters, VBG notices, HUK payouts, etc. are not vendor invoices.

- If they represent an **outgoing payment** already covered elsewhere, book as memo only.
- If they represent an **incoming payment** (e.g. Kaskoersatz), book as a negative
  expense / income offset against the related cost account.

### USD invoices

Book in USD (append `$`). Do not convert to EUR unless the actual EUR debit amount
is known (e.g. from a PayPal receipt). If EUR amount is known, book that instead and
note the exchange rate in a comment.

### IGZ invoices

IGZ bills have changed format over time. Always use net amount + Vorsteuer19.
The `Miete` account covers all IGZ line items (phone, electricity, post, etc.)
unless the invoice itemizes them at a level where splitting adds clarity.

### Hetzner invoices

Split is always: `Serverkosten` (net total) + `Vorsteuer19`. If a domain renewal
is included, it is still folded into `Serverkosten` unless user asks otherwise.

### Günzel monthly advance (Vorschussrechnung)

Each monthly installment of Fibu advance is a separate entry with month
in a comment. Account: `Steuerberater`.

---

## Output file

Write all entries for the batch to a single `.journal` file named:
`ledger_NNNN-MMMM.journal` (first and last invoice number in the batch).

Place the file in `/mnt/user-data/outputs/` and present it using `present_files`.

Prepend the file with a header block:

```
; ============================================================
; Ledger entries #NNNN – #MMMM
; Generated from uploaded invoices using markitdown
; ============================================================
```

List any numbering conflicts, duplicates, non-invoice documents, or data
discrepancies in `; NOTE` comments immediately after the header, before the
first transaction.
