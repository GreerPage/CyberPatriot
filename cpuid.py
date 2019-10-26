import os
import subprocess
import getpass
import atexit

username = getpass.getuser()


def main(username1):
    os.system(f'id -u {username1}')

if __name__ == '__main__':
    main(username)
