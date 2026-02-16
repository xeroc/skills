#!/usr/bin/env python3
"""
Wake-on-LAN Manager for local network machines
"""

import subprocess
import json
import sys
import argparse
from pathlib import Path

class WakeOnLanManager:
    def __init__(self, config_file=None):
        self.config_file = config_file or "/home/clawdbot/clawd/skills/wake-on-lan/machines.json"
        self.machines = self.load_config()
    
    def load_config(self):
        """Load machine configurations from JSON file"""
        try:
            with open(self.config_file, 'r') as f:
                data = json.load(f)
                return data.get('machines', {})
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def save_config(self):
        """Save machine configurations to JSON file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.machines, f, indent=2)
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def add_machine(self, name, mac_address, ip_address=None, description=""):
        """Add a new machine to the configuration"""
        self.machines[name] = {
            "mac_address": mac_address,
            "ip_address": ip_address,
            "description": description,
            "last_wake": None
        }
        self.save_config()
        return f"Added machine '{name}' with MAC {mac_address}"
    
    def remove_machine(self, name):
        """Remove a machine from the configuration"""
        if name in self.machines:
            del self.machines[name]
            self.save_config()
            return f"Removed machine '{name}'"
        return f"Machine '{name}' not found"
    
    def list_machines(self):
        """List all configured machines"""
        if not self.machines:
            return "No machines configured"
        
        output = "Configured machines:\n"
        for name, config in self.machines.items():
            mac = config.get('mac_address', 'Unknown')
            status = self.check_machine_status(name)
            output += f"- {name} ({mac}) - {status}\n"
        return output
    
    def check_machine_status(self, name):
        """Check if a machine is online using ping"""
        if name not in self.machines:
            return "Not found"
        
        ip_address = self.machines[name].get('ip_address')
        if not ip_address:
            return "Unknown (no IP configured)"
        
        try:
            result = subprocess.run(['ping', '-c', '1', '-W', '1', ip_address], 
                                  capture_output=True, text=True, timeout=5)
            return "Online" if result.returncode == 0 else "Offline"
        except subprocess.TimeoutExpired:
            return "Timeout"
        except Exception:
            return "Error"
    
    def wake_machine(self, name, broadcast_ip="255.255.255.255", port=9):
        """Wake up a machine by name"""
        if name not in self.machines:
            return f"Machine '{name}' not found"
        
        machine = self.machines[name]
        mac_address = machine['mac_address']
        
        try:
            # Use wakeonlan command
            result = subprocess.run(['wakeonlan', '-i', broadcast_ip, '-p', str(port), mac_address],
                                  capture_output=True, text=True, timeout=10)
            
            if result.returncode == 0:
                machine['last_wake'] = subprocess.run(['date'], capture_output=True, text=True).stdout.strip()
                self.save_config()
                return f"Successfully sent wake packet to {name} ({mac_address})"
            else:
                return f"Error sending wake packet: {result.stderr}"
        
        except subprocess.TimeoutExpired:
            return "Timeout sending wake packet"
        except FileNotFoundError:
            return "wakeonlan command not found. Please install wakeonlan package."
        except Exception as e:
            return f"Error: {str(e)}"
    
    def wake_all(self, broadcast_ip="255.255.255.255", port=9):
        """Wake up all configured machines"""
        if not self.machines:
            return "No machines configured"
        
        results = []
        for name in self.machines.keys():
            result = self.wake_machine(name, broadcast_ip, port)
            results.append(f"{name}: {result}")
        
        return "\n".join(results)

def main():
    parser = argparse.ArgumentParser(description="Wake-on-LAN Manager")
    parser.add_argument('--action', choices=['add', 'remove', 'list', 'wake', 'status'], 
                       required=True, help="Action to perform")
    parser.add_argument('--name', help="Machine name")
    parser.add_argument('--mac', help="MAC address")
    parser.add_argument('--ip', help="IP address")
    parser.add_argument('--description', default="", help="Machine description")
    parser.add_argument('--broadcast', default="255.255.255.255", help="Broadcast IP address")
    parser.add_argument('--port', type=int, default=9, help="Port number")
    
    args = parser.parse_args()
    
    manager = WakeOnLanManager()
    
    if args.action == 'add':
        if not args.name or not args.mac:
            print("Error: --name and --mac are required for add action")
            sys.exit(1)
        print(manager.add_machine(args.name, args.mac, args.ip, args.description))
    
    elif args.action == 'remove':
        if not args.name:
            print("Error: --name is required for remove action")
            sys.exit(1)
        print(manager.remove_machine(args.name))
    
    elif args.action == 'list':
        print(manager.list_machines())
    
    elif args.action == 'wake':
        if not args.name:
            print(manager.wake_all(args.broadcast, args.port))
        else:
            print(manager.wake_machine(args.name, args.broadcast, args.port))
    
    elif args.action == 'status':
        print(manager.list_machines())

if __name__ == "__main__":
    main()