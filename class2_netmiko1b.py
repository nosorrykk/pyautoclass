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
output = net_connect.send_command(command, expect_string=r"Protocol", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Target IP address", strip_prompt=False, strip_command=False)
output += net_connect.send_command( "8.8.8.8", expect_string=r"Repeat count", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Datagram size", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Timeout in seconds", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Extended commands", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Sweep range of sizes", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
net_connect.disconnect

print()
print(output)
print()

