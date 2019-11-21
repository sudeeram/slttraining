#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse
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
	# router2 = {
	# 	'device_type'	: 'cisco_ios',
	# 	'ip' 			: '172.25.1.2',
	# 	'username'		: 'cisco',
	# 	'password'		: 'cisco',
	# 	'secret'		: 'cisco',
	# }
	# router3 = {
	# 	'device_type'	: 'cisco_ios',
	# 	'ip' 			: '172.25.1.3',
	# 	'username'		: 'cisco',
	# 	'password'		: 'cisco',
	# 	'secret'		: 'cisco',
	# }

	# routers = [router1, router2, router3]
	routers = [router1]

	for router in routers:
		filename = "file_" + router['ip'] + '_show_run.cfg'

		with open(filename, 'r') as read_f:
			parse = CiscoConfParse(read_f)

			print ("Interface Configuration on the Device")
			print ("=====================================")

			for intf in parse.find_objects(r'^interface'):
				print (intf.text)

			print ("VRF Configuration on the Device")
			print ("===============================")

			for vrf in parse.find_objects(r'^ip vrf'):
				print (vrf.text)



if __name__ == '__main__':
	main()




