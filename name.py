# coding: cp1251
import os
import re

filelist = os.listdir("./mafiles/")

for line in filelist:
    mafile = open("./mafiles/" + line, "r").read()
    name = re.findall(r'name":"(.*?)"', mafile)
    secret = re.findall(r'd_secret":"(.*?)"', mafile)
    sfile = open(name[0] + ".secret", "w")
    sfile.write(secret[0])