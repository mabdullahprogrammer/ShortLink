"""
Author: Muhammad Abdulah
Project: ShortLink
Programmed In: Python 3.10.8
Github: https://Muhammad-Abdullah-Programmer

Usage:-
    ● Short a Link:-
            python short_link.py -m short -l https://gihub.com/Muhammad-Abdullah-Programmer/ShortLink
    -+ Output:
            Your URL: https://tinyurl.com/2jbwbwva
    ========================================================================================================
    ● Open a Link:-
            python short_link.py -m open -l https://tinyurl.com/2jbwbwva
    -+ Output:
            Done!
"""

import argparse
import random
import subprocess
import os
import sys



# try to import pythorteners else it will install it

try:
    import pyshorteners
except ImportError:
    print('\033[1;95mInstalling a Package...')
    subprocess.getoutput('pip3 install pyshorteners')

def clear():
    if "win" in os.environ:
        os.system('cls')
    else:
        os.system("clear")

def banner():
    bnr = ["""  
 █████████  █████                          █████    █████        ███             █████     
 ███░░░░░███░░███                          ░░███    ░░███        ░░░             ░░███      
░███    ░░░  ░███████    ██████  ████████  ███████   ░███        ████  ████████   ░███ █████
░░█████████  ░███░░███  ███░░███░░███░░███░░░███░    ░███       ░░███ ░░███░░███  ░███░░███ 
 ░░░░░░░░███ ░███ ░███ ░███ ░███ ░███ ░░░   ░███     ░███        ░███  ░███ ░███  ░██████░  
 ███    ░███ ░███ ░███ ░███ ░███ ░███       ░███ ███ ░███      █ ░███  ░███ ░███  ░███░░███ 
░░█████████  ████ █████░░██████  █████      ░░█████  ███████████ █████ ████ █████ ████ █████
 ░░░░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░        ░░░░░  ░░░░░░░░░░░ ░░░░░ ░░░░ ░░░░░ ░░░░ ░░░░░ 
                                                                                            """,
            r""" 
  _________.__                      __   .____     .__          __     
 /   _____/|  |__    ____ _______ _/  |_ |    |    |__|  ____  |  | __ 
 \_____  \ |  |  \  /  _ \\_  __ \\   __\|    |    |  | /    \ |  |/ / 
 /        \|   Y  \(  <_> )|  | \/ |  |  |    |___ |  ||   |  \|    <  
/_______  /|___|  / \____/ |__|    |__|  |_______ \|__||___|  /|__|_ \ 
        \/      \/                               \/         \/      \/""", """
 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄    ▄ 
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░▌  ▐░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌           ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░▌ ▐░▌ 
▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌               ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌▐░▌  
▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌               ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░▌░▌   
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌               ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░░▌    
 ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀      ▐░▌     ▐░▌               ▐░▌     ▐░▌   ▐░▌ ▐░▌▐░▌░▌   
          ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▌       ▐░▌     ▐░▌               ▐░▌     ▐░▌    ▐░▌▐░▌▐░▌▐░▌  
 ▄▄▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌      ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌▐░▌ ▐░▌ 
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░▌  ▐░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀    ▀ """, """
  
  .d8888b.  888                       888    888      d8b          888      
d88P  Y88b 888                       888    888      Y8P          888      
Y88b.      888                       888    888                   888      
 "Y888b.   88888b.   .d88b.  888d888 888888 888      888 88888b.  888  888 
    "Y88b. 888 "88b d88""88b 888P"   888    888      888 888 "88b 888 .88P 
      "888 888  888 888  888 888     888    888      888 888  888 888888K  
Y88b  d88P 888  888 Y88..88P 888     Y88b.  888      888 888  888 888 "88b 
 "Y8888P"  888  888  "Y88P"  888      "Y888 88888888 888 888  888 888  888 """]
    bnr = random.choice(bnr)
    print("\033[1;95m"+bnr)
    print("""\033[1;97m         
            Author: Muhammad Abdulah
            Project: ShortLink
            Programmed In: Python 3.10.8
            Github: https://Muhammad-Abdullah-Programmer""")

def shorten(link):
    s = pyshorteners.Shortener()
    print("\033[1;96mYour Link: \033[1;94m", end='')
    print(s.tinyurl.short(link), '\033[00m')

def open(link):
    linked = link.replace('http://', '')
    linked = link.replace('https://', '')
    a = subprocess.getoutput(f'ping {linked}')
    if "Ping request could not find" in a:

        print("\033[1;91mSorry Could Not Start The Host. Please Check your Internet Connection or The URL you typed\033[00m")
    else:
        os.system(f'start {link}')
        print("\033[1;93mDone!\033[00m")

def main():
    print('\n\033[1;91m1.\033[91mOpen     |       \033[1;91m2.\033[91mShort')
    while True:
        o = int(input("\033[1;90mEnter Option: "))
        if o == 2:
            l = input('\033[1;37mEnter The Link To Shorten:\033[1;95m ')
            shorten(l)
        elif o == 1:
            l = input('\033[1;37mEnter The Link To Open:\033[1;95m ')
            open(l)
        else:
            pass

def Func(args):
    if args.l and "open" in args.m:
        open(args.l)
    elif args.l and "short" in args.m:
        shorten(args.l)
    elif args.m and not args.l:
        print('\033[93mPlease Type The Link \033[31m(-l)\033[00m')
    else:
        main()

if __name__ == '__main__':
    clear()
    banner()
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--m', type=str, help="Tells the mode 's:Start' or 'o:Open' to the Program.")
    parser.add_argument('-l', '--l', type=str, help="Type Your Link Here.")
    args = parser.parse_args()
    sys.stdout.write(str(Func(args)))
