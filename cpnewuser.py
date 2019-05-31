import os
import subprocess
import getpass
import atexit

username = getpass.getuser()

def rootlogin():
    if __name__=='__main__':
        os.system('sudo python3 cpnewuser.py')
    else:
        try:
            subprocess.call('sudo python3 cp.py'.split())
        except OSError:
            exit()

def usercheck(name):
        users = subprocess.check_output("awk -F: '$NF!~/\/false$/ && $NF!~/\/nologin$/ && $6~/\/home/{print $1}' /etc/passwd",shell=True).decode('utf-8')
        if name in users: return True
        else: return False

def main(usernames, admin=False):
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
                if admin in [True, False]:
                    os.system('useradd {}'.format(user))
                    if admin == True:
                        os.system('usermod -aG sudo {}'.format(user))
                        print('added admin user: {}'.format(user))
                    if admin==False:
                        print('added user: {}'.format(user))
                else:
                    print('Error: {}: invalid value for admin'.format(admin))
            if tryname==True:
                print('{}: user already exists'.format(user))
                continue
