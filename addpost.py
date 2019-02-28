#!C:/Users/HP/AppData/Local/Programs/Python/Python37/python.exe
print ("Content-type:text/html")
print ("")

fp=open('header.py','r')
print (fp.read())
fp.close()

fp=open('usernav.py','r')
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
query="select * from addsubcat"
cursor.execute(query)
data=cursor.fetchall()

"""import usertrack
unm=usertrack.usertrack()
usertrack.logincheck()
"""


print ("""
	<div id="page">
		<div id="content">
			<div class="box">
				

 <h2>Advertisement Arena</h2><br>
 <h3>Post your advertisement here</h3><br>
                <form method="POST" action="" enctype="multipart/form-data">
                    <table  cellspacing='10'>
                        <tr>
                            <td>Book Name</td>
                            <td>
                            <input type="text" name="title" />    
                            </td>
                        </tr>
                        <tr>
                            <td>Category</td>
                            <td>
                                    <select name="cat_nm">
                                            <option>select category</option>
""")

for element in data:
	print ("<option>"+element[2]+"</option>")
print ("""
                 
         
              </select>    
                            </td>
                        </tr>

                        <tr>
                            <td>Ads Description</td>
                            <td>
                            <textarea name='description'></textarea>    
                            </td>
                        </tr>
                        <tr>
                                <td>Price</td>
                                <td>
                                <input type="text" name="price" />    
                                </td>
                            </tr>
                            <tr>
                                    <td>Ads Images</td>
                                    <td>
                                    Select File : <input type="file" name="myimg1" />
                                    <br><br>
                                    Select File : <input type="file" name="myimg2" />
                                    <br><br>
                                     </td>
                                </tr>
                            

                        <tr>
                            <td>Address</td>
                            <td>
                            <textarea name="address" rows="5" cols="32"></textarea>    
                            </td>
                        </tr>
                        <tr>
                                <td>Email ID</td>
                                <td>
                                <input type="text" name="email" />    
                                </td>
                            </tr>
                        <tr>
                            <td>Phone no.</td>
                            <td>
                            <input type="text" name="mob" />    
                            </td>
                        </tr>
                        <tr>
                            <td>City</td>
                            <td>
                            <select name="city">
                                <option>Select City</option>
                                <option>Indore</option>
                                <option>Bhopal</option>
                                <option>Ujjain</option>
                                <option>Khajuraho</option>
                                <option>Kanpur</option>
                                <option>Mumbai</option>
                                <option>Gwalior</option>
                                <option>Pune</option>
                                <option>Bengaluru</option>
                                <option>Calicut</option>
                                <option>Kolkata</option>
                                <option>Other City</option>
                            </select>    
                            </td>
                        </tr>
                        <tr>
                            <td colspan="2">
                               <input type="submit" name="s" value="Add Post" />     
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
	title=form.getvalue('title')
	cat_nm=form.getvalue('cat_nm')
	description=form.getvalue('description')
	price=form.getvalue('price')
	address=form.getvalue('address')
	email=form.getvalue('email')
	mob=form.getvalue('mob')
	city=form.getvalue('city')
	

	myimg1=form.getvalue('myimg1')
	if len(myimg1)>0:
		imgitem=form['myimg1']
		myimg1=imgitem.filename 
		fp=open('..//uploads//'+myimg1,'wb')
		fp.write(imgitem.file.read())	
		fp.close()
	else:
		myimg1="dummy.png"
	
	

	myimg2=form.getvalue('myimg2')
	if len(myimg2)>0:
		imgitem=form['myimg2']
		myimg2=imgitem.filename 
		fp=open('..//uploads//'+myimg2,'wb')
		fp.write(imgitem.file.read())	
		fp.close()
	else:
		myimg2="dummy.png"


	query="insert into postadd(title,sub_cat_nm,description,price,image1,image2,address,email,phone,city) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') " %(title,cat_nm,description,price,myimg1,myimg2,address,email,mob,city)

	

	res=cursor.execute(query)
	db.commit()
	
	if res:	
		print ("<script>alert('Post added successfully. You can see your post in respective subcategory once your post is validated')</script>")
		print ("<script>window.location='addpost.py'</script>")
	else:
		print ("<script>alert('post not added')</script>")
		print ("<script>window.location='addpost.py'</script>")

