
import os
import sys; import time; from io import StringIO; import re
def extractIPs(fileContent):
    pattern = r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)([ (\[]?(\.|dot)[ )\]]?(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3})"
    ips = [each[0] for each in re.findall(pattern, fileContent)]   
    for item in ips:
        location = ips.index(item)
        ip = re.sub("[ ()\[\]]", "", item)
        ip = re.sub("dot", ".", ip)
        ips.remove(item)
        ips.insert(location, ip) 
    return ips
def portscanner(target):
    import sys
    import socket
    from datetime import datetime
    # Add Banner 
    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scanning started at:" + str(datetime.now()))
    print("-" * 50)
    lowerport= int(input("what port would you like to start scanning at?:"))
    upperport= int(input('what port would you like to finish scanning at?:'))
    try:
        
        # will scan ports user defines
        for port in range(lowerport,upperport):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            
            # returns an error indicator
            result = s.connect_ex((target,port))
            if result ==0:
                print("Port {} is open".format(port))
            s.close()
        print('End of open ports')
            
    except KeyboardInterrupt:
            print("\n Exitting Program !!!!")
            sys.exit()
    except socket.gaierror:
            print("\n Hostname Could Not Be Resolved !!!!")
            sys.exit()
    except socket.error:
            print("\ Server not responding !!!!")
            sys.exit()
###############################################################################
print('Welcome to simple sweep ~insert ascii art')
print('-' *50)
print('Would you like to scan the network for IPs or enter a specific IP to port scan?')
print('-'*50)
scantype= input('type "scan" to perform a scan on network or press enter to scan a specific IP: ')
if scantype == 'scan':

    scanresult = os.popen('arp -a').read()
    listofIPs= extractIPs(scanresult)
    for IP in listofIPs:
        portscanner(IP)
else:
    customIP= input("input a IPV4 address to scan:")
    portscanner(customIP)





