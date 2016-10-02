import urllib
import re
file1= open("images.txt","w")
url1= raw_input("enter the website")
a= urllib.urlopen(url1)
html= a.read()
src1= re.compile("<img.*src=\"([^ ]*)\"")
dep=re.findall(src1,html)
for i in dep:
	if i.startswith("/"):
		print url1+i
		file1.write(url1+i+"\n")
	else:
		print url1+"/"+i
		file1.write(url1+"/"+i+"\n")
file1.close()			
