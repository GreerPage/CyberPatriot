import cppasswordslin
import fw
import os
import subprocess
import cprmuser
import cpnewuser
import getpass
import atexit
import readline
import rlcompleter

username = getpass.getuser()

class bcolors:
    purple = u'\033[95m'
    blue = u'\u001b[34m'
    green = u'\033[92m'
    yellow = u'\033[93m'
    red = u'\033[91m'
    cyan = u'\033[96m'
    white = u'\033[97m'
    grey = u'\033[90m'
    end = u'\033[0m'
    bold = u'\033[1m'
    underline = u'\033[4m'


def rootlogin():
        os.system('sudo python3 cp.py')

if username != 'root':
    os.system('clear')
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
else:
    os.system('clear')

def main():
    print('\33]0;CyberPatriot\a', end='', flush=True)
    if username=='root':
        char = '#'
    else:
        char = '$'
    global command
    print('{}{}cp{}|{}{}{}{}'.format(bcolors.bold, bcolors.blue, bcolors.end, bcolors.bold, bcolors.red, username, bcolors.end), end ='')
    command = input('{} '.format(char))
    if command=='clear':
        os.system('clear')
        main()
    if command in ['q', 'exit']:
        os.system('clear')
        exit()
    if command=='':
        main()
    if command=='1':
        cppasswordslin.main()
        main()
    if command.startswith('2'):
        command = command.split()
        arg1 = command[1]
        arg2 = command[2]
        cpnewuser.main(arg1, arg2)
        main()
    if command=='help':
        print('CyberPatriot help menu')
        print('1: change all local user account passwords')
        print('2: add user accounts (2 <username>) if admin (2 <username> admin=True)')
        print('3: remove user accounts (3 <usernames>)')
        print('4: enable ufw')
        main()
    else:
        x = command.isspace()
        if x==True:
            main()
        else:
            print('')
            print('{}Error: {}: not a CyberPatriot command{}'.format(bcolors.bold, command, bcolors.end))
            print('')
            main()

if __name__=='__main__':
    main()
