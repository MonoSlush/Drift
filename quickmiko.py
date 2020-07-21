import os
from getpass import getpass
from netmiko import ConnectHandler

password = os.getenv('PYNET_PASSWORD') if os.getenv('PYNET_PASSWORD') else getpass()

nxos1 = {
'host': 'nxos1.lasthop.io',
'username': 'pyclass',
'password': password,
'device_type': 'cisco_nxos',
}

nxos2 = {
'host': 'nxos2.lasthop.io',
'username': 'pyclass',
'password': password,
'device_type': 'cisco_nxos',
}


connection_list = [nxos1, nxos2]
for device in connection_list:
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())


# net_connect = ConnectHandler(**nxos1)
# print(net_connect.find_prompt())

cisco3 = {
'host': 'cisco3.lasthop.io',
'username': 'pyclass',
'password': password,
'device_type': 'cisco_ios',
}

show_version = 'show version'

cisco3_connect = ConnectHandler(**cisco3)




print(cisco3_connect.find_prompt())
print(cisco3_connect.send_command(show_version))

