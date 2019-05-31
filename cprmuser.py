import os
import subprocess
import getpass
import atexit

username = getpass.getuser()

def rootlogin():
    if __name__=='__main__':
        os.system('sudo python3 cprmuser.py')
    else:
        try:
            subprocess.call('sudo python3 cp.py'.split())
        except OSError:
            exit()

def usercheck(name):
        users = subprocess.check_output("awk -F: '$NF!~/\/false$/ && $NF!~/\/nologin$/ && $6~/\/home/{print $1}' /etc/passwd",shell=True).decode('utf-8')
        if name in users: return True
        else: return False

def main(usernames):
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
    usernames = usernames.split()
    for user in usernames:
        tryname = usercheck(user)
        if tryname==False:
            print('{}: user does not exist'.format(user))
            continue
        if tryname==True:
            os.system('userdel {}'.format(user))
            print('removed user: {}'.format(user))
            continue
