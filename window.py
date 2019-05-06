from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

#Main menu should have option for adding new order + viewing upcoming deliveries
#User friendly interface with entry boxes etc

root = Tk()
root.resizable(width=False, height=False)
root.iconbitmap("icon.ico")
root.title("Order Recorder v1.0")


def exit_program(): 
	if messagebox.askyesno("Exit Program", "Are you sure you want to exit?"):
		root.destroy()

def submit_info():
	if len(entry_order_id.get()) == 0 or len(entry_order_name.get()) == 0 or \
	len(entry_order_address.get()) == 0 or len(entry_order_.get()) == 0 or \
	len(entry_order_number.get()) == 0:
		messagebox.showerror("Invalid Data", "One or more fields are empty!")

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
with open("orders.txt", "r") as log_list:
	line_number = 0
	for line in log_list.readlines():
		if line_number > 9:
			order_list.insert(END, "00%i|%s %s"  % (line_number, "  "*4, line))
		elif line_number > 99:
			order_list.insert(END, "0%i|%s %s"   % (line_number, "  "*4, line))
		elif line_number > 999:
			order_list.insert(END, "%i|%s %s"    % (line_number, "  "*4, line))
		else:
			order_list.insert(END, "000%i|%s %s" % (line_number, "  "*4, line))
		line_number += 1

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

root.mainloop()
