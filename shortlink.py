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

# Required Imports

import argparse
import random
import os
import sys
import time
import requests

try:
    import subprocess
except ImportError:
    os.system('pip3 install subprocess')
try:
    from intents import day, month, year, ver
    from replace import replace
    from colors import lgtclr, no_clr, bg, drkclr
except Exception:
    print(f"File Not Found!")
    print(f"Installing Files...")
    try:
        subprocess.getoutput(
            'sudo apt install https://github.com/Muhammad-Abdullah-Programmer/ShortLink/blob/main/colors.py')
        subprocess.getoutput(
            'sudo apt install https://github.com/Muhammad-Abdullah-Programmer/ShortLink/blob/main/intents.py')
        subprocess.getoutput(
            'sudo apt install https://github.com/Muhammad-Abdullah-Programmer/ShortLink/blob/main/replace.py')
    except Exception:
        print(f"Your OS is not supported please install files manually from github!");quit()
    else:
        print(f'Package Installed Successfully!')
    time.sleep(1)

try:
    import pyshorteners
except ImportError:
    print(f'{lgtclr.bpurple}Installing a Package...')
    subprocess.getoutput('pip3 install pyshorteners')
    print(f'{lgtclr.bpurple}Package Installed Successfully!')

if day >= 22 and month == 7 and year == 23 and ver <= 2.1:
    subprocess.getoutput('git clone https://github.com/Muhammad-Abdullah-Programmer/ShortLink/')
    replace('ver = 2.1', 'ver = 2.4')
elif day >= 30 and month == 12 and year == 23 <= 2.4:
    subprocess.getoutput('git clone https://github.com/Muhammad-Abdullah-Programmer/ShortLink/')
    replace('ver = 2.4', 'ver = 2.6')
elif day >= 24 and month == 1 and year == 24 <= 2.6:
    subprocess.getoutput('git clone https://github.com/Muhammad-Abdullah-Programmer/ShortLink/')
    replace('ver = 2.6', 'ver = 2.8')
elif day >= 22 and month == 7 and year == 24 <= 2.8:
    subprocess.getoutput('git clone https://github.com/Muhammad-Abdullah-Programmer/ShortLink/')
    replace('ver = 2.8', 'ver = 3')
else:
    print("You are up to date.")


def clear():
    clear = subprocess.getoutput("clear")
    if "is not recognized as" in clear:
        os.system("cls")
    else:
        os.system("clear")

clear()


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
    print(f"{lgtclr.bpurple}" + bnr)
    print(f"""{lgtclr.bwhite}         
            Author: {lgtclr.bcyan}Muhammad Abdulah              {lgtclr.bwhite}  Github: {lgtclr.bcyan}https://Muhammad-Abdullah-Programmer
            {lgtclr.bwhite}Project: {lgtclr.bcyan}ShortLink           {lgtclr.bwhite}           Programmed In: {lgtclr.bcyan}Python 3.10.8
            {lgtclr.bwhite}Date: {lgtclr.bcyan}{day}                       {lgtclr.bwhite} Version: {lgtclr.bcyan}{ver}
            """)

sl = ""
def shorten(link):
    exep = False
    try:
        response = requests.get(link)
    except Exception:
        print(f'{lgtclr.bred}No Network Connection or Invalid URL!')
        exep = True
    if exep == False:
        s = pyshorteners.Shortener()
        slink = s.tinyurl.short(link)
        sl = slink
        print(f"{lgtclr.bcyan}Your Link: {lgtclr.bblue}", end='')
        print(slink, f'{no_clr}')
    else:
        pass
    time.sleep(3)

def update():
    if os.name != "nt":
        if day >= 22 or month >= 7 and year == 23 and ver <= 2.1:
            print(f"{lgtclr.byellow}There's a new update from {bg.lgtclr.bblue}{lgtclr.bwhite} {ver} {no_clr}{lgtclr.byellow}to{bg.lgtclr.bblue}{lgtclr.bwhite} 2.4 \033[00m")
            yn = input(f'{lgtclr.bpurple}Do You Want to update?{lgtclr.bwhite}({lgtclr.white}Y{lgtclr.bwhite}/{lgtclr.white}N{lgtclr.bwhite}){lgtclr.bpurple}: {lgtclr.bwhite}')
            if yn.lower() == "y":
                print(f"{lgtclr.bpurple}Updating...")
                subprocess.getoutput('git clone https://github.com/Muhammad-Abdullah-Programmer/ShortLink/')
                replace('ver = 2.1', 'ver = 2.4')
                print(f'{lgtclr.bgreen}Successfully Updated!')
            else:
                main()
        elif day >= 30 or month >= 12 and year == 23 <= 2.4:
            print(
                f"{lgtclr.byellow}There's a new update from {bg.lgtclr.bblue}{lgtclr.bwhite} {ver} {no_clr}{lgtclr.byellow}to{bg.lgtclr.bblue}{lgtclr.bwhite} 2.6 \033[00m")
            yn = input(
                f'{lgtclr.bpurple}Do You Want to update?{lgtclr.bwhite}({lgtclr.white}Y{lgtclr.bwhite}/{lgtclr.white}N{lgtclr.bwhite}){lgtclr.bpurple}: {lgtclr.bwhite}')
            if yn.lower() == "y":
                print(f"{lgtclr.bpurple}Updating...")
                subprocess.getoutput('git clone https://github.com/Muhammad-Abdullah-Programmer/ShortLink/')
                replace('ver = 2.4', 'ver = 2.6')
                print(f'{lgtclr.bgreen}Successfully Updated!')
            else:
                main()
        elif day >= 24 or month >= 1 and year == 24 <= 2.6:
            print(
                f"{lgtclr.byellow}There's a new update from {bg.lgtclr.bblue}{lgtclr.bwhite} {ver} {no_clr}{lgtclr.byellow}to{bg.lgtclr.bblue}{lgtclr.bwhite} 2.8 \033[00m")
            yn = input(
                f'{lgtclr.bpurple}Do You Want to update?{lgtclr.bwhite}({lgtclr.white}Y{lgtclr.bwhite}/{lgtclr.white}N{lgtclr.bwhite}){lgtclr.bpurple}: {lgtclr.bwhite}')
            if yn.lower() == "y":
                print(f"{lgtclr.bpurple}Updating...")
                subprocess.getoutput('git clone https://github.com/Muhammad-Abdullah-Programmer/ShortLink/')
                replace('ver = 2.6', 'ver = 2.8')
                print(f'{lgtclr.bgreen}Successfully Updated!')
            else:
                main()
        elif day >= 22 or month >= 7 and year == 24 <= 2.8:
            print(
                f"{lgtclr.byellow}There's a new update from {bg.lgtclr.bblue}{lgtclr.bwhite} {ver} {no_clr}{lgtclr.byellow}to{bg.lgtclr.bblue}{lgtclr.bwhite} 3 \033[00m")
            yn = input(
                f'{lgtclr.bpurple}Do You Want to update?{lgtclr.bwhite}({lgtclr.white}Y{lgtclr.bwhite}/{lgtclr.white}N{lgtclr.bwhite}){lgtclr.bpurple}: {lgtclr.bwhite}')
            if yn.lower() == "y":
                print(f"{lgtclr.bpurple}Updating...")
                subprocess.getoutput('git clone https://github.com/Muhammad-Abdullah-Programmer/ShortLink/')
                replace('ver = 2.8', 'ver = 3')
                print(f'{lgtclr.bgreen}Successfully Updated!')
            else:
                main()
        else:
            print(f'{lgtclr.bred}No New Updates Available or yo are up to date!\033[00m')

        time.sleep(1)
        main()
    else:
        print(f'{lgtclr.red}Sorry cant Update because your OS is not supported')
    time.sleep(1)

def openlink(link):
    linked = link.replace('http://', '')
    linked = link.replace('https://', '')
    a = subprocess.getoutput(f'ping {linked}')
    if "Ping request could not find" in a:

        print(
            f"{lgtclr.bred}Sorry Could Not Open Link. Please Check your Internet Connection or The URL you typed{no_clr}")
    else:
        if os.name == "nt":
            os.system(f'start {link}')
        else:
            os.system(f'xgd-open {link}')
        print(f"{lgtclr.byellow}Done!{no_clr}")
    time.sleep(1)

def main():
    clear()
    banner()
    print(f'\n')
    try:
        print(f'{lgtclr.bwhite}1.{lgtclr.byellow} Shorten')
        print(f'{lgtclr.bwhite}2.{lgtclr.byellow} Open')
        print(f'{lgtclr.bwhite}3.{lgtclr.byellow} Update')
        print(f'{lgtclr.bwhite}4.{lgtclr.byellow} Show History')
        print()
        o = input(f"{lgtclr.bgreen}Enter Option: {lgtclr.bwhite}")
        print(f"{lgtclr.byellow}")
        if o == '1':
            l = input(f'{drkclr.bwhite}Enter The Link To Shorten:{lgtclr.bpurple} ')
            save_history(f'Link Shortened from: {l} to {sl}')
            shorten(l)
        elif o == '2':
            l = input(f'{drkclr.bwhite}Enter The Link To Open:{lgtclr.bpurple} ')
            openlink(l)
            save_history(f'Link Opened: {l}')
        elif o == '3':
            update()
        elif o == '4':
            show_history()
            input()  # Click any key to continue
        else:
                print(f"{lgtclr.red}Invalid Option!")
                time.sleep(1)
        main()
    except KeyboardInterrupt:
        print(f"\n{lgtclr.bpurple}Thanks For Visiting.\nBye!{no_clr}")
        quit()

def save_history(link):
    with open('link.history', 'a') as f:
        f.write(link)
        f.close()

def show_history():
    with open('link.history', 'r') as f:
        data = f.read()
        f.close()
    print(data)

def Func(args):
    if args.l and args.m == "o":
        banner()
        open(args.l)
    elif args.l and args.m == "s":
        banner()
        shorten(args.l)
    elif args.m == "u":
        banner()
        update()
    elif args.m == "h":
        banner()
        show_history()
    elif args.m and not args.l:
        print(f'\033[93mPlease Type The Link \033[31m(-l){no_clr}')
    else:
        main()


if __name__ == '__main__':
    banner()
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--m', type=str, help="Tells the mode 's:Start' or 'o:Open' to the Program.")
    parser.add_argument('-l', '--l', type=str, help="Type Your Link Here.")
    args = parser.parse_args()
    sys.stdout.write(str(Func(args)))
