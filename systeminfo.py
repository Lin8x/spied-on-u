import os
import subprocess
import nmap
import platform

#######################################################
#######################################################
#######################################################

def getMac():

  # def writeCommand(command, filename):
  #     logger = open(filename, 'a+')
  #     startupinfo = subprocess.STARTUPINFO()
  #     startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
  #     command = command.split()
  #     const = ((200 - len(" ".join(command))) // 2)
  #     linestr = "-" * const + " ".join(command) + "-" * const
  #     output = subprocess.Popen(command, startupinfo=startupinfo, stdout=subprocess.PIPE)
  #     logger.write(str(output.stdout.read()).replace("\\r\\n", "\r\n"))
  #     logger.write("\n" + linestr + "\n")

  ####################################
    
  #http://teczd.com/2015/09/23/osx-get-system-info-from-command-line/

  line = "echo ' ----------------------------------------------' "

  #How System Prodfiler Works: system_profiler <app data>
  
  ####################################
  
  #Gets System DataTypes and puts it in dtypelist.log
  os.system("system_profiler -listDataTypes > MacOS/dtypelist.log")
  
  ####################################

  #Gets the Hardware Data and puts it in hardware.log
  #SPSPIDataType
  #SPUSBDataType
  #SPCardReaderDataType
  #SPPowerDataType
  os.system("system_profiler SPSPIDataType > MacOS/hardware.log")

  os.system(line + " >> MacOS/hardware.log")

  os.system("system_profiler SPUSBDataType >> MacOS/hardware.log")

  os.system(line + " >> MacOS/hardware.log")

  os.system("system_profiler SPCardReaderDataType >> MacOS/hardware.log")

  os.system(line + " >> MacOS/hardware.log")

  os.system("system_profiler SPPowerDataType >> MacOS/hardware.log")

  os.system(line + " >> MacOS/hardware.log")

  ####################################

  #Gets System Camera Data and puts it in cam.log
  #SPCameraDataType
  #SPAudioDataType
  #SPHardwareDataType
  #SPHardwareRAIDDataType
  os.system("system_profiler SPCameraDataType > MacOS/cam.log")

  os.system(line + " >> MacOS/cam.log")

  os.system("system_profiler SPAudioDataType >> MacOS/cam.log")

  os.system(line + " >> MacOS/cam.log")
  
  os.system("system_profiler SPHardwareDataType >> MacOS/cam.log")
  
  os.system(line + " >> MacOS/cam.log")

  os.system("system_profiler SPHardwareRAIDDataType >> MacOS/cam.log")

  os.system(line + " >> MacOS/cam.log")
  
  ####################################

  # Gets all the Operating System's Information and puts it in osxinfo.log
  os.system("sw_vers > MacOS/osxinfo.log")
  
  os.system(line + " >> MacOS/osxinfo.log")
  
  os.system("uname -a >>  MacOS/osxinfo.log")

  os.system(line + " >> MacOS/osxinfo.log")

  os.system("ls -l >> MacOS/osxinfo.log")

  ####################################

  #Gets all the Operating System's Software Information and puts it in software.log
  #SPDisplaysDataType
  #SPApplicationsDataType
  #SPUniversalAccessDataType
  #SPConfigurationProfileDataType
  #SPStartupItemDataType
  
  os.system("system_profiler SPDisplaysDataType > MacOS/software.log")

  os.system(line + " >> MacOS/software.log")

  os.system("system_profiler SPApplicationsDataType >> MacOS/software.log")

  os.system(line + " >> MacOS/software.log")

  os.system("system_profiler SPUniversalAccessDataType >> MacOS/software.log")

  os.system(line + " >> MacOS/software.log")

  os.system("system_profiler SPConfigurationProfileDataType >> MacOS/software.log")

  os.system(line + " >> MacOS/software.log")

  os.system("system_profiler SPStartupItemDataType >> MacOS/software.log")

  ####################################

  #Gets all the Operating System's Network Information and puts it in net.log
  #SPBluetoothDataType
  #SPEthernetDataType
  #SPFirewallDataType
  #SPNetworkLocationDataType
  #SPNetworkVolumeDataType
  #SPNetworkDataType
  #SPWWANDataType
  #SPAirPortDataType

  os.system("system_profiler SPBluetoothDataType > MacOS/net.log")

  os.system(line + " >> MacOS/net.log")

  os.system("system_profiler SPEthernetDataType >> MacOS/net.log")

  os.system(line + " >> MacOS/net.log")

  os.system("system_profiler SPFirewallDataType >> MacOS/net.log")

  os.system(line + " >> MacOS/net.log")

  os.system("system_profiler SPNetworkLocationDataType >> MacOS/net.log")
  
  os.system(line + " >> MacOS/net.log")

  os.system("system_profiler SPNetworkVolumeDataType >> MacOS/net.log")
  
  os.system(line + " >> MacOS/net.log")

  os.system("system_profiler SPNetworkDataType >> MacOS/net.log")
  
  os.system(line + " >> MacOS/net.log")

  os.system("system_profiler SPWWANDataType >> MacOS/net.log")

  os.system(line + " >> MacOS/net.log")

  os.system("system_profiler SPAirPortDataType >> MacOS/net.log")
  
  os.system(line + " >> MacOS/net.log")

#######################################################
#######################################################
#######################################################

def getWindows():
  
  def writeCommand(command):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    const = ((200 - len(command)) // 2)
    linestr = "-" * const + command + "-" * const
    output = subprocess.Popen(command, startupinfo=startupinfo, stdout=subprocess.PIPE)
    logger.write(str(output.stdout.read()).replace("\\r\\n", "\r\n"))
    logger.write("\n" + linestr + "\n")

  logger = open("systeminfowin.log", 'a+')
  writeCommand("Systeminfo")
  writeCommand("ipconfig")

#######################################################
#######################################################
#######################################################

def getLinux():

  line = "echo '----------------------------------------------' "

  #os info
  os.system("uname -a > Linux/linux.log")

  os.system(line + " >> Linux/linux.log")

  #internet configuration
  os.system("ifconfig >> Linux/linux.log")

  os.system(line + " >> Linux/linux.log")

  #cpu info
  os.system("lscpu >> Linux/linux.log")

  os.system(line + " >> Linux/linux.log")

  #usb info
  os.system("lsusb -v >> Linux/linux.log")

  os.system(line + " >> Linux/linux.log")

  #tbh I have no idea
  os.system("lsb_release -a >> Linux/linux.log")

#######################################################
#######################################################
#######################################################

def nmap():
  nm = nmap.PortScanner()
  ip = socket.gethostbyname(socket.gethostname()
  nmap.scan(ip ,'22-443')

#######################################################
#######################################################
#######################################################import os
import subprocess
import nmap
import platform

#######################################################
#######################################################
#######################################################

def getMac():

  # def writeCommand(command, filename):
  #     logger = open(filename, 'a+')
  #     startupinfo = subprocess.STARTUPINFO()
  #     startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
  #     command = command.split()
  #     const = ((200 - len(" ".join(command))) // 2)
  #     linestr = "-" * const + " ".join(command) + "-" * const
  #     output = subprocess.Popen(command, startupinfo=startupinfo, stdout=subprocess.PIPE)
  #     logger.write(str(output.stdout.read()).replace("\\r\\n", "\r\n"))
  #     logger.write("\n" + linestr + "\n")

  ####################################
    
  #http://teczd.com/2015/09/23/osx-get-system-info-from-command-line/

  line = "echo ' ----------------------------------------------' "

  #How System Prodfiler Works: system_profiler <app data>
  
  ####################################
  
  #Gets System DataTypes and puts it in dtypelist.log
  os.system("system_profiler -listDataTypes > MacOS/dtypelist.log")
  
  ####################################

  #Gets the Hardware Data and puts it in hardware.log
  #SPSPIDataType
  #SPUSBDataType
  #SPCardReaderDataType
  #SPPowerDataType
  os.system("system_profiler SPSPIDataType > MacOS/hardware.log")

  os.system(line + " >> MacOS/hardware.log")

  os.system("system_profiler SPUSBDataType >> MacOS/hardware.log")

  os.system(line + " >> MacOS/hardware.log")

  os.system("system_profiler SPCardReaderDataType >> MacOS/hardware.log")

  os.system(line + " >> MacOS/hardware.log")

  os.system("system_profiler SPPowerDataType >> MacOS/hardware.log")

  os.system(line + " >> MacOS/hardware.log")

  ####################################

  #Gets System Camera Data and puts it in cam.log
  #SPCameraDataType
  #SPAudioDataType
  #SPHardwareDataType
  #SPHardwareRAIDDataType
  os.system("system_profiler SPCameraDataType > MacOS/cam.log")

  os.system(line + " >> MacOS/cam.log")

  os.system("system_profiler SPAudioDataType >> MacOS/cam.log")

  os.system(line + " >> MacOS/cam.log")
  
  os.system("system_profiler SPHardwareDataType >> MacOS/cam.log")
  
  os.system(line + " >> MacOS/cam.log")

  os.system("system_profiler SPHardwareRAIDDataType >> MacOS/cam.log")

  os.system(line + " >> MacOS/cam.log")
  
  ####################################

  # Gets all the Operating System's Information and puts it in osxinfo.log
  os.system("sw_vers > MacOS/osxinfo.log")
  
  os.system(line + " >> MacOS/osxinfo.log")
  
  os.system("uname -a >>  MacOS/osxinfo.log")

  os.system(line + " >> MacOS/osxinfo.log")

  os.system("ls -l >> MacOS/osxinfo.log")

  ####################################

  #Gets all the Operating System's Software Information and puts it in software.log
  #SPDisplaysDataType
  #SPApplicationsDataType
  #SPUniversalAccessDataType
  #SPConfigurationProfileDataType
  #SPStartupItemDataType
  
  os.system("system_profiler SPDisplaysDataType > MacOS/software.log")

  os.system(line + " >> MacOS/software.log")

  os.system("system_profiler SPApplicationsDataType >> MacOS/software.log")

  os.system(line + " >> MacOS/software.log")

  os.system("system_profiler SPUniversalAccessDataType >> MacOS/software.log")

  os.system(line + " >> MacOS/software.log")

  os.system("system_profiler SPConfigurationProfileDataType >> MacOS/software.log")

  os.system(line + " >> MacOS/software.log")

  os.system("system_profiler SPStartupItemDataType >> MacOS/software.log")

  ####################################

  #Gets all the Operating System's Network Information and puts it in net.log
  #SPBluetoothDataType
  #SPEthernetDataType
  #SPFirewallDataType
  #SPNetworkLocationDataType
  #SPNetworkVolumeDataType
  #SPNetworkDataType
  #SPWWANDataType
  #SPAirPortDataType

  os.system("system_profiler SPBluetoothDataType > MacOS/net.log")

  os.system(line + " >> MacOS/net.log")

  os.system("system_profiler SPEthernetDataType >> MacOS/net.log")

  os.system(line + " >> MacOS/net.log")

  os.system("system_profiler SPFirewallDataType >> MacOS/net.log")

  os.system(line + " >> MacOS/net.log")

  os.system("system_profiler SPNetworkLocationDataType >> MacOS/net.log")
  
  os.system(line + " >> MacOS/net.log")

  os.system("system_profiler SPNetworkVolumeDataType >> MacOS/net.log")
  
  os.system(line + " >> MacOS/net.log")

  os.system("system_profiler SPNetworkDataType >> MacOS/net.log")
  
  os.system(line + " >> MacOS/net.log")

  os.system("system_profiler SPWWANDataType >> MacOS/net.log")

  os.system(line + " >> MacOS/net.log")

  os.system("system_profiler SPAirPortDataType >> MacOS/net.log")
  
  os.system(line + " >> MacOS/net.log")

#######################################################
#######################################################
#######################################################

def getWindows():
  
  def writeCommand(command):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    const = ((200 - len(command)) // 2)
    linestr = "-" * const + command + "-" * const
    output = subprocess.Popen(command, startupinfo=startupinfo, stdout=subprocess.PIPE)
    logger.write(str(output.stdout.read()).replace("\\r\\n", "\r\n"))
    logger.write("\n" + linestr + "\n")

  logger = open("systeminfowin.log", 'a+')
  writeCommand("Systeminfo")
  writeCommand("ipconfig")

#######################################################
#######################################################
#######################################################

def getLinux():

  line = "echo '----------------------------------------------' "

  #os info
  os.system("uname -a > Linux/linux.log")

  os.system(line + " >> Linux/linux.log")

  #internet configuration
  os.system("ifconfig >> Linux/linux.log")

  os.system(line + " >> Linux/linux.log")

  #cpu info
  os.system("lscpu >> Linux/linux.log")

  os.system(line + " >> Linux/linux.log")

  #usb info
  os.system("lsusb -v >> Linux/linux.log")

  os.system(line + " >> Linux/linux.log")

  #tbh I have no idea
  os.system("lsb_release -a >> Linux/linux.log")

#######################################################
#######################################################
#######################################################

def nmap():
  nm = nmap.PortScanner()
  ip = socket.gethostbyname(socket.gethostname()
  nmap.scan(ip ,'22-443')

#######################################################
#######################################################
#######################################################