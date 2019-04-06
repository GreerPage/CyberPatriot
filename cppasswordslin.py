import os
import sys
import subprocess
import re
        
users = subprocess.check_output('ls /home',shell=True).decode('utf-8')

userlist=(users.split())

you = input('Your username: ')

unique = 1

index = 0

userlist.remove(you)

userlist=sorted(userlist)

for word in userlist:
    password="Cyb3rP4tr10t#" + str(unique)
    print(word + ": " + password)
    os.system("echo {}:{} | /usr/sbin/chpasswd".format(word, password))
    unique=unique+1

input('Done')

