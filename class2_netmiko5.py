#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

devices = {
   "device1": {
       "host": "nxos1.lasthop.io",
       "username":"pyclass",
       "password":password,
       "device_type":"cisco_nxos",
   }, 
   "device2": {
      "host":"nxos2.lasthop.io",
      "username":"pyclass",
      "password":password,
      "device_type":"cisco_nxos",
   }, 
}

for name, device in devices.items():
    print(f"\n=== Connecting to {name}===")
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_from_file(config_file='vlan_config.txt')
    print()
    pprint(output)
    save_out = net_connect.save_config()
    print(save_out) 




