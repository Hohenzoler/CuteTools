#Network Device Scanner or N.D.S.
import scapy.all as scapy
import re
import time

format = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
while True:
    range = input("\nPlease enter the range of the ip address (ex 192.168.0.0/24): ")
    if format.search(range):
        break

while True:
    arp_result = scapy.arping(range)
    time.sleep(10)