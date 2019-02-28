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
				<h2>Add category!!!</h2>
				
			<form method="POST" action="" enctype="multipart/form-data">
                    <table  cellspacing='10'>
                        <tr>
                            <td>Category Name</td>
                            <td>
                            <input type="text" name="cat_nm" />    
                            </td>
                        </tr>
                        <tr>
                            <td>Category Image</td>
                            <td>
                            <input type='file' name='cat_img' />    
                            </td>
                        </tr>
                        
                        <tr>
                            <td colspan="2">
                               <input type="submit" name="s" value="Add Category" />     
                            </td>
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

import conn ,cgitb
cgitb.enable()
form=conn.cgiconfig()
db=conn.dbconfig()
cursor=db.cursor()

s=form.getvalue('s')
if s!=None:
	cat_nm=form.getvalue('cat_nm')
	imgitem=form['cat_img']
	cat_img=imgitem.filename 

	fp=open('../uploads/'+cat_img,'wb')
	fp.write(imgitem.file.read())	
	fp.close()	
	
	query="insert into addcat(cat_nm,cat_img) values('%s','%s')" %(cat_nm,cat_img)
	
	res=cursor.execute(query)
	db.commit()

	if res:	
		print ("<script>alert('category added successfully')</script>")
		print ("<script>window.location='addcat.py'</script>")
	else:
		print ("<script>alert('category not added')</script>")
		print ("<script>window.location='addcat.py'</script>")


















