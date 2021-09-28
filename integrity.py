import os
import filecmp
import ctypes  # An included library with Python install.   



#bobTheBuilder :)
file_to_check = "DONOTCHEAT.sb3"
web_request = "https://github.com/Imalaia3/IntegrityAC/blob/main/DONOTCHEAT.sb3?raw=true" #Demo


#Download
os.system("cd %TEMP% & mkdir IntegrityAC")
os.system("cd %TEMP%/IntegrityAC && powershell.exe Invoke-WebRequest " + web_request + " -OutFile abd4trzA.iac")


hacking = filecmp.cmp(os.getenv("TEMP") + "\\IntegrityAC\\abd4trzA.iac", file_to_check)
if hacking == False:
	ctypes.windll.user32.MessageBoxW(0, "IntegrityAC Has Determined Your Game Invalid", "IntegrityAC", 0)
	exit()