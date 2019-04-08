import os
import subprocess
import getpass
import atexit

username = getpass.getuser()

def rootlogin():
    if __name__=='__main__':
        os.system('sudo python3 fw.py')
    else:
        try:
            subprocess.call('sudo python3 cp.py'.split())
        except OSError:
            exit()
def main():
    if __name__ == '__main__':
        os.system('clear')
    if __name__=='__main__':
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
    os.system('sudo ufw enable')

if __name__ == '__main__':
    main('test1 test2')
