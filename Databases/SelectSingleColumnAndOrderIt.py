import sqlite3

def get_data(table_name=None, column_name=None):

	open_connection()
	
	c.execute('SELECT {cn} FROM {tn} ORDER BY {cn}'.\
        format(tn=table_name, cn=column_name))
	print(c.fetchall())

	close_connection()
	
# get_data('your_table_name', 'your_column_name')