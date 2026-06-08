import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        port = 3306,
        database = 'soldiers_db' 
    )

def get_all() -> list:
    conn = get_connection()
    curs = conn.cursor(dictionary=True)
    curs.execute('SELECT * FROM soldiers')
    soldiers = curs.fetchall()

    curs.close()
    conn.close()
    return soldiers

def get_by_id(soldier_id:int):
    conn = get_connection()
    curs = conn.cursor(dictionary=True)
    select = 'SELECT * FROM soldiers WHERE id  = %s'
    curs.execute(select,(soldier_id,))
    soldier = curs.fetchone()
    curs.close()
    conn.close()
    return soldier

def create(name,mrank,unit) ->int:
    conn = get_connection()
    curs = conn.cursor()
    values = (name,mrank,unit)
    createe = 'INSERT INTO soldiers(name,mrank,unit) VALUES (%s,%s,%s);'
    curs.execute(createe,values)
    last_id = curs.lastrowid
    conn.commit()
    curs.close()
    curs.close()
    return last_id


def update(soldier_id:int,data:dict):
    conn = get_connection()
    curs = conn.cursor()
    ser_parts = [f'{key} = %s' for key in data.keys()]
    set_clause = ','.join(ser_parts)

    sql = f'UPDATE soldiers SET {set_clause} WHERE id = %s'
    values = list(data.values()) + [soldier_id]
    curs.execute(sql,values)
    conn.commit()
    conn.close()
    conn.close()
    return True

def delete(soldier_id:int):
    conn = get_connection()
    curs = conn.cursor()
    delete = 'DELETE FROM soldiers WHERE id = %s'
    curs.execute(delete,(soldier_id,))
    conn.commit()
    curs.close()
    conn.close()
    return 'deleting'





#print(create('avi','ert','455'))
#print(get_by_id(1))
print(delete(1))
print(get_all())