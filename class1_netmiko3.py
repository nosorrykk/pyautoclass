#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

device1 = {
     "host": "nxos1.lasthop.io",
     "username": "pyclass",
     "password": password,
     "device_type": "cisco_nxos"
}
net_connect = ConnectHandler(**device1)
show_version = net_connect.send_command("show version")
with open("show_version.txt", "w") as f:
     f.write(show_version)
net_connect.disconnect
