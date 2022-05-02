from cmath import inf
import time
import os
import sys
import colorama
from termcolor import colored
from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style
init(convert=True)
import platform
import random
import string
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("BITFINDER - STATUS: LOADING...")

def clear():
  
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')



welcome = (colored('[.] Launching Server Firmware v1.0.0...', 'red'))
os.system('cls' or 'clear')
for char in welcome:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(1)

clear()
print("")
time.sleep(0.03)
print("")
time.sleep(0.03)
ctypes.windll.kernel32.SetConsoleTitleW("BITFINDER - STATUS: ACTIVE")
print(colored("██████╗██████████████████████╗   ████████╗█████████████╗","red"))
time.sleep(0.03)
print(colored("██╔══████╚══██╔══██╔════██████╗  ████╔══████╔════██╔══██╗","red"))
time.sleep(0.03)
print(colored("██████╔██║  ██║  █████╗ ████╔██╗ ████║  ███████╗ ██████╔╝","red"))
time.sleep(0.03)
print(colored("██╔══████║  ██║  ██╔══╝ ████║╚██╗████║  ████╔══╝ ██╔══██╗","red"))
time.sleep(0.03)
print(colored("██████╔██║  ██║  ██║    ████║ ╚██████████╔█████████║  ██║","red"))
time.sleep(0.03)
print(colored("╚═════╝╚═╝  ╚═╝  ╚═╝    ╚═╚═╝  ╚═══╚═════╝╚══════╚═╝  ╚═╝","red"))
time.sleep(0.03)
print("")
time.sleep(0.03)
print("")
time.sleep(0.5)

threads = print(Fore.RED + "[+] threads set to infinite")
print("")
time.sleep(1.3)
time.sleep(1.3)
print(Fore.LIGHTMAGENTA_EX + "[.] checking server...")
print("")
time.sleep(1.0)
print(Fore.LIGHTMAGENTA_EX + "[+] connected to france ")
print("")
time.sleep(0.5)

start = Fore.LIGHTMAGENTA_EX + "[.] starting..."
for char in start:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

print("")
print("")

ctypes.windll.kernel32.SetConsoleTitleW("BITFINDER VERSION 1.0.0 - STATUS: SEARCHING")

def get_random_string(length):
    letters = string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    print(Fore.WHITE + "[" + Fore.RED + "BITFINDER" + Fore.WHITE + "]" + "  TESTING WALLET: " + Fore.LIGHTRED_EX + result_str + Fore.WHITE + "  [" + "RESULT: " + Fore.RED + "0.00 BTC" + Fore.WHITE + "]")


for i in range(100000000000):
    get_random_string(35)
    time.sleep(0.02)
    


def get_random_win(length):
    letters = string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    print(Fore.WHITE + "[" + Fore.RED + "BITFINDER" + Fore.WHITE + "]" + "  TESTING WALLET: " + Fore.LIGHTGREEN_EX + result_str + Fore.WHITE + "  [" + "RESULT: " + Fore.GREEN + "0.00003 BTC" + Fore.WHITE + "]")

time.sleep(0.3)

get_random_win(35)

time.sleep(0.5)

ctypes.windll.kernel32.SetConsoleTitleW("BITFINDER 1.0.0 - STATUS: FOUND BTC!")

print("")
print("")
time.sleep(1)
print(Fore.WHITE + "[" + Fore.RED + "BITFINDER" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + " SAVING '0.00003 BTC' TO WALLET.TXT" + Fore.WHITE + "  [" + "RESULT: " + Fore.GREEN + "SUCCESS" + Fore.WHITE + "]") 
with open("Wallet.txt", "w") as text_file:
    text_file.write("[+] FOUND WALLET: M97FAYBQ1ME3V5L2433G3B343IAIZN18TLS")
time.sleep(1)
print("")
print(Fore.RED + "[.] closing...")
time.sleep(1)

time.sleep(2)
print(Fore.RESET)