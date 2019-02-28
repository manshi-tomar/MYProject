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

import conn

form=conn.cgiconfig()
db=conn.dbconfig()
cursor=db.cursor()
query="select * from addcat order by id desc limit 0,9"
cursor.execute(query)
data=cursor.fetchall()

print ("""
	<div id="page">
		<div id="content">
			<div class="box">

		<style>
		#mycat
		{
			height:450px;
			width:600px;
		}
		#mycat_part
		{
			height:150px;
			width:200px;
			float:left;		
		}
		</style>		
<div id='mycat'>
""")

for element in data:
	print ("""
                       <a href='viewsubcat.py?catnm="""+element[1]+"""'>
			<div id='mycat_part'>
			<center>
			<img src='../uploads/"""+element[2]+"""' height='100' width='150'/>
			<br>
			<b>"""+element[1]+"""</b>
			</center>			
			</div>
			</a>
	""")		



print ("""
</div>
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
