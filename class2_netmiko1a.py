#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
device1 = {
     "host": "cisco4.lasthop.io",
     "username": "pyclass",
     "password": password,
     "device_type": "cisco_nxos"
}
net_connect = ConnectHandler(**device1)
command = 'ping'
output = net_connect.send_command_timing(command, strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("8.8.8.8", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
net_connect.disconnect

print()
print(output)
print()
