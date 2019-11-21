from ncclient import manager
from demo import iosxeao
from xml.dom import minidom

iosxe_manager = manager.connect( 
host = iosxeao["address"], 
port = iosxeao["netconf_port"], 
username = iosxeao["username"], 
password = iosxeao["password"], 
hostkey_verify = False)

# The output will be True or False
iosxe_manager.connected

# iosxe_manager.server_capabilities


config = iosxe_manager.get_config("running")
# config = iosxe_manager.get_config("running", filter_iosxe_platform)

iosxe_config_xml = minidom.parseString(config.xml)
print (iosxe_config_xml.toprettyxml(indent = "   "))

# create_loopback = """
# <config>
#   <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
#     <interface>
#       <name>Loopback1025</name>
#       <description>Another Netconf Loopback</description>
#       <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
#         ianaift:softwareLoopback
#       </type>
#       <enabled>true</enabled>
#       <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
#         <address>
#           <ip>172.32.5.6</ip>
#           <netmask>255.255.255.255</netmask>
#         </address>
#       </ipv4>
#     </interface>
#   </interfaces>
# </config>
# """

# iosxe_create_loopback = iosxe_manager.edit_config(target = 'running', config = create_loopback)









