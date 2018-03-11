#!/usr/bin/python3
print("Installer for pmft 0.1")
import sys, os
osc = sys.platform
if (osc == "linux"):
    pwd = os.getcwd()
    os.system("cp " + pwd + "/pmft /usr/bin/pmft")
    os.system("cp -r " + pwd + "/avrdude-linux /usr/bin/avrdude-pmft")
    os.system("chmod +x /usr/bin/pmft")
    os.system("chmod +x /usr/bin/avrdude-pmft/avrdude-pmft")
    print("Installed!")
else:
    print("You aren't using Linux, run the installer for your operating system")

