from bs4 import BeautifulSoup
import urllib2
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'
}
num= 1
numm=1

for s in range(4):
    url = "https://www.packtpub.com/all-products/all-books?released=Available&page=7"+str(numm)
    numm +=1   
    req = urllib2.Request (url, headers=hdr)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup (page, features="html.parser")
    f = open('page'+str(num)+".html", 'w') 
    f.write(str(soup)) 
   
    f.close()
    num +=1   



 
    