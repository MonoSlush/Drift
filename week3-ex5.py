import yaml
from os import path
from netmiko import ConnectHandler
from pprint import pprint

home_dir = path.expanduser("~")
filename = path.join(home_dir, ".netmiko.yml")



with open(filename) as f:
    yaml_out = yaml.safe_load(f)

# pprint(yaml_out)

cisco3_dict = yaml_out['cisco3']

# pprint(cisco3_dict)

cisco3_connect = ConnectHandler(**cisco3_dict)
print(cisco3_connect.find_prompt())
