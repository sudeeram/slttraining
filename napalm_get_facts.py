#!/usr/bin/env python

from netmiko import ConnectHandler
from pprint import pprint
from netmiko import ConnectHandler
from napalm import get_network_driver

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



	driver = get_network_driver('ios')
	optional_args = {}
	optional_args['secret'] = 'cisco'

	# mgmt_ip = input("Device IP: ")
	mgmt_ip = router1["ip"]

	#device = driver(mgmt_ip, 'cisco', 'cisco')
	device = driver(mgmt_ip, 'cisco', 'cisco', optional_args=optional_args)
	device.open()
	# facts = device.get_facts()
	# pprint(facts)

	# facts = device.get_interfaces()
	# pprint(facts)

	# facts = device.get_bgp_neighbors()
	# pprint(facts)

	# facts = device.ping('172.25.1.3')
	# pprint(facts)

	facts = device.traceroute('172.25.1.2')
	pprint(facts)


	# facts = device.get_interfaces_counters()
	# print (facts)
	# for interface, values in facts.items():
	# 	print (interface)



if __name__ == '__main__':
	main()