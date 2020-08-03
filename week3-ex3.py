from pprint import pprint
from netmiko import ConnectHandler
import re

json_output = {
    "Ethernet2/1": {
        "ipv4": {
            "1.1.1.1": {
                "prefix_length": 24
            }
        }
    },
    "Ethernet2/2": {
        "ipv4": {
            "2.2.2.2": {
                "prefix_length": 27
            }, 
            "3.3.3.3": {
                "prefix_length": 25
            }
        }
    }, 
    "Ethernet2/3": {
        "ipv4": {
            "4.4.4.4": {
                "prefix_length": 16
            }
        }, 
        "ipv6": {
            "fe80::2ec2:60ff:fe4f:feb2": {
                "prefix_length": 64
            }, 
            "2001:db8::1": {
                "prefix_length": 10
            }
        }
    }, 
    "Ethernet2/4": {
        "ipv6": {
            "fe80::2ec2:60ff:fe4f:feb2": {
                "prefix_length": 64
            }, 
            "2001:11:2233::a1": {
                "prefix_length": 24
            }, 
            "2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2": {
                "prefix_length": 64
            }
        }
    } 
}


ipv4_list = []
ipv6_list = []

#for intf, int_dict in json_output.items():
#    for v4_v6, addr_info in int_dict.items():
#        for ip_addr, prefix_dict in addr_info.items():
#            prefix_length = prefix_dict['prefix_length']
#            if v4_v6 in ip_addr == 'ipv4':
#                ipv4_list.append('{}/{}'.format(ip_addr, prefix_length))
#            elif v4_v6 in ip_addr == 'ipv6':
#               ipv6_list.append('{}/{}'.format(ip_addr, prefix_length))
#
#
#print(ipv4_list, ipv6_list)


