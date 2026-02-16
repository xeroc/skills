name: wake-on-lan
description: Wake-on-LAN management for local network machines. Use when you need to wake up sleeping computers on the local network using magic packets. Supports managing multiple machines, checking their status, and sending wake commands with configurable timeouts and network settings.

## Quick Start

The Wake-on-LAN skill provides a complete solution for managing network wake-up commands:

- **Add machines**: Store MAC addresses and descriptions
- **List machines**: See all configured machines and their status  
- **Wake machines**: Send magic packets to power on machines
- **Check status**: Monitor online/offline status of machines

## Usage Examples

### Add a new machine
```
Add machine "truenas" with MAC address AA:BB:CC:DD:EE:FF
```
Or use the CLI: `python3 scripts/wake_on_lan_manager.py --action add --name truenas --mac AA:BB:CC:DD:EE:FF`

### Wake a specific machine
```
Wake up "jupiter" 
```
Or use the CLI: `python3 scripts/wake_on_lan_manager.py --action wake --name jupiter`

### Wake all machines
```
Wake up all configured machines
```

### Check machine status
```
Check status of "jupiter"
```

### List all machines
```
List all configured machines
```

## Configuration

Machine configurations are stored in `machines.json`:
```json
{
  "machines": {
    "jupiter": {
      "mac_address": "90:1b:0e:2b:e5:17",
      "ip_address": "192.168.178.49", 
      "description": "Jupiter server - currently online",
      "last_wake": null
    },
    "truenas": {
      "mac_address": "TBD",
      "ip_address": null,
      "description": "TrueNAS storage server - currently offline",
      "last_wake": null
    }
  }
}
```

## Finding MAC Addresses

For offline machines like truenas, find the MAC address by:

1. **From router admin interface**: Log into your Fritz!Box or router to see all connected devices and their MAC addresses
2. **From previous network scans**: Check if the device was previously connected and its MAC address is in ARP cache
3. **From device itself**: Check the device's network interface or system settings when it's powered on
4. **From documentation**: Check device manuals or previous configurations

## Network Requirements

- **Broadcast IP**: 255.255.255.255 (default) or your subnet broadcast address
- **Port**: 9 (standard) or 0-1023
- **Network**: Machines must be on the same subnet for broadcast to work

## Advanced Usage

### Custom Broadcast IP
```bash
python3 scripts/wake_on_lan_manager.py --action wake --name jupiter --broadcast 192.168.178.255
```

### Custom Port  
```bash
python3 scripts/wake_on_lan_manager.py --action wake --name jupiter --port 7
```

### Remove a machine
```bash
python3 scripts/wake_on_lan_manager.py --action remove --name oldserver
```

## Troubleshooting

If wake commands don't work:
1. **Verify MAC address**: Ensure the correct MAC address is configured
2. **Check BIOS settings**: Wake-on-LAN must be enabled in BIOS/UEFI
3. **Test with command line**: Use `wakeonlan 90:1b:0e:2b:e5:17` directly
4. **Check network connectivity**: Ensure sender can reach the broadcast address
5. **Review logs**: Monitor system logs for any errors

For detailed troubleshooting and technical information, see [references/README.md](references/README.md).

## Current Status

**Configured Machines:**
- ✅ **jupiter**: Online (MAC: 90:1b:0e:2b:e5:17, IP: 192.168.178.49)
- ⚠️ **truenas**: Offline - needs MAC address configured

**Tools Installed:**
- ✅ wakeonlan (magic packet sender)
- ✅ nmap (network scanning)
- ✅ Python script with management interface

The skill is ready to use. Just provide the MAC address for truenas to complete the configuration.