import tkinter as tk



win = tk.Tk()
win.title("Subnet calculator")
win.geometry("600x400")

left_fr = tk.Frame(win)
left_fr.grid(row=0,column=0)

right_fr = tk.Frame(win)
right_fr.grid(row=0,column=1)

#non tkinter variables for calculation
#ip_lst = ip.split(".")
#subnet_lst = sub_net.split(".")
ip1 = ""
sub1= ""
oct_ip = []
oct_mask = []
network_addr = []
network_addr_real = []
temp1 = ""
num = 0
#tkinter variables for display on screen
ip = tk.StringVar(left_fr)
sub_net = tk.StringVar(left_fr)
real_network_addr = tk.StringVar(left_fr)
useable_bits = tk.IntVar(left_fr)




#converting ip address into binary
def calc_net_addr():
	ip1 = ip.get()
	sub1 = sub_net.get()
	ip_lst = ip1.split(".")
	subnet_lst = sub1.split(".")
	#print(ip)
	#print(sub_net)
	#print(ip_lst)
	#print(subnet_lst)
	for i in ip_lst:
		print(i)
		print(type(i))
		d = int(i)
		c = (f"{d:08b}")
		oct_ip.append(c)
	for i in subnet_lst:
		d = int(i)
		c = (f"{d:08b}")
		oct_mask.append(c)

	#network address calculation
	def network_address(j):
		temp = []
		s = ""
		for i in range(len(oct_ip[j])):
			c = str(int(oct_ip[j][i]) * int(oct_mask[j][i]))
			temp.append(c)
		for i in temp:
			s += i
		network_addr.append(s)
	#iterating through the list and calculating the network address	
	for j in range(len(oct_ip)):
		network_address(j)
	#printing the network address as a string (from list)
	
	#finding number of usable bits in network address
	print(network_addr_real)
	num = 0
	for i in network_addr[::-1]:
		for j in i[::-1]:
			if j == '0':
				num += 1
			elif j == '1':
				break
		if j == '1':
			break		
	#print (num)#number of useable network addresses
	#printing the network address as a string (from list)
	for i in range(len(network_addr)):
		c = network_addr[i]
		d = int(c,2)
		e = str(d)
		network_addr_real.append(e)
	print(network_addr_real)	
	temp1 = ".".join(network_addr_real)
	#print(temp1)
	print(temp1)
	print(num)
	t = 2**num
	useable_bits.set(t) 
	real_network_addr.set(temp1) 


def display():
	lst.insert(tk.END,real_network_addr.get())
	lst.insert(tk.END,useable_bits.get())

#starting the tkinter

tk.Label(left_fr, text="Enter IP" ).grid(row=0, column=0) #entering IP
name_entry = tk.Entry(left_fr,textvariable=ip)
name_entry.grid(row=0,column=1)

tk.Label(left_fr, text="Enter sub net mask" ).grid(row=1, column=0)#entering sub net mask
name_entry = tk.Entry(left_fr,textvariable=sub_net)
name_entry.grid(row=1,column=1)

lst=tk.Listbox(right_fr)
lst.grid(row=0,column=1)

tk.Button(left_fr,text="Submit",command = calc_net_addr).grid(row=10,column=0)
tk.Button(left_fr,text="Display",command = display).grid(row=10,column=1)	

win.mainloop()



