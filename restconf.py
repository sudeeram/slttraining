import requests
import sys

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# use the IP address or hostname of your CSR1000V
HOST = 'ios-xe-mgmt.cisco.com'
# use the HTTPS port for RESTCONF on your CSR1000V
PORT = 9443
# use your user credentials to access the CSR1000V
USER = 'root'
PASS = 'D_Vay!_10&'


# create a main() method
def main():
    """Main method that retrieves the hostname from CSR1000V via RESTCONF."""

    # url string to issue GET request
    # url = "https://{h}:{p}/api/running/native/hostname".format(h=HOST, p=PORT)
    # url = "https://{h}:{p}/restconf/data/ietf-yang-library:modules-state".format(h=HOST, p=PORT)
    url = "https://{h}:{p}/restconf/data/Cisco-IOS-XE-native:native/interface".format(h=HOST, p=PORT)

    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
    # this statement performs a GET on the specified url
    response = requests.get(url, auth=(USER, PASS),
                            headers=headers, verify=False)

    # print the json that is returned
    print(response.text)

if __name__ == '__main__':
    sys.exit(main())