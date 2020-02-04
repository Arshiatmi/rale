#!/usr/bin/python3

cmd = ""
while cmd != "exit":
    cmd = input("-> ")
    try:
        s = eval(cmd)
        if str(type(s)) != "<class '_sitebuiltins.Quitter'>":
            if s or s != None:
                print(s)
        continue
    except:
        pass
