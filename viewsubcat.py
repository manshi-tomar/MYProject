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
catnm=form.getvalue('catnm')
db=conn.dbconfig()
cursor=db.cursor()
query="select * from addsubcat where cat_nm='%s'" %(catnm)
cursor.execute(query)
data=cursor.fetchall()

query1="select * from addcat"
cursor.execute(query1)
data1=cursor.fetchall()

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

<h1>Sub Category List</h1><br><br>
<div id='mycat'>
""")

for element in data:
	print ("""				
			<a href='viewads.py?subcatnm="""+element[2]+"""'>
			<div id='mycat_part'>
			<center>
			<img src='../uploads/"""+element[3]+"""' height='100' width='150'/>
			<br>
			<b>"""+element[2]+"""</b>
			</center>			
			</div>
			</a>
	""")		



print ("""
</div>
</div>

			<br class="clearfix" />
		</div>
		<div id="sidebar">
			<div class="box">
				<h3>Category List</h3>
				<ul class="list">
""")
for element in data1:
	print ("<li><a href='viewsubcat.py?catnm="+element[1]+"'>"+element[1]+"</a></li>")

print ("""
				</ul>
			</div>
			
		</div>
		<br class="clearfix" />
	</div>

""")

fp=open('footer.py','r')
print (fp.read())
fp.close()
