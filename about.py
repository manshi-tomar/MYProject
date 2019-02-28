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
				<h2>About page</h2>

			Books are integral part of process of gaining knowledge. Books do not help only in reading they help us in making a perception and thinking and imagining. But it is not possible to buy all the books to read them all. We always need to buy books for studying because even though in today’s era we have pdf of complete books but a large portion of people prefer reading form hardcopies. Going to book shops and searching for books, going again if we didn’t get it in previous attempt and doing this again to get the book again. This is like a tedious never-ending cycle. If we buy a second hand book then we have to give more amount because the shopkeeper also want profit. Now if we want to sell a book we have to go to a shop and sell it in a very less amount to a shopkeeper.   		

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
