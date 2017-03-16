import urllib2

def WriteFile(str):
    with open('/mnt/d/Temp/proxylist.txt', "a") as f:
        f.write(str+'\n')
        return

def GetURL(URLString):
	attempts = 0
	while attempts < 3:
		try:
			opener = urllib2.build_opener()
			urllib2.install_opener(opener)
			
			response = urllib2.urlopen(URLString, timeout = 30)
			content = response.read()
			#print(content)
			from bs4 import BeautifulSoup
			soup = BeautifulSoup(content)
			for row in soup.findAll("script"):
				riga= ''.join(map(str, row.contents))
				#print(riga)
				if 'gp.insertPrx' in riga:
					StrArray = riga.split(":")
					IP = StrArray[3].split(",")[0].replace('\"','')
					port = str(int(StrArray[5].split(",")[0].replace('\"',''), 16))
					WriteFile(IP+":"+port)

			break
		except urllib2.URLError as e:
			attempts += 1
			print type(e)

GetURL("http://gatherproxy.com/proxylist/anonymity/?t=Anonymous#1")
GetURL("http://gatherproxy.com/proxylist/anonymity/?t=Anonymous#2")