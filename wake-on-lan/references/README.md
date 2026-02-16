# Wake-on-LAN Reference

## How Wake-on-LAN Works

Wake-on-LAN (WoL) is a networking standard that allows a powered-off or sleeping computer to be turned on by a network message. The message is called a "magic packet" and contains the MAC address of the target computer.

### Requirements

1. **Network Interface**: The target machine must have a network interface that supports Wake-on-LAN
2. **Motherboard/BIOS**: Must have WoL enabled in BIOS/UEFI settings
3. **Network Card**: Must support Wake-on-LAN (most modern network cards do)
4. **Power**: Machine must be connected to power (even when "off")

### Magic Packet Format

- Contains 6 bytes of all 0xFF (broadcast indicator)
- Followed by 16 repetitions of the target MAC address
- Total size: 102 bytes

## Finding MAC Addresses

### From Command Line (Linux)

```bash
# Show all network interfaces and their MAC addresses
ip link show

# Show ARP table for specific IP
ip neigh show 192.168.1.100

# Send ping and check ARP
ping -c 1 192.168.1.100 && ip neigh show 192.168.1.100
```

### From Router/Web Interface

Most routers provide a list of connected devices with their MAC addresses:
- Fritz!Box: fritz.box > Heimnetz > Netzwerk
- OpenWRT: LuCI > Status > Devices
- pfSense: Interfaces > ARP table

### From Windows

```cmd
ipconfig /all
```

### From macOS

```bash
ifconfig | grep ether
```

## Configuration

### Machine Configuration

Each machine entry in `machines.json` contains:
- `mac_address`: Required, format: AA:BB:CC:DD:EE:FF
- `ip_address`: Optional, for status checking
- `description`: Optional, human-readable description
- `last_wake`: Timestamp of last successful wake (auto-updated)

### Network Configuration

- **Broadcast IP**: Default 255.255.255.255 (local network broadcast)
- **Port**: Default 9 (standard WoL port), can be 7 or 0-1023
- **Subnet**: Must be reachable (no VLAN/routing restrictions)

## Usage Examples

### CLI Usage

```bash
# Add a new machine
python3 scripts/wake_on_lan_manager.py --action add --name server1 --mac AA:BB:CC:DD:EE:FF --ip 192.168.1.100

# List all machines
python3 scripts/wake_on_lan_manager.py --action list

# Wake a specific machine
python3 scripts/wake_on_lan_manager.py --action wake --name server1

# Wake all machines
python3 scripts/wake_on_lan_manager.py --action wake

# Check machine status
python3 scripts/wake_on_lan_manager.py --action status

# Remove a machine
python3 scripts/wake_on_lan_manager.py --action remove --name server1
```

### Python API

```python
from scripts.wake_on_lan_manager import WakeOnLanManager

manager = WakeOnLanManager()
manager.add_machine("server1", "AA:BB:CC:DD:EE:FF", "192.168.1.100")
print(manager.wake_machine("server1"))
print(manager.check_machine_status("server1"))
```

## Troubleshooting

### Common Issues

1. **Magic Packet Not Received**
   - Check firewall rules on sender
   - Verify network connectivity
   - Try different broadcast IP (subnet broadcast)

2. **Machine Doesn't Wake**
   - Verify WoL is enabled in BIOS/UEFI
   - Check power settings in OS
   - Ensure network cable is connected
   - Test with different network interface

3. **Permission Denied**
   - Run script with sudo if needed
   - Check wakeonlan package installation

### Testing

1. **Test with ping**: Ensure you can ping the machine when it's awake
2. **Test manually**: Use `wakeonlan AA:BB:CC:DD:EE:FF` from command line
3. **Check logs**: Monitor system logs for network events

## Security Considerations

- Magic packets are sent in clear text
- Restrict access to your local network
- Consider using MAC address filtering if supported by your router
- Wake-on-LAN should be disabled on unused machines