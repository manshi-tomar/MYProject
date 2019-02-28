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
subcatnm=form.getvalue('subcatnm')
db=conn.dbconfig()
cursor=db.cursor()
query="select * from postadd where sub_cat_nm='%s' && status=1" %(subcatnm)
cursor.execute(query)
data=cursor.fetchall()

print ("""
	<div id="page">
		<div id="content">
			<div class="box">

<style>
#myadd
{
 border:2px solid #6E6E6E;
}
</style>

<h1>View Ads</h1><br><br>
""")
for ads in data:
	print ("""<table style='border:2px solid black;'  id='myadd' height='150' width='100%'>
<tr>
<td width='35%' rowspan='5'>
<center>
<img src='../uploads/"""+ads[5]+"""' height='100' width='200' />
</center>
</td>
<td>
<font color='black'><b>Title :<font color='blue'> """+ads[1]+"""</font></b></font>
</td>
</tr>
<tr>
<td><font color='black'><b>Description :<font color='blue'> """+ads[3]+"""</font></b></font></td>
</tr>
<tr>
<td><font color='black'><b>E-mail :<font color='blue'> """+ads[8]+"""</font></b></font></td>
</tr>
<tr>
<td><font color='black'><b>Mobile No. :<font color='blue'> """+ads[9]+"""</font></b></font></td>
</tr>
<tr>
<td><font color='black'><b>Price : <font color='blue'>"""+ads[4]+"""</font></b></font></td>
</tr>
</table> <br><br>
	""")

print ("""
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
