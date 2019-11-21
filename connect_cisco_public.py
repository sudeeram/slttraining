from netmiko import ConnectHandler

def main():
	router1 = {
		'device_type'	: 'cisco_xe',
		'ip' 			: 'ios-xe-mgmt.cisco.com',
		'port'			: '8181',
		'username'		: 'root',
		'password'		: 'D_Vay!_10&'
	}

	# SSH INTO ROUTER
	print ("Connecting to router1 (%s)" % router1["ip"])
	r1_con = ConnectHandler(**router1)
	print ("************************")
	command = 'terminal length 0'
	output = r1_con.send_command(command)

	# EXECUTE A SHOW RUN COMMAND
	command = 'show run'
	print ("Executing %s" %command)
	output = r1_con.send_command(command)
	print (output)
	r1_con.disconnect()

if __name__ == '__main__':
	main()