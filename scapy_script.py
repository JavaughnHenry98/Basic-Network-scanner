from scapy.all import ARP, Ether, srp

target_ip = "192.168.1.1/24"
#IP Address for the Destination
#create ARP packet

arp= ARP(pdst=target_ip)
#create the Ether broadcast packet
#ff:ff:ff:ff:ff:ff MAC address indicates bradcasting

ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# stack them

packet = ether/arp

result = srp(packet, timeout =3)[0] 

# a list of clients, we will fill this in the upcoming loop
clients = [] 

for sent, recieved in result:
        #for each response, append ip and mac address to 'clients' list
        clients.append({'ip': recieved.psrc, 'mac': recieved.hwsrc})

# print clients
print("available devices in the network:")

print("IP' + "*18+"MAC")
for client in clients:

        print("{:16}   {}".format(client['ip'], client['mac']))