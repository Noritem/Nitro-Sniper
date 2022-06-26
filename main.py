import re, requests

from colorama import Fore,Style, init
from discord.ext import commands


init()
Sniper = commands.Bot(command_prefix="!", help_command=None, self_bot=True)


import json
with open('config.json') as config_file: data = json.load(config_file)

token = data['token']
dev = data['dev']

import os
cls = lambda: os.system('cls')
cls()

from time import sleep

import datetime

def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time


banner = (f"""{Fore.RED}
                ███╗   ██╗██╗████████╗██████╗  ██████╗     ███████╗███╗   ██╗██╗██████╗ ███████╗██████╗ 
                ████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    ██╔════╝████╗  ██║██║██╔══██╗██╔════╝██╔══██╗
                ██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║    ███████╗██╔██╗ ██║██║██████╔╝█████╗  ██████╔╝
                ██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║    ╚════██║██║╚██╗██║██║██╔═══╝ ██╔══╝  ██╔══██╗
                ██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝    ███████║██║ ╚████║██║██║     ███████╗██║  ██║
                ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝     ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝{Style.RESET_ALL}
                                        {Fore.MAGENTA}Developed by: {dev} {Style.RESET_ALL}
        """) 
print(banner)


#check if token is valid
head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
if src.status_code == 200:
    print(f'{Fore.GREEN}[+] Your Token Is Valid {Style.RESET_ALL}')
    sleep(4)
else:
    print(f'{Fore.RED}[-] Your Token Is Invalid {Style.RESET_ALL}')
    sleep(4)
    exit()



@Sniper.event
async def on_connect():
    cls()
    print(banner)
    print(f'{Fore.GREEN}Sniper Started at {update_time()} {Style.RESET_ALL}')
    print(f'{Fore.GREEN}Sniper Is Ready To Use')




@Sniper.event
async def on_message(message):
    try:
        if 'discord.gift/' in message.content:
            code = re.search("discord.gift/(.*)", message.content).group(1)
            headers = {
                'Authorization': token,
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36 "
            }
            nitro = f"{Fore.MAGENTA}Nitro-Sniper {Fore.RESET}| Code: {Fore.BLUE}{code} {Fore.RESET}| "
            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers)
            if '{"message": "Unknown Gift Code", "code": 10038}' in r.text:
                print(nitro + Fore.RED + "INVALID CODE!")
            elif '{"message": "This gift has been redeemed already.", "code": 50050}' in r.text:
                print(nitro + Fore.YELLOW + "ALREADY REDEEMED!")
            elif 'You are being rate limited' in r.text:
                print(nitro + Fore.RED + "RATE LIMITED!")
            elif 'Access denied' in r.text:
                print(nitro + Fore.RED + "DENIED ACCESS!")
            elif 'subscription_plan' in r.text:
                print(nitro + Fore.GREEN + "REDEEMED!!")
    except AttributeError:
        pass


Sniper.run(token, bot=False)