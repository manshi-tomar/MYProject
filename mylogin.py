#!C:/Users/HP/AppData/Local/Programs/Python/Python37/python.exe

import conn,Cookies

userdetail=Cookies.SimpleCookie()

form=conn.cgiconfig()
db=conn.dbconfig()
cursor=db.cursor()


s=form.getvalue('s')
if s!=None:
	unm=form.getvalue('unm')
	passw=form.getvalue('pass')
	
	query="select * from register where unm='%s' && pass='%s'" %(unm,passw)

	cursor.execute(query)
	data=cursor.fetchone()
	
	if data!=None:
		userdetail['username']=data[2]
		userdetail['role']=data[8]
		print (userdetail)								



print ("Content-type:text/html")
print ("")


if data!=None:
		print ("<script>alert('login success!!!')</script>")
		if data[8]=='admin':		
			print ("<script>window.location='adminhome.py'</script>")
		if data[8]=='user':		
			print ("<script>window.location='userhome.py'</script>")
else:
		print ("<script>alert('login failed!!!')</script>")
		print ("<script>window.location='login.py'</script>")
