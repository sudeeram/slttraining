#!/usr/bin/env python

# CISCO IOX XE ROUTER AVAILABLE ON CISCO DEVNET LAB

iosxeao_netconf = {
	'address' : 'ios-xe-mgmt.cisco.com',
	'netconf_port' : 10000,
	'restconf_port' : 9443,
	'username' : 'root',
	'password' : 'D_Vay!_10&',
}


def main():
	router1 = {
		'device_type'	: 'cisco_ios',
		'ip' 			: '192.168.160.5',
		'username'		: 'cisco',
		'password'		: 'cisco',
		'secret'		: 'cisco',
	}

	# SSH INTO ROUTER
	print ("Connecting to router1 (%s)" % router1["ip"])
	r1_con = ConnectHandler(**router1)
	print ("************************")

	# EXECUTE A SHOW IP INTERFACE BRIEF COMMAND
	command = 'show ip interface brief'
	print ("Executing %s" %command)
	output = r1_con.send_command(command)


if __name__ == '__main__':
	main()