#!/usr/bin/python3
from colorama import Fore,Back, Style
import os

cmd = ""
while cmd != "exit":
    cmd = input(Fore.GREEN + "{in} :  " + Fore.RESET)
    try:
        print()
        s = eval(cmd)
        if str(type(s)) != "<class '_sitebuiltins.Quitter'>":
            if s or s != None:
                print(Fore.RED + "{out} : " + Fore.RESET,end='')
                print(s)
                print()
        continue
    except:
        try:
            out = os.popen(cmd + " 2> /dev/null").read()
            out = out.strip()
            if out:
            	print(out + "\n")
            else:
            	raise
        except:
            print(Fore.RED + "Sorry ! Command Was Not Found !" + Fore.RESET)
            print()
