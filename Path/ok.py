# -*- coding: utf-8 -*-
#!/usr/bin/python2
#coding=utf-8
#originally written by Azmi
try:
	import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests
        from multiprocessing.pool import ThreadPool
        from requests.exceptions import ConnectionError
        from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('python2 MS.py')
if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):
    os.system("apt update && apt install nodejs -y")
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

from requests.exceptions import ConnectionError
s = requests.Session()
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])

reload(sys)
sys.setdefaultencoding('utf8')
os.system('termux-setup-storage')
os.system('clear')

logo = '\n        \x1b[1;97m    __  __           _    _ \n           |  \\/  |         | |  (_)\n           | \\  / |_   _ ___| | ___ \n           | |\\/| | | | / __| |/ / |\n           | |  | | |_| \\__ \\   <| |\n           |_|  |_|\\__,_|___/_|\\_\\_|                      \n \x1b[1;90m---------------------------------------------\n\x1b[1;97m [+] AUTHER     :   MUSKI \n [+] FACEBOOK   :   XTYLISH PATHANI \n [+] WHATSAPP   :   +1541xxxxxxx\n [+]\x1b[1;97m BE ORIGINAL LETS THE WORLD COPY YOU\n \x1b[1;97m---------------------------------------------'

    

def menu():
	
	os.system('clear')
        print logo
	print"    Change user agent"
	print""
	hos = raw_input("[+] Paste User Agent :  ")
	if hos =="":
		print" Put user agent 1st"
		time.sleep(5)
		menu()
	elif hos =="1":
	    print" Put user agent 1st"
	    menu()
	    time.sleep(5)
	elif hos =="827272":
	    print" Put user agent 1st"
	    menu()
	else:
	    main()
def main():
    os.system('clear')
    print logo
    print""
    print "[1] Facebook Cloning"
    print "[2] Access Token Extension"
    print "[3] Follow Me On Facebook"
    print "[4] Change user agent"
    print "[0] Exit            "
    menu2_menu()
	
def menu2_menu():
    m2m = raw_input('\nSelect :  ')
    if m2m =="":
        print "[!] Filled Incorrectly."
        time.sleep(1)
        menu2_menu()
    elif m2m =="1":
        os.system('clear')
        Crack()
    elif m2m =="2":
        os.system('clear')
        choice2()
    elif m2m =="3":
        os.system('clear')
    elif m2m =="4":
        os.system('clear')
        change()
    elif m2m =="0":
         os.system('clear')
         print"Exit Successfully"
    
def change():
    os.system('clear')
print logo
print""
print"Run This Link To Get user agent"
print"\x1b[1;95mhttps://myuseragent.blogspot.com\x1b[1;97m"
print ('      ')
hos = raw_input("[+] Paste User Agent :  ")
if hos =="":
	print" Put user agent 1st"
	time.sleep(5)
	menu()
elif hos =="1":
	print" Put user agent 1st"
        menu()
        time.sleep(5)
elif hos =="827272":
    print" Put user agent 1st"
    menu()
else:
	main()
    


     
def Crack():
    print logo
    print""
    print "[1] Random Cloning"
    print "[2] Login Cloning"
    print "[3] Return main menu"
    print "[0] Exit            "
    menu3_menu()
	
def menu3_menu():
    m3m = raw_input('\nSelect :  ')
    if m3m =="":
        print "[!] Filled Incorrectly."
        time.sleep(1)
        os.system('clear')
        menu3_menu()
    elif m3m =="1":
        os.system('clear')
        Random()
    elif m3m =="2":
        os.system('clear')
        login()
    elif m3m =="3":
        os.system('clear')
        main()
    elif m3m =="0":
        
        print"Exit Successfully"
    
def Random():
    print logo
    print""
    print "[1] Random Numbers "
    print "[2] Random mails"
    print "[3] Random username"
    print "[4] Searching, Hashtags, Lists"
    print "[5] Return To Previous menu"
    print "[0] Exit "
    menu4_menu()
	
def menu4_menu():
    m4m = raw_input('\nSelect :  ')
    if m4m =="":
        print "[!] Filled Incorrectly."
        time.sleep(1)
        menu4_menu()
    elif m4m =="1":
        os.system('clear')
        number()
    elif m4m =="2":
        os.system('clear')
        mail()
    elif m4m =="3":
        os.system('clear')
        os.system('clear')
        main()
    elif m4m =="4":
        os.system('clear')
        other()
    elif m4m =="5":
        os.system('clear')
        Crack()
    elif m4m =="0":
        print"Exit Successfully"
    


    
if __name__=='__main__':
    menu()
    
    
    
