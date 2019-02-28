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

import conn ,cgitb
cgitb.enable()
form=conn.cgiconfig()
db=conn.dbconfig()
cursor=db.cursor()
query="select * from addcat"
cursor.execute(query)
data=cursor.fetchall()

"""import usertrack
unm=usertrack.usertrack()
usertrack.logincheckadmin()
"""
print ("""
	<div id="page">
		<div id="content">
			<div class="box">
				<h2>Add sub category!!!</h2>
				
			<form method="POST" action="" enctype="multipart/form-data">
                    <table  cellspacing='10'>
<tr>
                            <td>Select Category</td>
                            <td>
                            <select name='cat_nm'>
			    <option>select category</option>
                            
""")
for element in data:
	print ("<option>"+element[1]+"</option>")
print ("""				
		 </select>            
                            </td>
                        </tr>                        
<tr>
                            <td>Sub Category Name</td>
                            <td>
                            <input type="text" name="sub_cat_nm" />    
                            </td>
                        </tr>
                        <tr>
                            <td>Sub Category Image</td>
                            <td>
                            <input type='file' name='cat_img' />    
                            </td>
                        </tr>
                        
                        <tr>
                            <td colspan="2">
                               <input type="submit" name="s" value="Add Sub Category" />     
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



s=form.getvalue('s')
if s!=None:
	
	cat_nm=form.getvalue('cat_nm')
	sub_cat_nm=form.getvalue('sub_cat_nm')	
	imgitem=form['cat_img']
	cat_img=imgitem.filename 

	fp=open('../uploads/'+cat_img,'wb')
	fp.write(imgitem.file.read())	
	fp.close()	
	
	query="insert into addsubcat(cat_nm,sub_cat_nm,sub_cat_img) values('%s','%s','%s')" %(cat_nm,sub_cat_nm,cat_img)
	
	res=cursor.execute(query)
	db.commit()

	if res:	
		print ("<script>alert('subcategory added successfully')</script>")
		print ("<script>window.location='addsubcat.py'</script>")
	else:
		print ("<script>alert('subcategory not added')</script>")
		print ("<script>window.location='addsubcat.py'</script>")


















