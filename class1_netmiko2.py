#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

devices = {
    "device1": {
        "host": "nxos1.lasthop.io",
        "username": "pyclass",
        "password": password,
        "device_type": "cisco_nxos"
    },
    "device2": {
        "host": "nxos2.lasthop.io",
        "username": "pyclass",
        "password": password,
        "device_type": "cisco_nxos"
    }
}

for device, device_params in devices.items():
    net_connect = ConnectHandler(**device_params)
    print(net_connect.find_prompt())
    net_connect.disconnect()

