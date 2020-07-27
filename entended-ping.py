from netmiko import ConnectHandler

#cisco4 (Cisco IOS-XE)
#    hostname = cisco4.lasthop.io
#    snmp_port = 161
#    ssh_port = 22
#    username = pyclass
#    password = 88newclass

password = 'mzd3nwtydN'

cisco4 = {
    'device_type': 'cisco_ios',
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': password,
}

net_connect = ConnectHandler(**cisco4)
print(net_connect.findprompt())

