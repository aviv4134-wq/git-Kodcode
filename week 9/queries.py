import mysql.connector
import db

def get_by_rank(rank):
    conn = db.get_connection()
    curs = conn.cursor(dictionary=True)
    show = 'SELECT * FROM soldiers WHERE mrank = %s'
    mrank = (rank,)
    curs.execute(show,mrank)
    soldiers = curs.fetchall()
    curs.close()
    conn.close()
    return soldiers

def get_active_sorted(order):
    conn = db.get_connection()
    curs = conn.cursor(dictionary=True)
    if order.upper() not in ["ASC", "DESC"]:
        order = "ASC"
    show = f'''
    SELECT * FROM soldiers
    WHERE active = TRUE
    ORDER BY name {order};
    '''
    curs.execute(show)
    soldiers = curs.fetchall()
    curs.close()
    conn.close()
    return soldiers

def get_distent_unit():
    conn = db.get_connection()
    curs = conn.cursor()
    show = '''
    SELECT DISTINCT unit FROM soldiers;  
    '''
    curs.execute(show)
    units = curs.fetchall()
    curs.close()
    conn.close()
    return units

def search_by_name(term):
    conn = db.get_connection()
    curs = conn.cursor(dictionary=True)
    curs.execute("SELECT * FROM soldiers WHERE name LIKE %s",
    (f"%{term}%",)
             )
    soldier = curs.fetchall()
    curs.close()
    conn.close()
    return soldier

def get_missing_rank():
    conn = db.get_connection()
    curs = conn.cursor(dictionary=True)
    show = 'SELECT * FROM soldiers WHERE mrank IS NULL'
    curs.execute(show)
    soldiers = curs.fetchall()
    curs.close()
    curs.close()
    return soldiers

def get_by_unit(unit):
    conn = db.get_connection()
    curs = conn.cursor(dictionary=True)
    show = 'SELECT * FROM soldiers WHERE unit = %s ORDER BY name ASC'
    unit = (unit,)
    curs.execute(show,unit)
    soldiers = curs.fetchall()
    curs.close()
    conn.close()
    return soldiers

def get_sorted_by_id():
    conn = db.get_connection()
    curs = conn.cursor(dictionary=True)
    curs.execute('SELECT * FROM soldiers ORDER BY id ASC')
    sol = curs.fetchall()
    curs.close()
    conn.close()
    return sol

    

if __name__ == '__main__':
    #print(get_by_rank('private'))
    #print(get_active_sorted('desc'))
    #print(get_distent_unit())
    #print(search_by_name(''))
    #print(get_missing_rank())
    #print(get_by_unit('8200'))
    print(get_sorted_by_id())