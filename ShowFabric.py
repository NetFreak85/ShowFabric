# coding=utf-8
import requests
import json
import warnings
import getCookie

#Print 
def printAux():
	print("+-------------------------------------------+")

#Get Resquest to APICs and return a json object
def get_request(url, cookie):
	r = requests.get(url, cookies=cookie, verify=False)
	json_obj = json.loads(r.content)
	return json_obj

#Method that discovery all the ACI Members and print values
def findFabric(apicIP, cookie):
	response = get_request('https://%s/api/node/class/fabricNode.json?&order-by=fabricNode.modTs|desc' % apicIP, cookie)
	
	#Print the number of members in the Fabric
	printAux()
	print("|   Number of member in the Fabric :   %s" % response['totalCount'] + "    |")
	printAux()
	
	#Print the Address, Model, Name, Role, S/N and NX-OS Version
	for i in range(0,int(response['totalCount'])):
		printAux()
		print ("   Address           :      %s" % response['imdata'][i]['fabricNode']['attributes']['address'])
		print ("   Model             :      %s" % response['imdata'][i]['fabricNode']['attributes']['model'])
		print ("   Name              :      %s" % response['imdata'][i]['fabricNode']['attributes']['name'])
		print ("   Role              :      %s" % response['imdata'][i]['fabricNode']['attributes']['role'])
		print ("   Serial Number     :      %s" % response['imdata'][i]['fabricNode']['attributes']['serial'])
		print ("   Version NX-OS     :      %s" % response['imdata'][i]['fabricNode']['attributes']['version'])
		printAux()

#Main program
if __name__ == '__main__':

    user = "admin"
    passwd = "C1sc0123"
    apic = "a1networking.igrupobbva"
    cookie = getCookie.get_cookie(apic, user, passwd)	
    findFabric(apic,cookie)
