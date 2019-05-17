from shutil import copyfile
import os

cpu_name = "ohams_000" #computer's id path
def_path = "C:\\Users\\%s\\" % cpu_name #default computer path
backup_path = ""

#Upgrade to work on any computer
#When code is finished import into main.py and call every runtime

def backup():
	transfer = False
	if not os.path.exists("%sDocuments\\OrderRecorderBU" % def_path):
		if os.path.isfile("%sDesktop\\Projects\\Python\\OrderRecorder\\orders.txt" % def_path) \
		and os.path.isfile("%sDesktop\\Projects\\Python\\OrderRecorder\\references.txt" % def_path):
		
			print("\nBackup Folder doesn't exist, creating new folder...")
			os.mkdir("%sDocuments\\OrderRecorderBU" % def_path)
			
			print("\nTransferring data from order log to backup log...")
			copyfile("%sDesktop\\Projects\\Python\\OrderRecorder\\orders.txt" % def_path, 
				"%sDocuments\\OrderRecorderBU\\orders.txt" % def_path)
			copyfile("%sDesktop\\Projects\\Python\\OrderRecorder\\references.txt" % def_path, 
				"%sDocuments\\OrderRecorderBU\\references.txt" % def_path)
			transfer = True
		else:
			print("\nOne or more files are missing!\n")
	else:
		if os.path.isfile("%sDesktop\\Projects\\Python\\OrderRecorder\\orders.txt" % def_path) \
		and os.path.isfile("%sDesktop\\Projects\\Python\\OrderRecorder\\references.txt" % def_path):
			with open("%sDocuments\\OrderRecorderBU\\orders.txt" % def_path, "r") as a_log:
				with open("%sDesktop\\Projects\\Python\\OrderRecorder\\orders.txt" % def_path, "r") as b_log:
					if len(a_log.read()) == 0 or len(a_log.read()) != len(b_log.read()):
						copyfile("%sDesktop\\Projects\\Python\\OrderRecorder\\orders.txt" % def_path, 
							"sDocuments\\OrderRecorderBU\\orders.txt" % def_path)
			with open("%sDocuments\\OrderRecorderBU\\references.txt" % def_path, "r") as c_log:
				with open("%sDesktop\\Projects\\Python\\OrderRecorder\\references.txt" % def_path, "r") as d_log:
					if len(c_log.read()) == 0 or len(c_log.read()) != len(d_log.read()):
						copyfile("%sDesktop\\Projects\\Python\\OrderRecorder\\references.txt" % def_path, 
							"%sDocuments\\OrderRecorderBU\\references.txt" % def_path)
		transfer = True
	if transfer:
		print("\nTransfer Complete! Program ended\n")

if __name__ == "__main__":
	#Debugging purposes
	backup()
