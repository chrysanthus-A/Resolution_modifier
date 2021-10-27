import PIL
from PIL import Image
import os
import re 

def multiple_image(resolution):
	

	location=input("Enter the location of the images")
	os.chdir(location)

	dirlist=os.listdir(os.curdir)
	for i,x in enumerate(dirlist):
		c=str(i)
		name=re.split(r"[.]",x)
		os.rename(x,name[0]+'.jpg')
	dirlist=os.listdir(os.curdir)
	for  i,x in enumerate(dirlist):
		name=str(i)
		f=Image.open(x)
		f=f.resize(resolution,PIL.Image.ANTIALIAS)
		f.save(x)
	#os.rename(x,name+'.jpg')





def single_image(resolution):
	location=input("Enter the location of the images")
	name=input("Enter the name of the image ")
	os.chdir(location)
	dirlist=os.listdir(location)	
	print(dirlist)
	#txt=re.search(r"\w\w\w\w\w\w*",dirlist[0])
	#print(txt.group(0))
	for a in dirlist:
		if(re.search(r"^\w*",a).group(0)==name):
			f=Image.open(a)
			f=f.resize(resolution,PIL.Image.ANTIALIAS)
			f.save(a)
			break	









opt=int(input("do you want to change the resolution of multiple images or single image \n 1]single Image \n 2]Multiple Images\n"))
c=input("Enter the new resolution")

h=re.split(r"[x | *]",c)

resolution=(int(h[0]),int(h[1]))

if(opt==1):
	single_image(resolution)
elif(opt==2):
	multiple_image(resolution
