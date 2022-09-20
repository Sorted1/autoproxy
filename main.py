#######################################
             discord.gg/sns
#######################################


import requests
import os


ip = input("Server IP: ")
port = input("CNC Port: ")


os.system(f"sysctl -w net.ipv4.ip_forward=1")
os.system(f"iptables -A FORWARD -i eth0 -j ACCEPT")
os.system(f"iptables -A FORWARD -o eth0 -j ACCEPT")
os.system(f"iptables -I FORWARD -i eth0 -p tcp --dport {port} -j ACCEPT"),
os.system(f"iptables -t nat -A PREROUTING -p tcp --dport {port} -j DNAT --to-destination {ip}:{port}")
os.system(f"iptables -t nat -A POSTROUTING -j MASQUERADE")

r = requsts.get(f"https://ipv4.icanhazip.com/")
res = r.json()

print(f"Connect To Your Server With {res.text} On Port {port} | Made BY Sorted")
