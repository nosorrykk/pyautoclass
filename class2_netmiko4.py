#!/usr/bin/env python
from netmiko import ConnectHandler
from pprint import pprint
device1 = {
     "host": "cisco3.lasthop.io",
     "username": "pyclass",
     "password": "88newclass",
     "device_type": "cisco_ios",
##   "fast_cli": True,
}
net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output1 = net_connect.send_config_from_file(config_file='my_changes.txt')
output2 = net_connect.send_command("ping google.com")

print()
pprint(output1)
print()
print(output2)



