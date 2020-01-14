##The following modules must be imported
import os
import sys
##this is the code to execute
program = "python"
print("Process calling")
arguments = ["called_Process.py"]

##we call the called_Process.py script
os.execvp(program, (program,)+ tuple(arguments))



