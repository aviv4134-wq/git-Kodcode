
import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    port = 3306,
    database = 'soldier_4'
)

curs = conn.cursor(dictionary=True)

# #curs.execute('''
#     CREATE TABLE IF NOT EXISTS soldiers(
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name  VARCHAR(100) NOT NULL,
#     mrank VARCHAR(50),
#     unit  VARCHAR(100),
#     active BOOLEAN 
#          )''')
# curs.execute('''INSERT INTO soldiers(name,mrank, unit, active) VALUES
#              ('Yonatan Har', 'sergeant', '8200', TRUE),
#              ('Rivka Dagan', NULL, '9900', FALSE),
#              ('Benny Mizrahi', 'private', '8200', TRUE);
#              ''')
# conn.commit()

