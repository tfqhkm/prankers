import os, sys

print ("\033[1;32mINSERT USERNAME & PASSWORD")

print ("\033[1;32IIF YOU WANT TO KNOW CONTACT: 0189710113")

username = 'lcf.err'      

password = 'smktamanjasmin2'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[1;32mTHANK YOU", 

			sys.exit()



		else:

			print "\033[1;32mPLEASE CHECK YOUR USERNAME OR PASSWORD INSTEAD [?]\033[00m"

			print "CONTACT : 0189710113\n"

			restart()



	else:

		print "\033[1;32mPLEASE CHECK YOUR USERNAME OR PASSWORD INSTEAD [?]\033[00m"

		print "CONTACT : 0189710113\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
