from shutil import copyfile
import os

def backup(backup_path, orders_data_path, orders_backup_path, references_data_path, references_backup_path):
	transfer = False
	if not os.path.exists(backup_path):
		
		if os.path.isfile(orders_data_path) and os.path.isfile(references_data_path):
		
			print("\nBackup Folder doesn't exist, creating new folder...")
			os.mkdir(backup_path)
			print("\nTransferring data from order log to backup log...")
			
			copyfile(orders_data_path, orders_backup_path)
			copyfile(references_data_path, references_backup_path)
			transfer = True
		
		else:
			print("\nOne or more files are missing!\n")
	
	else:
		if os.path.isfile(orders_data_path) and os.path.isfile(references_data_path):
			with open(orders_backup_path, "r") as a_log, open(orders_data_path, "r") as b_log:	
				if len(a_log.read()) == 0 or len(a_log.read()) != len(b_log.read()):
					copyfile(orders_data_path, orders_backup_path)
			
			with open(references_backup_path, "r") as c_log, open(references_data_path, "r") as d_log:
					if len(c_log.read()) == 0 or len(c_log.read()) != len(d_log.read()):
						copyfile(references_data_path, references_backup_path)
		transfer = True
	
	if transfer:
		print("\nTransfer Complete! Program ended\n")

if __name__ == "__main__":
	#backup()
