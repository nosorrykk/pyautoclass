#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

device1 = {
     "host": "cisco4.lasthop.io",
     "username": "pyclass",
     "password": password,
     "device_type": "cisco_ios"
}
net_connect = ConnectHandler(**device1)
command1 = 'show version'
command2 = 'show lldp neighbors'
output1 = net_connect.send_command(command1, use_textfsm=True)
output2 = net_connect.send_command(command2, use_textfsm=True)

net_connect.disconnect()

print()
print(output1)
print()
print(output2)
print()
print(type(output2))
print()
print(output2[0]['local_interface'])
print()

