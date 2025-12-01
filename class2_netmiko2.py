#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

device1 = {
     "host": "nxos2.lasthop.io",
     "username": "pyclass",
     "password": password,
     "device_type": "cisco_nxos"
}
net_connect = ConnectHandler(**device1)
command = 'show lldp neighbors detail'
output = net_connect.send_command(command)
net_connect.disconnect

print()
print(output)
print()
