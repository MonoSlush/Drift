
from pprint import pprint
from netmiko import ConnectHandler

cisco4 = {
    "host":" cisco4.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios",
}

cisco4_connect = ConnectHandler(**cisco4)

show_lldp_neighbors_command = cisco4_connect.send_command('show lldp neighbors', use_textfsm=True)
show_version_command = cisco4_connect.send_command('show version', use_textfsm=True)

pprint(show_version_command)
pprint(show_lldp_neighbors_command)

print(show_lldp_neighbors_command[0]['neighbor_interface'])

#for key, value in show_lldp_neighbors_command.items():
#    if key == 'show version':
#        print(key, value)

cisco4_connect.disconnect()








