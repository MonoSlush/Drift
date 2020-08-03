
from pprint import pprint
from netmiko import ConnectHandler
import re

arp_string = '''
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
'''

# print(arp_string)


list_of_arp_dicts = []

split_arp_string = arp_string.splitlines()

for line in split_arp_string:
    split_line = re.split(r'\s+', line)
    if split_line[0] == 'Internet':
        list_of_arp_dicts.append({
            'macaddr': split_line[3],
            'address': split_line[1],
            'interface': split_line[5],
        })

pprint(list_of_arp_dicts)













