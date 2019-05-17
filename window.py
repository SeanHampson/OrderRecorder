from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import random, os

root = Tk()                               #Creating tkinter instance
root.resizable(width=False, height=False) #Setting window to a fixed size
root.iconbitmap("icon.ico")               #Setting icon of application window
root.title("Order Recorder v1.0")         #Title of application


def exit_program():
	#Verifies with user if they wish to exit
	if messagebox.askyesno("Exit Program", "Are you sure you want to exit?"):
		root.destroy() #Closes application

def submit_info():
	#If statement to check whether 1 or more fields are empty: if so then notify user
	if len(entry_order_due.get()) == 0 or len(entry_order_name.get()) == 0 or \
	len(entry_order_address.get()) == 0 or len(entry_order_.get()) == 0 or \
	len(entry_order_number.get()) == 0:
		#Notifies user that 1 or more fields are empty
		messagebox.showerror("Invalid Data", "One or more fields are empty!")
	
	else:
		order_name    = entry_order_name.get()
		order_address = entry_order_address.get()
		order_        = entry_order_.get()
		order_phone   = entry_order_number.get()
		order_due     = entry_order_due.get()

		order_ref     = create_ref()
		order_ref     = Customer(order_ref, order_name, order_address, order_, order_phone, order_due)

		entry_order_name.delete(0, END)
		entry_order_address.delete(0, END)
		entry_order_.delete(0, END)
		entry_order_number.delete(0, END)
		entry_order_due.delete(0, END)

		try: display_data("orders.txt")
		except Exception as e: print(e)

def display_data(file):
	order_listr = open(file, "r")	      #Opens order file to read data
	contents    = order_listr.readlines() #Added data to list for iteration
	order_listr.close()
	
	count = 0
	for line in contents:
		#Insert data to list element on application 			
		if count > 9:
			order_list.insert(END, "00%i|%s %s"  % (count, "  "*4, line))

		elif count > 99:
			order_list.insert(END, "0%i|%s %s"   % (count, "  "*4, line))

		elif count > 999:
			order_list.insert(END, "%i|%s %s"    % (count, "  "*4, line))

		else:
			order_list.insert(END, "000%i|%s %s" % (count, "  "*4, line))
		count += 1
##################################
references = []
def print_ref(index):
	with open("orders.txt", "r") as r_order:
		lines = r_order.readlines()
		for x in range(1, 6):
			print("\n%s"   % (lines[x]))

def search_ref(ref_query):
	num = 0
	with open("references.txt", "r") as ref:
		for line in ref.readlines():
			if ref_query + "\n" == line:
				with open("orders.txt", "r") as r_order:
					for line in r_order.readlines():
						if "Order Ref: " + ref_query + "\n" == line:
							print_ref(num)
							break
						num += 1
					break
			else:
				print("\nNo References Available!")
				break


def log_order(order_info):
	with open("orders.txt", "a") as log:
		log.write(order_info)
		print("\nLog file updated")

def create_ref():
	ref = random.randint(10000, 99999)
	with open("references.txt", "r") as ref_log:
		for line in ref_log.readlines():
			if line == ref:
				ref = random.randint(10000, 99999)
	references.append(ref)
	with open("references.txt", "a+") as ref_add:
		ref_add.write(str(ref) + "\n")
	return(ref)

class Customer(object):
	def __init__(self, ref, name, address, order, number, due):
		self.ref        = ref
		self.name       = name
		self.address    = address
		self.order      = order
		self.number     = number
		self.due        = due
		self.order_info = "Order Ref: %s\nName: %s\nAddress: %s\nOrder: %s\nNumber: %s\nOrder Due: %s\n\n" \
		% (self.ref, self.name, self.address, self.order, self.number, self.due)
		
		print("Order Reference No. is", self.ref)
		log_order(self.order_info)

	def __repr__(self):
		return(self.order_info)

##################################
#============Labels==============
label_order_name    = Label(root, text="NAME: ")
label_order_address = Label(root, text="ADDRESS: ")
label_order_        = Label(root, text="ORDER: ")
label_order_number  = Label(root, text="CONTACT NO: ")
label_order_due     = Label(root, text="ORDER DUE: ")

#============Inputs==============
entry_order_name    = Entry(root)
entry_order_address = Entry(root)
entry_order_        = Entry(root)
entry_order_number  = Entry(root)
entry_order_due     = Entry(root)

search_order        = Entry(root)

#============Buttons=============
submit = Button(root, text="SUBMIT", command=submit_info)
exit   = Button(root, text="EXIT",   command=exit_program)

search = Button(root, text="SEARCH")

#============Lists===============
order_list = Listbox(root, height=10, width=50, relief=GROOVE, bd=4)
scrollbar  = Scrollbar(root)

#============Labels==============
label_order_name.grid(row=1, sticky=W)
label_order_address.grid(row=2, sticky=W)
label_order_.grid(row=3, sticky=W)
label_order_number.grid(row=4, sticky=W)
label_order_due.grid(row=5, sticky=W)

#============Inputs==============
entry_order_name.grid(row=1, column=1)
entry_order_address.grid(row=2, column=1)
entry_order_.grid(row=3, column=1)
entry_order_number.grid(row=4, column=1)
entry_order_due.grid(row=5, column=1)

search_order.grid(row=8, sticky=W)

#============Buttons==============
submit.grid(row=6, column=2, sticky=W)
exit.grid(row=6, sticky=W)

search.grid(row=8, column=1 , sticky=W)

#============Lists================
order_list.grid(row=7, columnspan=3, sticky=W)
scrollbar.grid(row=7, column=3, sticky=N+S+W)

order_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=order_list.yview)

if __name__ == "__main__":
	if len(references) < 1:
		with open("references.txt", "r") as refs:
			if len(refs.read()) > 0:
				for line in refs.readlines():
					references.append(line)
	##########################################
	try: display_data("orders.txt")
	except Exception as e: print(e)
	root.mainloop()