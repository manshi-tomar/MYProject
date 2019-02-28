#!C:/Users/HP/AppData/Local/Programs/Python/Python37/python.exe
print ("Content-type:text/html")
print ("")

fp=open('header.py','r')
print (fp.read())
fp.close()

fp=open('usernav.py','r')
print (fp.read())
fp.close()

fp=open('slider.py','r')
print (fp.read())
fp.close()

import conn,cgitb
cgitb.enable()
form=conn.cgiconfig()
db=conn.dbconfig()
cursor=db.cursor()
query="select * from register"
cursor.execute(query)
data=cursor.fetchall()

"""import usertrack
unm=usertrack.usertrack()
usertrack.logincheck()
"""


print ("""
	<div id="page">
		<div id="content">
			<div class="box">
				

 <h2>CHANGE PASSWORD</h2><br>
 <h3>Fill the entries properly</h3><br>
                <form method="POST" action="" enctype="multipart/form-data">
                    <table  cellspacing='10'>

                        <tr>
                        <td>User name</td>
                        <td><input type='text' name='cunm'</td>
                        </tr>
                        <tr>
                        <td>Current Password</td>
                        <td><input type='passw' name='passwc'</td>
                        </tr>
                        <tr>
                        <td>New Password</td>
                        <td><input type='passw' name='passwn'</td>
                        </tr>
                        <tr>
                        <td></td>
                        <td><input type='submit' name='s'</td>
                        </tr>
                    </table>        
                </form>



	</div>

			<br class="clearfix" />
		</div>
		

""")

fp=open('sidebox.py','r')
print (fp.read())
fp.close()


fp=open('footer.py','r')
print (fp.read())
fp.close()



s=form.getvalue('s')
if s!=None:
	unmc=form.getvalue('cunm')
	passwc=form.getvalue('passwc')
	passwn=form.getvalue('passwn')
	
	query="UPDATE register SET passw='%s' WHERE unm='%s' AND passw='%s'" %(passwn,unmc,passwc)


	res=cursor.execute(query)
	db.commit()
	
	if res:	
		print ("<script>alert('Password changed successfully')</script>")
		print ("<script>window.location='passca.py'</script>")
	else:
		print ("<script>alert('Password not changed')</script>")
		print ("<script>window.location='passca.py'</script>")

