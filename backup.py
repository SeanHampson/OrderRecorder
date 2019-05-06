from shutil import copyfile
import os

name = "***"

#Upgrade to work on any computer
#When code is finished import into main.py and call every runtime

def backup():
	transfer = False
	if not os.path.exists("C:\\Users\\%s\\Documents\\OrderRecorderBU" % name):
		if os.path.isfile("C:\\Users\\%s\\Desktop\\Projects\\Python\\OrderRecorder\\orders.txt" % name) \
		and os.path.isfile("C:\\Users\\%s\\Desktop\\Projects\\Python\\OrderRecorder\\references.txt" % name):
		
			print("\nBackup Folder doesn't exist, creating new folder...")
			os.mkdir("C:\\Users\\%s\\Documents\\OrderRecorderBU" % name)
			
			print("\nTransferring data from order log to backup log...")
			copyfile("C:\\Users\\%s\\Desktop\\Projects\\Python\\OrderRecorder\\orders.txt" % name, 
				"C:\\Users\\%s\\Documents\\OrderRecorderBU\\orders.txt" % name)
			copyfile("C:\\Users\\%s\\Desktop\\Projects\\Python\\OrderRecorder\\references.txt" % name, 
				"C:\\Users\\%s\\Documents\\OrderRecorderBU\\references.txt" % name)
			transfer = True
		else:
			print("\nOne or more files are missing!\n")
	else:
		if os.path.isfile("C:\\Users\\%s\\Desktop\\Projects\\Python\\OrderRecorder\\orders.txt" % name) \
		and os.path.isfile("C:\\Users\\%s\\Desktop\\Projects\\Python\\OrderRecorder\\references.txt" % name):
			with open("C:\\Users\\%s\\Documents\\OrderRecorderBU\\orders.txt" % name, "r") as a_log:
				with open("C:\\Users\\%s\\Desktop\\Projects\\Python\\OrderRecorder\\orders.txt" % name, "r") as b_log:
					if len(a_log.read()) == 0 or len(a_log.read()) != len(b_log.read()):
						copyfile("C:\\Users\\%s\\Desktop\\Projects\\Python\\OrderRecorder\\orders.txt" % name, 
							"C:\\Users\\%s\\Documents\\OrderRecorderBU\\orders.txt" % name)
			with open("C:\\Users\\%s\\Documents\\OrderRecorderBU\\references.txt" % name, "r") as c_log:
				with open("C:\\Users\\%s\\Desktop\\Projects\\Python\\OrderRecorder\\references.txt" % name, "r") as d_log:
					if len(c_log.read()) == 0 or len(c_log.read()) != len(d_log.read()):
						copyfile("C:\\Users\\%s\\Desktop\\Projects\\Python\\OrderRecorder\\references.txt" % name, 
							"C:\\Users\\%s\\Documents\\OrderRecorderBU\\references.txt" % name)
		transfer = True
	if transfer:
		print("\nTransfer Complete! Program ended\n")

if __name__ == "__main__":
	#Debugging purposes
	backup()
