ip = input("Enter the ip address   ")
sub_net = input("Enter the subnet mask   ")
ip_lst = ip.split(".")
subnet_lst = sub_net.split(".")
oct_ip = []
oct_mask = []
network_addr = []
network_addr_real = []
real_network_addr = ""
r = 0
print(f"The entered IP address is {ip}")
print(f"The entered subnet mask is {sub_net}")

for i in ip_lst:
	d = int(i)
	c = (f"{d:08b}")
	oct_ip.append(c)
for i in subnet_lst:
	d = int(i)
	c = (f"{d:08b}")
	oct_mask.append(c)

def network_address(j):
	temp = []
	s = ""
	for i in range(len(oct_ip[j])):
		c = str(int(oct_ip[j][i]) * int(oct_mask[j][i]))
		temp.append(c)
	for i in temp:
		s += i
	network_addr.append(s)
	

for j in range(len(oct_ip)):
	network_address(j)
print(network_addr)

for i in network_addr[::-1]:
	for j in i[::-1]:
		if j == '0':
			r += 1
		elif j == '1':
			break
	if j == '1':
		break		
	
print (r)

for i in range(len(network_addr)):
	c = network_addr[i]
	d = int(c,2)
	e = str(d)
	network_addr_real.append(e)
real_network_addr = ".".join(network_addr_real)
print(real_network_addr)

