# Blockchain microinsurance & mutual risk pools — condensed research (Aug 2026)

Session context: Fabian evaluating whether blockchain can make microinsurance/mutual
pools more viable; tie-in considered with Tributary (Solana recurring payments) for
micro-premium collection. Provenance flags: [V] = verified live that day, [K] = knowledge-base
(subagent synthesis, early-2025 cutoff), [E] = peer-reviewed source cited.

## Market shape [K]
- SSA microinsurance: ~122.6M people covered, ~$2.1bn premium (MiN Africa Landscape 2023,
  pub. Feb 2025). Funeral cover = dominant line. Global inclusive coverage ~400-500M est.
- Natcat protection gap: 2023 $250bn losses / $95bn insured; 2024 $320bn / $140bn
  (Munich Re, Swiss Re sigma 1/2025).
- Premiums: $1-5/month (funeral/life), $5-40/yr micro-health, $3-25/season agri index.
- Unit economics = the killer: expense ratios 40-70% micro vs ~20% mainstream; one claims
  adjudication costs $2-15 (often > the claim); agri per-farm assessment $10-50.
  Break-even needs ~100k+ policies/line. MNO/mobile distribution cuts per-policy cost
  from $5-10 to <$1.

## What blockchain actually fixes (evidence-ranked)
1. Claims adjudication cost — parametric trigger + oracle auto-payout = cents marginal
   cost. This is why index insurance exists; chain makes settlement trustless/instant.
2. Payout speed/observability = demand. Cole et al. AEJ 2013: near-zero take-up without
   trust; past payout experience lifts demand ~40-50% (Cai). PMFBY pays in 6-12 months →
   farmers quit. Funeral insurance wins on fast observable payouts.
3. Verifiable solvency — on-chain overcollateralized reserve = audit-free proof money
   exists (trust primitive in low-trust markets).
4. Stablecoin payout rails — instant, USD hedge; MoneyGram-Stellar ~380k CICO points,
   Kotani Pay (USDC↔M-Pesa), Onafriq. Frictions: CICO spread, depeg risk (USDC $0.87,
   Mar 2023), gray-zone retail crypto rules in EMs.
5. Micro-premium collection — MNO commissions 15-30%; recurring-payment rails (Tributary's
   thesis) could collapse the other half of the expense ratio. Nobody has shipped a
   serious crypto-native recurring-micro-premium insurance product.

## Project post-mortems
- **Arbol** [V]: alive, $2B+ notional transferred, #1 global non-CAT parametric writer,
  15+ countries. Quietly de-blockchained — chain persisted only in settlement rails.
- **Nexus Mutual** [V]: alive, $7B+ crypto protected since 2019 — but still DeFi-internal
  cover only; never escaped "insuring DeFi against DeFi". Sole surviving mutual at scale.
- **Etherisc** [V]: alive, pivoted to B2B parametric rails for licensed insurers (D1Conf
  2024 Bangkok). Flight-delay dApp + Kenya maize pilots with ACRE Africa (payouts in days).
- **Sherlock**: survives by bundling cover with its audit marketplace (skin in the game).
- **Dead/wound down**: Risk Harbor (paid out cleanly on Terra 2022, then sunset — best
  "worked as designed, no viable market" case), InsurAce, Solace (Nov 2022), Bridge
  Mutual, Unslashed, Cover Protocol (exploited 2020), Tidal, Bright Union.
- **AXA fizzy**: Ethereum parametric flight delay, worked perfectly, killed 2019 —
  demand didn't justify it. Automation alone doesn't sell policies.
- **Lemonade Crypto Climate Coalition**: Kenya pilots (Chainlink/Etherisc/Hannover Re/ACRE),
  then silence post-2023. Incumbent R&D/PR, no durable business.
- **Amulet** (Solana): V1 sunset → pivoted to Eclipse L2. No durable Solana-native risk pool.
- **Xiang Hu Bao** (Ant Group): ~105M members as "mutual aid plan", shut down Jan 2022 —
  CBIRC reclassified as unlicensed insurance. THE cautionary tale: tech+distribution scaled
  fine; the license was the binding constraint.

## Cross-cutting lesson
Parametric + oracle worked technically EVERY time. Failures were always distribution,
capital cost, correlated demand, or regulation — never the tech.

## Regulatory reality (follow-up question: "are mutuals easier?" — answer: no)
- Substance over form: mutual = ownership structure, not a regulatory category. VVaG,
  mutuelle, incorporated friendly society, US mutual = all licensed insurers. Solvency II
  form-agnostic. MiCA excludes insurance → no EU arbitrage.
- Four real carve-outs: (1) small-mutual exemptions with hard caps + closed membership
  (UK registered friendly societies FSA 1974 c.46 [V]; German small-VVaG exemption,
  region/occupation-restricted; US fraternals/town-farm mutuals) — caps exist precisely
  to prevent shadow insurers; open global crypto pool violates closed-membership day one.
  (2) Discretionary no-promise pools (US healthcare sharing ministries, ~30 state safe
  harbors; German Vereine) — legally not insurance because no enforceable promise; on-chain
  escrow + code-executed redistribution restores credibility without a legal promise;
  untested at scale. (3) Tontine mechanics (Forman & Sabin) — redistribute own funds, no
  guarantee → not insurance; fits longevity, awkward for hazard. (4) Microinsurance
  licenses (Kenya/Ghana/Philippines/India): reduced capital tiers, simplified filing,
  mobile-channel rules, sandboxes, several explicitly allow mutual/coop microinsurers —
  the practical path. Philippines = friendliest EM regime.
- Doesn't help: DAO wrappers (legal personality ≠ insurance license); parametric can be
  worse (derivative reclassification risk). Mutuals harder to capitalize (no share capital).

## Design thesis delivered
Parametric crop/weather cover; satellite/rainfall index (CHIRPS 0.05° rainfall, Sentinel-2
NDVI 10m — free, 2-3wk final latency); Solana contract; stablecoin payout via mobile-money
off-ramp; licensed local carrier fronting; Tributary-style recurring micro-premiums;
on-chain reserve as the visible trust feature. Binding constraints in order: basis risk /
index design, licensing, distribution & trust, stablecoin CICO.

## Key academic anchors [E]
Clarke 2016 Economica (basis risk can make fair index insurance welfare-reducing);
Cole et al. 2013 AEJ:Applied; Jensen/Barrett/Mude IBLI; Forman & Sabin, Tontine Pensions
(U. Penn L. Rev.); arXiv 2412.05321 (Dec 2024) — collaborative parametric pool,
surplus-provider tokens, Solidity PoC [V].
