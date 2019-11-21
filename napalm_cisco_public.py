#!/usr/bin/env python

from netmiko import ConnectHandler
from pprint import pprint
from netmiko import ConnectHandler
from napalm import get_network_driver

def main():
	router1 = {
		'device_type'	: 'cisco_xe',
		'ip' 			: 'ios-xe-mgmt.cisco.com',
		'port'			: '8181', # Not required if default SSH
		'username'		: 'root',
		'password'		: 'D_Vay!_10&'
	}


	routers = [router1]

	driver = get_network_driver('ios')
	optional_args = {}

	# mgmt_ip = input("Device IP: ")
	mgmt_ip = router1["ip"]

	#device = driver(mgmt_ip, 'cisco', 'cisco')
	device = driver(mgmt_ip, router1['username'], router1['password'])
	device.open()
	facts = device.get_facts()
	pprint(facts)

	# facts = device.get_interfaces()
	# pprint(facts)

	# facts = device.get_bgp_neighbors()
	# pprint(facts)

	# facts = device.get_interfaces_counters()
	# print (facts)
	# for interface, values in facts.items():
	# 	print (interface)



if __name__ == '__main__':
	main()