import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        password = 'root',
        user = 'root',
        database =  'soldiers_db'
    )

def get_schema():
    conn = get_connection()
    curs = conn.cursor()
    curs.execute('DESCRIBE soldiers;')
    rows = curs.fetchall()
    curs.close()
    conn.close()
    return [{"name": row[0], "type": row[1]} for row in rows]
