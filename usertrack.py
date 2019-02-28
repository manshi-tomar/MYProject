import os
from http import cookies


def usertrack():
        
	if 'HTTP_COOKIE' in os.environ:
		data=os.environ['HTTP_COOKIE']
		cookie=data.split(';')
		(c2,v2)=cookie[0].split('=')
		(c1,v1)=cookie[1].split('=')
		return v1
	else:
		print ("<script>alert('Invalid user please login first...')</script>")
		print ("<script>window.location='login.py'</script>")
	
def logincheck():
	if 'HTTP_COOKIE' in os.environ:
		data=os.environ['HTTP_COOKIE']
		cookie=data.split(';')
		(c2,v2)=cookie[0].split('=')
		(c1,v1)=cookie[1].split('=')
	if v2=='admin':
		print ("<script>alert('Invalid user please login first...')</script>")
		print ("<script>window.location='login.py'</script>")

def logincheckadmin():
	if 'HTTP_COOKIE' in os.environ:
		data=os.environ['HTTP_COOKIE']
		cookie=data.split(';')
		(c2,v2)=cookie[0].split('=')
		(c1,v1)=cookie[1].split('=')
	if v2=='user':
		print ("<script>alert('Invalid user please login first...')</script>")
		print ("<script>window.location='login.py'</script>")
		
