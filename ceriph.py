#!/usr/bin/python
import subprocess
import sys
import os


def scanip(line):
    print(('[-] Scanning ' + line.strip('\n')))
    subprocess.call(["unicornscan", "-l test.log ", line.strip('\n')])


def main():
    if len(sys.argv) == 2:
        scanfile = sys.argv[1]
        if not os.path.isfile(scanfile):
            print(('[-] ' + scanfile + ' does not exist'))
            exit(0)
        if not os.access(scanfile, os.R_OK):
            print('[-] Access Denied')
            exit(0)
    else:
        print(('[-] Usage: ' + str(sys.argv[0]) + ' <Scanfile>'))
        return
    try:
        subprocess.check_call(["which", "nmap"])
    except:
        print("nmap - No such file")
        return
    try:
        subprocess.check_call(["which", "unicornscan"])
    except:
        print("unicornscan - No such file")
        return
    subprocess.call(["mkdir", "udir"])
    ip = open(scanfile, 'r')
    for line in ip.readlines():
        scanip(line)


if __name__ == "__main__":
    main()