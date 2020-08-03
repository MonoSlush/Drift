from pprint import pprint
from netmiko import ConnectHandler

arp_string = '''
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
'''

#print(arp_string)

list_of_arp_dicts = []

nu_split_arp_string = arp_string.splitlines()

arp_entry_1 = nu_split_arp_string[2]
arp_entry_2 = nu_split_arp_string[3]
arp_entry_3 = nu_split_arp_string[4]
arp_entry_4 = nu_split_arp_string[5]
arp_entry_5 = nu_split_arp_string[6]

arp_entry_1_split = arp_entry_1.split(' ')
arp_entry_2_split = arp_entry_2.split(' ')
arp_entry_3_split = arp_entry_3.split(' ')
arp_entry_4_split = arp_entry_4.split(' ')
arp_entry_5_split = arp_entry_5.split(' ')

arp_entry_1_dict = {
'mac_addr': arp_entry_1_split[7],
'ip_addr': arp_entry_1_split[2],
'interface': arp_entry_1_split[11],
}

arp_entry_2_dict = {
'mac_addr': arp_entry_2_split[6],
'ip_addr': arp_entry_2_split[2],
'interface': arp_entry_2_split[10],
}

arp_entry_3_dict = {
'mac_addr': arp_entry_3_split[7],
'ip_addr': arp_entry_3_split[2],
'interface': arp_entry_3_split[11],
}

arp_entry_4_dict = {
'mac_addr': arp_entry_4_split[5],
'ip_addr': arp_entry_4_split[2],
'interface': arp_entry_4_split[9],
}

arp_entry_5_dict = {
'mac_addr': arp_entry_5_split[5],
'ip_addr': arp_entry_5_split[2],
'interface': arp_entry_5_split[9],
}

#list_of_arp_dicts.append([arp_entry_1_dict, arp_entry_2_dict, arp_entry_3_dict, arp_entry_4_dict, arp_entry_5_dict])




pprint(list_of_arp_dicts)






