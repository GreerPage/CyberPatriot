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

def after(value, a):
    pos_a = value.rfind(a)
    if pos_a == -1: return ""
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= len(value): return ""
    return value[adjusted_pos_a:]

print('\33]0;CyberPatriot\a', end='', flush=True)

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
    if command =='0':
        if username != 'root':
            print('restarting sript as root...')
            atexit.register(rootlogin)
            exit()
        else:
            print('Error: you are already logged in as root')
            main()
        main()
    if command=='1':
        cppasswordslin.main()
        main()
    if command.startswith('2'):
        commands = command.split()
        check = after(command, ', ')
        if check in ['True', 'admin=True', 'admin = True']:
            newuser = command.replace(check, '')
            newuser = newuser.replace('2', '')
            newuser = newuser.replace(', ', '')
            newuser = newuser.replace(',', '')
            cpnewuser.main(newuser, admin=True)
        else:
            check = after(command, ',')
            if check in ['True', 'admin=True', 'admin = True']:
                newuser = command.replace(check, '')
                newuser = newuser.replace(', ', '')
                newuser = newuser.replace('2', '')
                newuser = newuser.replace(',', '')
                cpnewuser.main(newuser, admin=True)
            else:
                newuser = command.replace('2', '')
                cpnewuser.main(newuser)
        main()
    if command.startswith('3'):
        if command=='3':
            print('Error: no usernames entered')
            main()
        else:
            usernames = command.replace('3 ', '')
            cprmuser.main(usernames)
        main()
    if command=='4':
        fw.main()
        main()
    if command=='5':
        os.system("awk -F: '$NF!~/\/false$/ && $NF!~/\/nologin$/ && $6~/\/home/{print $1}' /etc/passwd")
        main()
    if command=='help':
        print('CyberPatriot help menu')
        print('0: log in as root')
        print('1: change all local user account passwords')
        print('2: add user accounts (2 <username>) if admin (2 <username>, admin=True)')
        print('3: remove user accounts (3 <usernames>)')
        print('4: enable ufw')
        print('5: list all real users')
        main()
    else:
        x = command.isspace()
        if x==True:
            main()
        else:
            print('Error: {}: not a CyberPatriot command'.format(command))
            main()

if __name__=='__main__':
    main()
