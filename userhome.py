#!C:/Users/HP/AppData/Local/Programs/Python/Python37/python.exe
print ("Content-type:text/html")
print ("")

"""<?php
$cookie_name = "user";
$cookie_value = "John Doe";
setcookie($cookie_name, $cookie_value, time() + (86400*30), "/");
?>"""
"""print ("<?php")
print ( "setcookie('name', 'John Watkin', time()+3600, '/','', 0);)
print ("setcookie('age', '36', time()+3600, '/', '',  0);")
print ("?>")"""

fp=open('header.py','r')
print (fp.read())
fp.close()

fp=open('usernav.py','r')
print (fp.read())
fp.close()

fp=open('slider.py','r')
print (fp.read())
fp.close()

        

"""import usertrack
unm=usertrack.usertrack()
usertrack.logincheck()
"""

print ("""
	<div id="page">
		<div id="content">
			<div class="box">
				<h2>Welcome to Book-Market User Panel....</h2>
			

<!--Hello-->Here user can get the email id and contact number of the seller so they could interact and lock the deal.  

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






