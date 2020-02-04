import os

unallowed = ["traceback","error"]

def is_ok(string):
    for i in unallowed:
        if i.lower() in string.lower():
            return False
    return True

def tryToFind(string):
    s = os.popen("file " + string).read()
    f = open("/usr/bin/god_data/repo.txt")
    data = f.readlines()
    f.close()
    for i in data:
        if i.split("=")[0].strip() in s.lower():
            return i.split("=")[1].strip()
    return 404
