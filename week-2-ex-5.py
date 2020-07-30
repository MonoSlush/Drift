from pprint import pprint
from netmiko import ConnectHandler
from datetime import datetime

nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_nxos",
}   

nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_nxos",
}    

nxos1_connect = ConnectHandler(**nxos1)
nxos2_connect = ConnectHandler(**nxos2)

week2_exercise5_txt = []
with open('week2_exercise5.txt') as txt:
    week2_exercise5_txt = txt.readlines()

# print(week2_exercise5_txt)

nxos1_output_1 = (nxos1_connect.send_config_from_file(config_file='week2_exercise5.txt'))
nxos1_output_2 = (nxos1_connect.save_config())

print(nxos1_output_1, nxos1_output_2)

nxos1_output_3 = (nxos1_connect.send_command('show vlan brief'))

print(nxos1_output_3)
