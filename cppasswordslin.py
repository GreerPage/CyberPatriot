import os
import subprocess
import atexit
import getpass

username = getpass.getuser()

def rootlogin():
    if __name__=='__main__':
        os.system('sudo python3 cppasswordslin.py')
    else:
        try:
            subprocess.call('sudo python3 cp.py'.split())
        except OSError:
            exit()

def usercheck(name):
        users = subprocess.check_output("awk -F: '$NF!~/\/false$/ && $NF!~/\/nologin$/ && $6~/\/home/{print $1}' /etc/passwd",shell=True).decode('utf-8')
        if name in users: return True
        else: return False

def main():
    if __name__ == '__main__':
        os.system('clear')
        if username != 'root':
            print('In order to run this script you need to be root')
            while True:
                exitc = input('Would you like to restart the script as root? [Y/n] ').lower()
                if exitc=='y':
                    atexit.register(rootlogin)
                    exit()
                if exitc=='n':
                    break
                else:
                    continue
    users = subprocess.check_output("awk -F: '$NF!~/\/false$/ && $NF!~/\/nologin$/ && $6~/\/home/{print $1}' /etc/passwd",shell=True).decode('utf-8')

    userlist=(users.split())

    you = input('Your username: ')

    unique = 1

    filecontent = ''

    try:
        userlist.remove(you)
        userlist=sorted(userlist)
        for word in userlist:
            tryname = usercheck(word)
            if tryname==False:
                continue
            if tryname==True:
                password="Cyb3rP4tr10t#" + str(unique)
                toprint = word + ": " + password
                print(toprint)
                os.system("echo {}:{} | /usr/sbin/chpasswd".format(word, password))
                unique=unique+1
                filecontent += toprint + '\n'
        file = open('passwords.txt', 'w')
        file.write(filecontent)
        file.close()
        if __name__=='__main__':
            input('Done')
            exit()
    except ValueError:
        print("Error: username entered is invalid")
        if __name__=='__main__':
            exit()

if __name__=='__main__':
    main()
