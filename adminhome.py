#!C:/Users/HP/AppData/Local/Programs/Python/Python37/python.exe
print ("Content-type:text/html")
print ("")

fp=open('header.py','r')
print (fp.read())
fp.close()

fp=open('adminnav.py','r')
print (fp.read())
fp.close()

fp=open('slider.py','r')
print (fp.read())
fp.close()

"""import usertrack
unm=usertrack.usertrack()
usertrack.logincheckadmin()
"""
print ("""
	<div id="page">
		<div id="content">
			<div class="box">
				<h2>Welcome to Book-Market Admin Panel....</h2>
			
 This gives administrator all the rights about the post, he can unblock and block any advertisement posted by the user.


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
