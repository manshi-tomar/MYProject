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
				<h2><font color='purple'><font face='Bedrock'>Complete Your Registration Here!!!</font></font></h2>
				<form method="POST" action="">
                    <table  cellspacing='10'>
                        <tr>
                            <td><font color='purple'><font face='Bedrock'>Name</font></font></td>
                            <td>
                            <input  type="text" name="nm" placeholder="name"/>    
                            </td>
                        </tr>
                        <tr>
                            <td><font color='purple'><font face='Bedrock'>Username(Email ID)</font></font></td>
                            <td>
                            <input  type="text" name="unm" placeholder="email"/>    
                            </td>
                        </tr>
                        <tr>
                            <td><font color='purple'><font face='Bedrock'>Password</font></font></td>
                            <td>
                            <input type="password" name="passw" placeholder="password"/>    
                            </td>
                        </tr>
                        <tr>
                            <td><font color='purple'><font face='Bedrock'>Address</font></font></td>
                            <td>
                            <textarea name="address" rows="5" cols="32"></textarea>    
                            </td>
                        </tr>
                        <tr>
                            <td><font color='purple'><font face='Bedrock'>Phone no.</font></font></td>
                            <td>
                            <input type="text" name="mob" placeholder="phone no." />    
                            </td>
                        </tr>
                        <tr>
                            <td><font color='purple'><font face='Bedrock'>City</font></font></td>
                            <td>
                           <font face='Bedrock'><select name="city"></font>
                                <option>Select City</option>
                                <option>Indore</option>
                                <option>Bhopal</option>
                                <option>Ujjain</option>
                                <option>Gwalior</option>
                                <option>Kanpur</option>
                                <option>Mumbai</option>
                            </select>    
                            </td>
                        </tr>
                        <tr>
                            <td><font color='purple'><font face='Bedrock'>Gender</font></td>
                            <td>
                        <font color='purple'><font face='Bedrock'>   Male <input type="radio" name="gender" value='male' checkbox/></font></font>
                            &nbsp;&nbsp;    
                         <font color='purple'><font face='Bedrock'> Female <input type="radio" name="gender" value='female'/></font></font>
                            </td>
                        </tr>
                        <tr>
                            <td colspan="8">
                            <button><input style="background-color:yellowgreen;"type="submit" name="s" value="Register" /></button>     
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

import cgi,cgitb,pymysql
		
cgitb.enable()
form=cgi.FieldStorage()
s=form.getvalue('s')
if s!=None:
	nm=form.getvalue('nm')
	unm=form.getvalue('unm')
	passw=form.getvalue('passw')
	address=form.getvalue('address')
	mob=form.getvalue('mob')
	city=form.getvalue('city')
	gender=form.getvalue('gender')	

		#code to connect with mysql database
	db=pymysql.connect('localhost','root','','book')
	cursor=db.cursor()	

	query="insert into register(nm,unm,passw,address,mob,city,gender,role) values('%s','%s','%s','%s',%s,'%s','%s','user')" %(nm,unm,passw,address,mob,city,gender)
	
	result=cursor.execute(query);
	db.commit()
	if result:
                
		print ('<h1>Record inserted....</h1>')
	else:
		print ('<h1>Record not inserted....</h1>')	









