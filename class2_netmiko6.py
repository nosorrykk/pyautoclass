#!/usr/bin/env python
from netmiko import ConnectHandler
from pprint import pprint
from getpass import getpass
import os
import time

password = os.getenv("PYNET_PASSWORD") or getpass()
device = {
     "host": "cisco4.lasthop.io",
     "username": "pyclass",
     "password": password,
     "secret": password,
     "device_type": "cisco_ios",
     "session_log": "my_output.txt",
     "disable_sha2_fix": True,
}
net_connect = ConnectHandler(**device)
print("\n Executing the enable method:")
net_connect.enable()
output = net_connect.find_prompt()
print(output)

net_connect.disconnect()
##output1 = net_connect.send_config_from_file(config_file='my_changes.txt')
##output2 = net_connect.send_command("ping google.com")




