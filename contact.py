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
			<center><h1><font color='blue'><font face='Bedrock'>Welcome to our book market...</font></font></h1></center>
				</br></br><h4> You can Contact here!!!</h4>

			<p> 		

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
