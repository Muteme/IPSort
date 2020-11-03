import sys


Filein = sys.argv[1]
Fileout = sys.argv[2]

ip_in = open(Filein)
ip_out = open(Fileout)

#Sort ip's
ip_sorted = sorted(ip_in, key=lambda j: ''.join(('00'+j.split('.')[i])[-3::] for i in range(4)))
print("output saved to "+Fileout)
clean_ips = [item.rstrip() for item in ip_sorted]

#Write to file	
sys.stdout = print(*clean_ips, sep="\n", end="", file=open(sys.argv[2], "w"))
