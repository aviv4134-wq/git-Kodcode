import setup_reports

conn = setup_reports.conn
curs = setup_reports.curs

def get_summery():  #ACTIVE NOT ACTIV
    conn = setup_reports.conn
    curs.execute('SELECT COUNT(*) AS total FROM soldiers')
    total = curs.fetchone()
    curs.execute('SELECT COUNT(*) AS active FROM soldiers WHERE active = TRUE')
    active = curs.fetchone()
    curs.execute('SELECT COUNT(*) AS inactive FROM soldiers WHERE active =  FALSE')
    inactive = curs.fetchone()
    curs.close()
    

    return [total,active,inactive]

def count_by_unit(): #[{"unit": "8200", "total": 4}, ...]
    conn = setup_reports.conn
    curs = setup_reports.curs
    curs.execute('SELECT unit, COUNT(*) AS unit_total FROM soldiers GROUP BY unit ORDER BY unit_total DESC  ')
    total = curs.fetchall()


    return total

def get_missing_data(): #Soldiers where rank IS NULL
    curs.execute('SELECT COUNT(*) AS soldiers_rank_null FROM soldiers WHERE mrank IS NULL')
    total = curs.fetchone()


    return total

def get_units_with_multiple_soldiers(): # Only units that have more than 1 soldier (useHAVING)
    curs.execute(
        '''SELECT unit,COUNT(*) AS units_soldiers_total
           FROM soldiers
           GROUP BY unit
           HAVING units_soldiers_total > 1;
           ''')    
    total = curs.fetchall()
        
        
    return total

def soldiers_by_rank():
    curs.execute('SELECT COUNT(*) AS ranks FROM soldiers')
    numberof_ranks = curs.fetchone()



    return numberof_ranks

def stats_units_top():
    curs.execute('SELECT unit,COUNT(*) AS max_unit FROM soldiers GROUP BY unit ORDER BY max_unit DESC LIMIT 1;')
    max_unit = curs.fetchone()




    return max_unit


if __name__ == '__main__':
    # print(get_summery())
    #print(count_by_unit())
    # print(get_missing_data())
    # print(get_units_with_multiple_soldiers())
    #print(soldiers_by_rank())
    print(stats_units_top())