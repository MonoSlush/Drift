import yaml
from os import path
from netmiko import ConnectHandler
from pprint import pprint
 
home_dir = path.expanduser("~")
filename = path.join(home_dir, ".netmiko.yml")
 
 
 
with open(filename) as f:
    yaml_out = yaml.safe_load(f)

# pprint(yaml_out)
 
cisco4_dict = yaml_out['cisco4']

# pprint(cisco4_dict)
 
cisco4_connect = ConnectHandler(**cisco4_dict)
print(cisco4_connect.find_prompt())

print(cisco4_connect.send_command('show run'))
