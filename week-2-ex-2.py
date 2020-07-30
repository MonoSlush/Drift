import os
from datetime import datetime
from netmiko import ConnectHandler

show_lldp_neighbors_detail = 'show lldp neighbors detail'

nxos2 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "global_delay_factor": 2,
}

nxos2_connect = ConnectHandler(**nxos2)

start_time = datetime.now()
show_output = nxos2_connect.send_command(show_lldp_neighbors_detail)
end_time = datetime.now()

print('#' * 80)
print(show_output)
print('#' * 80)
print('\n\nExecution Time: {}'.format(end_time - start_time))
print('#' * 80)
