
## Import libraries
import mysql.connector
#from mysql.connector.constants import ClientFlag

## function for connecting the sql and extracting data

##  function to connect and return the data retreived from the db
def connect_return_data():
	words_sql = []
	phrases_sql = []

	config = {
	    'user': 'root',
	    'password': 'SouthAfrica_2020',
	    'host': '35.236.104.20',
            'database' : 'hate_speech_dict',
#	    'client_flags': [ClientFlag.SSL],
	    'ssl_ca': '/home/dsurkutwar/mysqlCerts/ca.pem',
	    'ssl_cert': '/home/dsurkutwar/mysqlCerts/client-cert.pem',
	    'ssl_key': '/home/dsurkutwar/mysqlCerts/client-key.pem'
	}


	db = mysql.connector.connect(**config)

	# Creating a Cursor object
	cur = db.cursor(buffered=True)

	#Using sql commands through execute command 
	cur.execute("SELECT * FROM tb_all;")

	# print all the first cell of all the rows

	for row in cur.fetchall():
	  words_sql.append(row[0])
	  phrases_sql.append(row[1])


	db.close()

	print(words_sql)
	print(phrases_sql)
	return(words_sql,phrases_sql)

