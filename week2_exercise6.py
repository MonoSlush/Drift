from netmiko import ConnectHandler
import time

cisco4 = {
    "host":" cisco4.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "secret": "88newclass",
    "device_type": "cisco_ios",
    "session_log": "week2_exercise6_log.txt",
}

cisco4_connect = ConnectHandler(**cisco4)
print(cisco4_connect.find_prompt())
cisco4_connect.config_mode()
print(cisco4_connect.find_prompt())
cisco4_connect.exit_config_mode()
print(cisco4_connect.find_prompt())
 
print("\nExit privileged exec (disable), Current Prompt: ")
cisco4_connect.write_channel("disable\n")
time.sleep(2)
output = cisco4_connect.read_channel()
print(output)

print("\nRe-enter enable mode, Current Prompt: ")
cisco4_connect.enable()
print(cisco4_connect.find_prompt())

cisco4_connect.disconnect()
print()
