#!/usr/bin/env python3
# Coded By Tux-MacG1v
#https://t.me/I_am_a_silent_killer
#https://www.facebook.com/tux.macg1v
#DONATE ME:
#  TRC20 - TEd4f33f2c2AVGaB14VFCZbVLCe9hirNtK
#  BTC -  1KP3ekYeQGNVpMJr8P4hwwPPQ5sFP4h2Xb

import re
import os.path
import string
import os
import sys
import time
import urllib.request
from platform import system
import warnings
from concurrent.futures import ThreadPoolExecutor
from importlib import reload
from colorama import init, Fore, Style
from urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)
init(autoreset=True)
#try:
#	os.mkdir('Result') #createfolder
#	os.getcwd()
#except:
#	pass

reload(sys)
r = Fore.RED + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
o = Fore.RESET + Style.RESET_ALL

good=[]
bad=[]
failed =[]
GOOD = 0
BAD = 0
FAILED = 0

os.system("title " + "[+] GOOD:  {} , [-]BAD : {}  , [!]FAILED : {}  ".format(GOOD, BAD, FAILED))


banner = """

               {}[!] {}NOSLEP-DEMO {} - {}REVERSE IP{}
                    {}CODED BY TUX-MACG1V{}
	      {}FOR BUY MAIN TOOL CONTACT WITH ME{}
              {}https://t.me/I_am_a_silent_killer{}
	      {}TRC20-  TEd4f33f2c2AVGaB14VFCZbVLCe9hirNtK
	      BTC -  1KP3ekYeQGNVpMJr8P4hwwPPQ5sFP4h2Xb{}


""".format(r, g, y, g, o, r, o, y, o, r, o, g, o)
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

def reverseip(i):
	global GOOD, BAD, FAILED
	try:
		grab = urllib.request.urlopen('https://apifromtuxdemo1.herokuapp.com/'+ i, timeout=2000).read()
		html = grab.decode('ISO-8859-1')
		if not "null" in html:
			res = re.findall('"(.*?)"', html)
			print('{}[+] {}Reverse {}http://{} {}[{} {} {}DOMAINS]{}'.format(g, c, y, i, g, r, len(str(res)), g, o))
			for domain in res:
				open('Domains.txt', "a+").write(str(domain)+'\n')
				good.append(i)
				GOOD += 1
				
		else:
			print('{}[-] {}Reverse {}http://{} {}[{} NO DOMAIN {}]{}'.format(r, c, y, i, g, r, g, r, o))
			bad.append(i)
			BAD += 1
	except KeyboardInterrupt:
		print('{}[-] {}Reverse {}http://{} {}[{} API FAILED OR WRONG {}]{}'.format(r, c, y, i, g, r, g, r, o))
		failed.append(i)
		FAILED += 1
		time.sleep(0.5)
		sys.exit()

def main():
	try:
		os.system('cls' if os.name == 'nt' else 'clear')
		print(banner)
		lists = input('\n{}[+] {}Website List{} > {}'.format(c, g, o, g).strip())
		power = int(input('{}[+] {}Thread{} > {}'.format(c, g, o, r, r)))
		print('')

		def runner():
			threads = []
			domain = lists.replace('"', '')
			process = open(domain, 'r').read().splitlines()
			with ThreadPoolExecutor(max_workers=power) as thread:
				[threads.append(thread.submit(reverseip, i)) for i in process]

		runner()
		print("\n\n{}[+] TOTAL GOODS {}:{}[{}{}{}]{}".format(g, o, g, o, str(len(good)), g, o))
		print("{}[-] TOTAL BADS {}:{}[{}{}{}]{}".format(c, o, c, o, str(len(bad)), r, o))
		print("{}[!] TOTAL FAILED {}:{}[{}{}{}]{}".format(r, o, r, o, str(len(failed)), r, o))
	except Exception as e:
		print('{}[!] {}Incorrect'.format(c, r))
		time.sleep(0.5)

if __name__ == '__main__':
	main()
