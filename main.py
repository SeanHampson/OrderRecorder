#Upgrade data logging to spreadsheet
#Add price to log - calculate price form order and append onto log
#Add time stamp for delivery onto log

import random, os

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
	def __init__(self, name, address, order, number, due):
		self.name         = name
		self.address      = address
		self.order        = order
		self.number       = number
		self.due          = due
		self.order_info   = "Order Ref: %s\nName: %s\nAddress: %s\nOrder: %s\nNumber: %s\nOrder Due: %s\n\n" \
		% (order_ref, self.name, self.address, self.order, self.number, self.due)
		
		print("Order Reference No. is", order_ref)
		log_order(self.order_info)

	def __repr__(self):
		return(self.order_info)

if __name__ == "__main__":
	if len(references) < 1:
		with open("references.txt", "r") as refs:
			if len(refs.read()) > 0:
				for line in refs.readlines():
					references.append(line)
	
	while True:
		command = input("\n>>> ")

		try:
			if command in {"end", "exit", "bye"}:
				print("\nProgram Ended\n")
				break
			elif int(command) > 9999 and int(command) < 100000:
				search_ref(command)

		except ValueError:	
			order_name = input("\nName>>> ")
			if order_name in {"end", "exit", "bye"}:
				print("\nProgram Ended\n")
				break
			
			order_address = input("\nAddress>>> ")
			if order_address in {"end", "exit", "bye"}:
				print("\nProgram Ended\n")
				break
			
			order_ = input("\nOrder>>> ")
			if order_ in {"end", "exit", "bye"}:
				print("\nProgram Ended\n")
				break
			
			order_phone   = input("\nNumber>>> ")
			if order_phone in {"end", "exit", "bye"}:
				print("\nProgram Ended\n")
				break

			order_due   = input("\nOrder Due>>> ")
			if order_due in {"end", "exit", "bye"}:
				print("\nProgram Ended\n")
				break
			
			order_ref = create_ref()
			order_ref = Customer(order_name, order_address, order_, order_phone, order_due)
