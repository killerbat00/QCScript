import urllib2
import os

start = int(raw_input('Input a starting comic: '))
end = int(raw_input('Input an ending comic: ')) + 1
dir = 'Questionable Content'
if not os.path.exists(dir):
	os.makedirs(dir)
extensions = ['.png', '.jpg', '.gif']
exists = True


for x in xrange(start, end):
	extension = extensions[0]
	picture_page = "http://www.questionablecontent.net/comics/"+str(x)
	
	try:
		response = urllib2.urlopen(picture_page + extension)
	except urllib2.URLError, e:
		if hasattr(e, 'code'):
			if e.code == 404:
				exists = False
				extension = extensions[1]

	if exists == False:
			try:
				response = urllib2.urlopen(picture_page + extension)
			except urllib2.URLError, e:
				if hasattr(e, 'code'):
					if e.code == 404:
						extension = extensions[2]
						exists = True
	print picture_page + extension
	opener1 = urllib2.build_opener()
	page1 = opener1.open(picture_page + extension)
	my_picture = page1.read()
	filename = os.path.join(dir,"Comic" + str(x) + extension)
	print filename
	fout = open(filename, "wb")
	fout.write(my_picture)
	fout.close()