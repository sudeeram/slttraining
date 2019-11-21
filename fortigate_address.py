#!/usr/bin/env python

from ftntlib import FortiOSREST
import json
import ssl
import sys
import getopt
import getpass
import base64
from pprint import pprint
import ast

def main():

	verbose = True
	hostname = "192.168.160.14"
	username = "admin"
	password = "admin"
	vdom = "root"
	port1 = "port1"
	port2 = "port2"
	verbose = False
	undo = False
	showConfig = False
	resultTemplate = "{0:30}{1:30}{2:20}"

	AdrObjs = {
		"AdrObj" :
		[
			{
			"name": "TEST_SUBNET_1",
			"subnet": "10.100.1.0 255.255.255.0"
			},
			{
			"name": "TEST_SUBNET_2",
			"subnet": "10.100.2.0 255.255.255.0"
			},
			{
			"name": "TEST_SUBNET_3",
			"subnet": "10.100.3.0 255.255.255.0"
			},
			{
			"name": "TEST_SUBNET_4",
			"subnet": "10.100.4.0 255.255.255.0"
			},
		]
	}

	fgt = FortiOSREST()
	fgt._https = False
	# if verbose: fgt.debug('on')   
	result = fgt.login(hostname, username, password)
	print (result)
	if verbose: 
		print (result)  

	print ("****** add Addresses to Fortigate *******")
	for AdrObj in AdrObjs["AdrObj"]:
		postData = {
			"json" : {
				"name": AdrObj["name"],
				"subnet": AdrObj["subnet"],
				"type": "ipmask",
				"cache-ttl": 0,
				"comment": "",
				"visibility": "enable",
				"associated-interface": ""
			}
		}
		response = fgt.post('cmdb', 'firewall', 'address', parameters={"vdom": vdom}, data=postData)
		json_response = json.loads(response)
		print (resultTemplate.format("Add Address Object", str(json_response["name"]), str(json_response["status"])))

	# response = fgt.get('cmdb', 'firewall', 'address', parameters={ "scope": "global"})
	# response = fgt.get('cmdb', 'firewall', 'address', parameters={ "vdom": vdom})



	# response = fgt.get('cmdb', 'firewall', 'policy', parameters={ "vdom": vdom})
	# response = fgt.get('cmdb', 'firewall', 'address', parameters={ "vdom": vdom})
	# new_response = response.decode('utf-8')
	# new_response_dict = ast.literal_eval(new_response)




	# print (type(new_response))
	# pprint (new_response_dict['results'])

	# print ("****** show the config *******")
	# response = fgt.get('monitor', 'system', 'config', 'backup', parameters={"scope": "global"})
	# response = fgt.get('monitor', 'system', 'config', 'backup', parameters={"scope": "global"})
	# print (str(response).split("\n",1)[0]) 
	# print (str(response).split("\n",1)[1])
	# if verbose: 
	# 	json_response = json.loads(response)
	# print ("Full Config: \n" + str(json_response))
	# print ("****** DONE *******")




	

	
            


















if __name__ == '__main__':
	main()