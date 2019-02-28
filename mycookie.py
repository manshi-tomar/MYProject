C:/Users/HP/AppData/Local/Programs/Pythpn/Python37/python.exe

import Cookie
mycookie=Cookie.SimpleCookie()
mycookie['username']='abc'
mycookie['username']['expires']=3600*24
mycookie['password']=1234
mycookie['password']['expires']=3600*24
print (mycookie)


print ("Content-type:text/html")
print ("")

print ("<h1>Cookie stored successfully...</h1>")

import os
if 'HTTP_COOKIE' in os.environ:
	cookie_data=os.environ['HTTP_COOKIE']		
	cookie=cookie_data.split(';')	
		
	(c1,v1)=cookie[0].split('=')
	(c2,v2)=cookie[1].split('=')
	
	print (c2,'====>',v2,'<br>')
	print (c1,'====>',v1,'<br>')	
	
else:
	print ('no data')











