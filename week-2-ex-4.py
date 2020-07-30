from pprint import pprint
from netmiko import ConnectHandler
from datetime import datetime
  
cisco3 = {
    "host":" cisco3.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios",
    "fast_cli": True,
}

cisco3_connect = ConnectHandler(**cisco3)

command_set = [
'ip name-server 1.1.1.1',
'ip name-server 1.0.0.1',
'ip domain-lookup'
]

start_time = datetime.now()
show_output = cisco3_connect.send_config_set(command_set)
end_time = datetime.now()
  
print('#' * 80)
print(show_output)
print('#' * 80)
print('\n\nExecution Time: {}'.format(end_time - start_time))
print('#' * 80)
print(cisco3_connect.send_command('ping google.com', delay_factor=4))
print('#' * 80)


