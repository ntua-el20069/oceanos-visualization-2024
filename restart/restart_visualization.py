import subprocess
import time
while True:
	pythonProcess = subprocess.check_output("ps -ef | grep 'App.py'", shell =True).decode()
	pythonProcess = pythonProcess.split('\n')
	print(len(pythonProcess))
	print(type(pythonProcess))
	i = 0
	for process in pythonProcess[0 : ((len(pythonProcess))-1)]:
		print(process)
		if process.find("grep", 0, len(process)) == -1:
			print("This is the process: ", process)
			i +=1
			print(i)
			time.sleep(1)
		if i ==0:
			subprocess.call(['python3', 'App.py'])
			print("process restarted!") 
			time.sleep(1)


