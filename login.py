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
import cgitb
cgitb.enable()
                       
                           
                           

print ("""
	<div id="page">
		<div id="content">
			<div class="box">
				<h2><font color='olive'><font face='Bedrock'>Please Login First!!!</font></font></h2>
	
			<form method="POST" action="">
                    <table  cellspacing='15'>
                        <tr>
                            <td><font face ='Bedrock'><font color='purple'>Username(Email ID)</font></font></td>
                            <td>
                
                            <input style="border:2px solid black;" type="text" name="unm" placeholder="username" />    
                            </td>
                        </tr>
                        <tr>
                            <td><font face ='Bedrock'><font color='purple'>Password</font></font></td>
                            <td>
                            <input style="border:2px solid black;" type="password" name="passw"  placeholder="password"/>    
                            </td>
                        </tr>
                        
                        <tr>
                            <td colspan="8">
                              <button> <input style="background-color:yellowgreen;" type="submit" name="s" value="Login" />    </button> 
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


import conn
form=conn.cgiconfig()
db=conn.dbconfig()
cursor=db.cursor()


s=form.getvalue('s')
if s!=None:
        
	unm=form.getvalue('unm')
	passw=form.getvalue('passw')
	query="select * from register where unm='%s' && passw='%s'" %(unm,passw)
	cursor.execute(query)
	data=cursor.fetchone()
	if data!=None:
		print ("<script>alert('login success!!!')</script>")
		if data[8]=='admin':		
			print ("<script>window.location='adminhome.py'</script>")
			
                        
		if data[8]=='user':		
			print ("<script>window.location='userhome.py'</script>")
                        
	else:
		print ("<script>alert('login failed!!!')</script>")
		print ("<script>window.location='login.py'</script>")


	
	





