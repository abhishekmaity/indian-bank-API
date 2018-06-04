from flask import Flask
import json
import sqlite3
app = Flask(__name__)

#Given a bank branch IFSC code, get branch details
@app.route('/ifsc/<ifsc_code>')
def ifsc_get(ifsc_code):
	conn = sqlite3.connect('bank.db')
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM bank_branches where ifsc=?;", (ifsc_code,) )
	branch = cursor.fetchall()
	conn.commit()
	return json.dumps(branch)

#Given a bank name and city, gets details of all branches of the bank in the city
@app.route('/bank_name/<bank_name>/city/<city>')
def branch_city_get(bank_name,city):
	conn = sqlite3.connect('bank.db')
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM bank_branches where bank_name=? and city=?;", (bank_name,city,) )
	branches = cursor.fetchall()
	conn.commit()
	return json.dumps(branches)

if __name__=='__main__':
	app.run(debug=False,host='127.0.0.1',port=8000)