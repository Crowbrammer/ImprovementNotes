
import sqlite3

def open_connection():

	global conn 
	global c
	conn = sqlite3.connect('mydb.db')
	c= conn.cursor()

def close_connection():

	c.close()
	conn.close()
	
def create_table(table1, table2=None, table3=None):
	
	open_connection()
	
	print('create_table() was called')

	c.execute('CREATE TABLE IF NOT EXISTS '
	
	close_connection()
	
def insert_data(tb=None, col1=None, data1=None, col2=None, data2=None, col3=None, 	data3=None):
	
	print('insert_data() was called')
	
	if tb == None: pass
	
	elif col1 is None: pass
	
	elif col1 is not None or data1 is not None:
	
		if col2 is not None or data2 is not None:
		
			if col3 is not None or data3 is not None:
			
				c.execute('INSERT INTO ' + tb + '(' + col1 + ', ' + col2 + ', ' + col3 + ') VALUES(?, ?, ?)', (data1, data2, data3))
				
			else: 
			
				c.execute('INSERT INTO ' + tb + '(' + col1 + ', ' + col2 + ') VALUES(?, ?)', (data1, data2))
				
		else:
		
			c.execute('INSERT INTO ' + tb + '(' + col1 + ') VALUES(?)', (data1,))
	
	conn.commit()
	
	print('insert_data() finished')
	
	'''Example use:
	
	insert_data('machineID_modelID_status', 'machineID', 'test', 'modelID', 'test')'''

def get_data(table_name=None, column_name=None):

	open_connection()
	
	c.execute('SELECT {cn} FROM {tn} ORDER BY {cn}'.\
        format(tn=table_name, cn=column_name))
	print(c.fetchall())

	close_connection()
	
get_data('your_table_name', 'your_column_name')