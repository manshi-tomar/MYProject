import cgi,pymysql


def cgiconfig():
	form=cgi.FieldStorage()
	return form

def dbconfig():
	db=pymysql.connect('localhost','root','','book')
	return db	
