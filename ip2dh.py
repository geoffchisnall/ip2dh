#!/usr/bin/python3
## Convert an IP Address to Decimal and Hex

import sys
import ipaddress


#Validate IP address

def validate_ip(raw_ip):

	try:
		ip = ipaddress.ip_address(raw_ip)
		return ip.version == 4
	except:
		print("This is not a valid IP Address.")

#Convert IP Address
	
def convert_ip(rawip):
	ip = rawip.split('.')
	ip = list(map(int, ip))
	dip = (ip[0]*2**24 + ip[1]*2**16 + ip[2]*2**8 + ip[3])
	print("IP Address:", rawip,"\n")
	print("Decimal:", dip)
	hip = (hex(dip))
	print("Hex:", hip)

#	return ip

if __name__ == '__main__':
	if len(sys.argv) != 1:
		if  validate_ip(sys.argv[1]) == True:
			convert_ip(sys.argv[1])

	else:
		print("Usage:", sys.argv[0], "127.0.0.1")
	
