import mysql.connector
import time

conn = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    password = 'root',
    user = 'root'
)

curs = conn.cursor()

curs.execute('CREATE DATABASE IF NOT EXISTS soldiers_db')
curs.execute('USE soldiers_db')

create_table = '''
CREATE TABLE IF NOT EXISTS soldiers( 
    id   INT,
    name VARCHAR(50),
    mrank VARCHAR(50),
    unit  INT,
    active BOOLEAN  DEFAULT TRUE  
       )'''


curs.execute(create_table)
print('success create')

curs.close()
conn.close()



