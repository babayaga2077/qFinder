from app import mysql
from flask import session

		
def GetQuote(data):
	conn = mysql.connect()
	cursor =conn.cursor()
	try:
		cursor.execute("SELECT quote,author from quotes_all where quote like '%"+data+"%'")
		data = cursor.fetchall()
		if data:
			return data
		else:
			return "Sorry, cannot find your request."	
	except Exception as e: 
		return str(e)
	finally:
		conn.close()

def GetFlag():
	conn = mysql.connect()
	cursor =conn.cursor()
	try:
		cursor.execute("SELECT id,flag from flag")
		data = cursor.fetchall()
		retunr data
	except Exception as e: 
		return str(e)
	finally:
		conn.close()

def IsLoggedIn():
	if session.get('username', None):
		return True
	else:
		return False