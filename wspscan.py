import subprocess
import pyfiglet
text = pyfiglet.figlet_format("WSPscan")
print (text)
print ("enter your site name >")
i = input()
subprocess.call("ping "+ i ,shell=True)
