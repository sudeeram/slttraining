#!/usr/bin/env python

# from ciscoconfparse import CiscoConfParse

from netmiko import ConnectHandler

def main():
	router1 = {
		'device_type'	: 'cisco_ios',
		'ip' 			: '172.25.1.1',
		'username'		: 'cisco',
		'password'		: 'cisco',
		'secret'		: 'cisco',
	}
	router2 = {
		'device_type'	: 'cisco_ios',
		'ip' 			: '172.25.1.2',
		'username'		: 'cisco',
		'password'		: 'cisco',
		'secret'		: 'cisco',
	}
	router3 = {
		'device_type'	: 'cisco_ios',
		'ip' 			: '172.25.1.3',
		'username'		: 'cisco',
		'password'		: 'cisco',
		'secret'		: 'cisco',
	}

	routers = [router1, router2, router3]

	for router in routers:
		print ("Connecting to", router["ip"] )
		con = ConnectHandler(**router)
		command = 'show run'
		print ("Downloading config...")
		output = con.send_command(command)
		filename = "file_" + router['ip'] + '_show_run.cfg'
		with open(filename, 'w') as f:
			f.write(output)







if __name__ == '__main__':
	main()


