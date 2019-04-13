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
    try:
        tryname = subprocess.check_output('getent passwd {}'.format(name), shell=True)
        return True
    except OSError:
        return False
    except subprocess.CalledProcessError:
        return False

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

    try:
        userlist.remove(you)
    except ValueError:
        print("username entered is invalid! exiting...")
        if __name__=='__main__':
            exit()

    userlist=sorted(userlist)

    for word in userlist:
        tryname = usercheck(word)
        if tryname==False:
            continue
        if tryname==True:
            password="Cyb3rP4tr10t#" + str(unique)
            print(word + ": " + password)
            os.system("echo {}:{} | /usr/sbin/chpasswd".format(word, password))
            unique=unique+1

    input('Done')
    if __name__=='__main__':
        exit()

if __name__=='__main__':
    main()
