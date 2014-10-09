#!/usr/bin/python
import subprocess

try:
    subprocess.check_call(["which", "nmap"])
except:
    print("nmap - No such file")

try:
    subprocess.check_call(["which", "unicorn"])
except:
    print("unicornscan - No such file")


