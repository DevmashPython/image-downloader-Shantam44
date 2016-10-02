import urllib
import re
file1= open("images.txt","w")
url1= "https://www.tutorialspoint.com/"
a= urllib.urlopen(url1)
html= a.read()
src1= re.compile("<img.*src=\"([^ ]*)\"")
dep=re.findall(src1,html)
for i in dep:
	if i.startswith("/"):
		print "https://www.tutorialspoint.com"+i
		file1.write("https://www.tutorialpspoint.com"+i+"\n")
	else:
		print url1+i
		file1.write(url1+i+"\n")
file1.close()			