#!/usr/bin/env python3

import subprocess

def runxampp():
    subprocess.check_call(['sudo','/opt/lampp/manager-linux-x64.run'])
    subprocess.check_call(['123456'])
def main():
    runxampp()
main()

