

from netmiko import ConnectHandler
from pprint import pprint

hostnames = ['cisco3', 'cisco4', 'arista1', 'arista2', 'srx2']

user_pass = ['admin', 'pass']

#dev_dict = {}
#dev_dict_list = []

#for device in hostnames:
#    dev_dict_list.append({
#       'FQDN': device,
#        'User': user_pass[0],
#        'Pass': user_pass[1],
#    })

#print(dev_dict_list)

#dev_dict_string = (f'{dev_dict_list}')

#pprint(dev_dict_string)

#dict_output = []
#for dict in dev_dict_list:
#   dict_output.append(dict)

#print(dict_output)

#print(dev_dict_string)

#dev_dict_split = dev_dict_string.split(',')

#print(dev_dict_split)


#with open('week3-ex2b.txt', mode='w') as f:
#    f.write(dev_dict_string)
#    f.flush()



#dev_dict_yam = (f'''
#---


import yaml
from pprint import pprint

cisco3 = {"device_name": "cisco3", "host": "cisco3.lasthop.io"}

cisco4 = {"device_name": "cisco4", "host": "cisco4.lasthop.io"}

arista1 = {"device_name": "arista1", "host": "arista1.lasthop.io"}

arista2 = {"device_name": "arista2", "host": "arista2.lasthop.io"}

my_devices = [cisco3, cisco4, arista1, arista2]
for device in my_devices:
    device["username"] = "admin"
    device["password"] = "cisco123"

print()
pprint(my_devices)
print()

with open("my_devices.yml", "w") as f:
    yaml.dump(my_devices, f, default_flow_style=False)
   
