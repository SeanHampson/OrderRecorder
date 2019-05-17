from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

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
	
	#else:
		#Gather values from each input and run through main.py
		#Empty fields after

def display_data(file):
	order_listr = open(file, "r")	
	contents    = order_listr.readlines()
	order_listr.close()

	count = 0
	for line in contents:
				
		if count > 9:
			contents.insert(END, "00%i|%s %s"  % (count, "  "*4, line))

		elif count > 99:
			contents.insert(END, "0%i|%s %s"   % (count, "  "*4, line))

		elif count > 999:
			break 
			contents.insert(END, "%i|%s %s"    % (count, "  "*4, line))

		else:
			contents.insert(END, "000%i|%s %s" % (count, "  "*4, line))
		print(count)
		count += 1

	order_listw = open(file, "w")
	contents    = "".join(contents)
	order_listw.write(contents)
	order_listw.close()

###########

		#contents.insert(index, value)

		#f = open("path_to_file", "w")
		#contents = "".join(contents)
		#f.write(contents)
		#f.close()

#============Labels==============
#label_order_id      = Label(root, text="ORDER REF: ")
label_order_name    = Label(root, text="NAME: ")
label_order_address = Label(root, text="ADDRESS: ")
label_order_        = Label(root, text="ORDER: ")
label_order_number  = Label(root, text="CONTACT NO: ")
label_order_due     = Label(root, text="ORDER DUE: ")

#============Inputs==============
#entry_order_id      = Entry(root)
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
#label_order_id.grid(row=0, sticky=W)
label_order_name.grid(row=1, sticky=W)
label_order_address.grid(row=2, sticky=W)
label_order_.grid(row=3, sticky=W)
label_order_number.grid(row=4, sticky=W)
label_order_due.grid(row=5, sticky=W)

#============Inputs==============
#entry_order_id.grid(row=0, column=1)
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
	try: display_data("orders.txt")
	except Exception as e: print(e)
	root.mainloop()