""" PY TO ESP (LED CONTROLLER) """
# Written by Junicchi - https://github.com/Kebablord

import urllib.request
root_url = "http://192.168.1.19/"  # ESP's url, ex: http://192.168.102 (Esp prints it to serial console when connected to wifi)
#ip adress suzanne 192.168.1.19
#ip adress Peloquin 192.168.123.7

def sendRequest(url):
	n = urllib.request.urlopen(url) # send request to ESP

# Example usage
def ledControl(open):

	if(open):
		sendRequest(root_url + "CLOSE_LED")
	else:
		sendRequest(root_url + "OPEN_LED")

def ledEffects(command):
	command = root_url + "OPEN_LED," + command
	print(command)
	sendRequest(command)

def closeLED():
	print("closing LED")
	command = root_url + "CLOSE_LED"
	sendRequest(command)