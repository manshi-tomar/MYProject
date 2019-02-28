#!C:/Users/HP/AppData/Local/Programs/Python/Python37/python.exe
print ("Content-type:text/html")
print ("")

fp=open('header.py','r')
print (fp.read())
fp.close()

fp=open('nav.py','r')
print (fp.read())
fp.close()

fp=open('slider.py','r')
print (fp.read())
fp.close()

print ("""
	<div id="page">
		<div id="content">
			<div class="box">
				<h2>Welcome to Book Market</h2>
				<h2>Service page</h2>

			<!-- Write content here -->The main requirement of the application is to be time saver, this saves a lot of time of travelling again and again to the market. It should be user friendly. This project will be able to save time and money of the student so that they can use it somewhere else effectively and efficiently.  		

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
