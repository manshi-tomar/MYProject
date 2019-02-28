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


import conn,cgitb
cgitb.enable()
form=conn.cgiconfig()
db=conn.dbconfig()
cursor=db.cursor()
query="select * from postadd"
cursor.execute(query)
data=cursor.fetchall()


print ("""

	<div style='overflow:scroll;' id="page">
				<h2>View Ads To Verify....</h2>
				<br>
				<br>
""")
"""
import usertrack
unm=usertrack.usertrack()
usertrack.logincheckadmin()
"""
print( """


	<table id="example" class="display"  border="4px solid black" cellspacing="15px" cellpadding="5px">
        <thead>
            <tr>
							<th>Title</th>
<th>Description</th>
<th>Price</th>
<th>Image1</th>
<th>Image2</th>

<th>Address</th>
<th>Email</th>
<th>Phone</th>
<th>City</th>
<th>Status</th>	
            </tr>
        </thead>
        <tbody>
""")


for row in data:
	print ("<tr>")
	print ("<td>",row[1],"</td>")
	print ("<td>",row[3],"</td>")	
	print ("<td>",row[4],"</td>")
	print ("<td><img src='../uploads/"+row[5]+"' height='50' width='70'/></td>")
	print ("<td><img src='../uploads/"+row[6]+"' height='50' width='70'/></td>")
	print ("<td>",row[7],"</td>")	
	print ("<td>",row[8],"</td>")
	print ("<td>",row[9],"</td>")
	print ("<td>",row[10],"</td>")
	print ("<td>",row[11],"</td>")
	
	if row[11]==0:	
		print ("<td><a style='color:green;' href='viewadsadmin.py?unblock="+str(row[0])+"'>Un-Block Post</a></td>")	
	else:
		print ("<td><a style='color:red;' href='viewadsadmin.py?block="+str(row[0])+"'>Block Post</a></td>")
		
	print ("</tr>")


print ("""            
         </tbody>
        <tfoot>
            
        </tfoot>
    </table>
    <br>
    <br>

""")
               
fp=open('footer.py','r')
print (fp.read())
fp.close()


unblock=form.getvalue('unblock')
if unblock!=None:
	query="update postadd set status=1 where pid=%s" %(unblock)
	cursor.execute(query)
	db.commit()
	print ("<script>alert('post unblocked')</script>")
	print ("<script>window.location='viewadsadmin.py'</script>")

block=form.getvalue('block')
if block!=None:
	query="update postadd set status=0 where pid=%s" %(block)
	cursor.execute(query)
	db.commit()
	print ("<script>alert('post blocked')</script>")
	print ("<script>window.location='viewadsadmin.py'</script>")







