# coding=utf-8
#**********************************************************************************
#    This script is for discovery all the members in the Cisco ACI Fabric
#	 The script will print the following information:
#		IP Management Address
#		Model
#		Name
#		Role
#		Serial Number
#		NX-OS Version
#		System Uptime
#		System Last Reboot
#		Current System Time
#		TEP IP Address
#		TEP Pool
#		Mac Address
#
#   --usage:
#             ./ShowFabric.py  
#         or  python ShowFabric.sh  
#
# date:  01/09/2021 Created
#**********************************************************************************

import requests
import json
import warnings
import getCookie
import Constant

def printAux():
	print("+---------------------------------------------------------------+")

#Get Resquest to APICs and return a json object
def get_request(url, cookie):
	r = requests.get(url, cookies=cookie, verify=False)
	json_obj = json.loads(r.content)
	return json_obj

#Method that discovery all the ACI Members and print values
def findFabric(apicIP, cookie):
	response = get_request('https://%s/api/node/class/fabricNode.json?&order-by=fabricNode.modTs|desc' % apicIP, cookie)
	NodeInfo = get_request('https://%s/api/node/class/topSystem.json?&order-by=topSystem.modTs|desc' % apicIP, cookie)

	#Print the number of members in the Fabric
	printAux()
	print("    Number of member in the Fabric :   %s" % response['totalCount'])
	printAux()

	#Print the Fabric Info
	for i in range(0,int(response['totalCount'])):
		print ("   Management IP Address   :      %s" % NodeInfo['imdata'][i]['topSystem']['attributes']['inbMgmtAddr'])
		print ("   Model                   :      %s" % response['imdata'][i]['fabricNode']['attributes']['model'])
		print ("   Name                    :      %s" % response['imdata'][i]['fabricNode']['attributes']['name'])
		print ("   Role                    :      %s" % response['imdata'][i]['fabricNode']['attributes']['role'])
		print ("   Serial Number           :      %s" % response['imdata'][i]['fabricNode']['attributes']['serial'])
		print ("   Version NX-OS           :      %s" % response['imdata'][i]['fabricNode']['attributes']['version'])
		print ("   TEP IP Address          :      %s" % response['imdata'][i]['fabricNode']['attributes']['address'])
		print ("   TEP POOL                :      %s" % NodeInfo['imdata'][i]['topSystem']['attributes']['tepPool'])
		print ("   Fabric Mac Address      :      %s" % NodeInfo['imdata'][i]['topSystem']['attributes']['fabricMAC'])
		print ("   System Uptime           :      %s" % NodeInfo['imdata'][i]['topSystem']['attributes']['systemUpTime'])
		print ("   Current System Time     :      %s" % NodeInfo['imdata'][i]['topSystem']['attributes']['currentTime'])
		print ("   Last Reboot             :      %s" % NodeInfo['imdata'][i]['topSystem']['attributes']['lastRebootTime'])
		printAux()

#Main program
if __name__ == '__main__':

    cookie = getCookie.get_cookie(Constant.apic, Constant.User, Constant.Password)	
    findFabric(Constant.apic,cookie)
