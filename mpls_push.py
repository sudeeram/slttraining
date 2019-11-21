#!/usr/bin/env python

# from ciscoconfparse import CiscoConfParse
from netmiko import ConnectHandler

__author__ = "Sudeera Mudugamuwa"

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
		filename = "file_" + router['ip'] + '_mplsconfig.cfg'

		commandset = []
		with open(filename, 'r') as read_f:
			for line in read_f:
				commandset.append(line.strip('\n').strip())

		
		print ("Connecting to", router["ip"] )
		con = ConnectHandler(**router)
		
		print ("Writing Config ...")
		print (commandset)
		output = con.send_config_set(commandset)
		print (output)


if __name__ == '__main__':
	main()




