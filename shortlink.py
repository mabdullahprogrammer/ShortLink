"""
Author: Muhammad Abdulah
Project: ShortLink
Programmed In: Python 3.10.8
Github: https://github.com/mabdullahprogrammer

Usage:-
    ● Short a Link:-
            python short_link.py -m short -l https://gihub.com/github.com/mabdullahprogrammer/ShortLink
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
import json
import random
import os
import sys
import time
import datetime

day = int(datetime.datetime.now().strftime("%d"))
month = int(datetime.datetime.now().strftime("%m"))
year = int(datetime.datetime.now().strftime("%y"))

with open('config.json', 'r') as file:
    # Load the JSON content
    data = json.load(file)

ver = data['version']


def verify_pkgs():
    files = os.listdir()
    if 'colors.py' not in files:
        print(f'Config file not installed!')
        with open('config.json', 'w') as colf:
            data = requests.get(
                'https://raw.githubusercontent.com/mabdullahprogrammer/ShortLink/refs/heads/main/config.json').content
            colf.write(data)
    if 'colors.py' not in files:
        print(f'Colors file not installed!')
        with open('colors.py', 'w') as colf:
            data = requests.get(
                'https://raw.githubusercontent.com/mabdullahprogrammer/ShortLink/refs/heads/main/colors.py').content
            colf.write(data)
    if 'replace.py' not in files:
        print(f'Colors file not installed!')
        with open('replace.py', 'w') as colf:
            data = requests.get(
                'https://raw.githubusercontent.com/mabdullahprogrammer/ShortLink/refs/heads/main/replace.py').content
            colf.write(data)

    try:
        import pyshorteners
    except ImportError:
        print('\033[0;92mA necessary Package is not installed. Wait while installing it...\033[1;91m', end='')
        os.system('pip install pyshorteners')
        print('Done')

def check_conn():
    try:
        requests.get('https://google.com')
    except:
        print('\033[1;31mNo Internet!\033[00m');exit()
        
check_conn()
verify_pkgs()

from colors import *
from replace import *
import pyshorteners





os_name = "windows" if 'nt' in os.name else os.name
def clear():
    if os_name == 'windows':
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
            Author: {lgtclr.bcyan}Muhammad Abdulah              {lgtclr.bwhite}  Github: {lgtclr.bcyan}https://github.com/mabdullahprogrammer
            {lgtclr.bwhite}Project: {lgtclr.bcyan}ShortLink           {lgtclr.bwhite}           Programmed In: {lgtclr.bcyan}Python 3.10.8
            {lgtclr.bwhite}Date: {lgtclr.bcyan}{day}                                {lgtclr.bwhite} Version: {lgtclr.bcyan}{ver}
            """)

sl = ""
def shorten(link):
    exep = False
    try:
        response = requests.get(link)
    except ConnectionError:
        print(f'{lgtclr.bred}No Network Connection')
        exep = True
    except requests.exceptions.MissingSchema or requests.exceptions.InvalidURL or requests.exceptions.InvalidSchema:
        print(f'{lgtclr.bred}Invalid URL')
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

import os
import requests
import zipfile
import io


def clone(username, repo_name, destination=None):
    # Construct the URL for the zip file of the repository
    repo_url = f"https://github.com/{username}/{repo_name}/archive/refs/heads/main.zip"

    if destination is None:
        destination = repo_name  # Default destination folder as repo_name

    try:
        print(f"Downloading {repo_url} ...")
        # Send a GET request to download the repository as a zip file
        response = requests.get(repo_url)

        if response.status_code == 200:
            print("Download successful, extracting...")
            # Extract the downloaded zip file to the destination
            with zipfile.ZipFile(io.BytesIO(response.content)) as z:
                z.extractall(destination)
            print(f"Repository cloned to '{destination}'")
        else:
            print(f"Failed to download repository: HTTP {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")


def update():
    data = requests.get('https://raw.githubusercontent.com/mabdullahprogrammer/ShortLink/refs/heads/main/config.json')
    data = data.json()
    new_ver = data['version']
    if data['update'] and ver!=new_ver:
        print(f"{lgtclr.byellow}There's a new update from {bg.lgtclr.bblue}{lgtclr.bwhite} {ver} {no_clr}{lgtclr.byellow}to{bg.lgtclr.bblue}{lgtclr.bwhite} {new_ver} \033[00m")
        yn = input(f'{lgtclr.bpurple}Do You Want to update?{lgtclr.bwhite}({lgtclr.white}Y{lgtclr.bwhite}/{lgtclr.white}N{lgtclr.bwhite}){lgtclr.bpurple}: {lgtclr.bwhite}')
        if yn.lower() == "y":
            print(f"{lgtclr.bpurple}Updating...")
            cwd = os.getcwd()
            pwd = cwd.split('\\')
            pwd.pop(-1)
            pwd = '\\'.join(pwd)
            clone('mabdullahprogrammer', 'ShortLink',f'{pwd}')
            print(f'{lgtclr.bgreen}Successfully Updated!')
            print(f'{lgtclr.yellow}Run the script again to apply updates. \n{lgtclr.bwhite}Also Remove Old Directory and rename Shortlink-main to ShortLink')
            exit()
        else:
            main()
    else:
        print(f'{lgtclr.bred}No New Updates Available or yo are up to date!\033[00m')

    time.sleep(1)
    main()

def openlink(link):
    linked = link.replace('http://', '')
    linked = link.replace('https://', '')
    a = os.system(f'ping {linked}')
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
        f.write(link+"\n")
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
