import pymysql

def sql():
    db = pymysql.connect(
        user = 'root',
        passwd = 'password',
        #host = '120.136.121.44',
        #port = 9007,
        host = '192.168.200.140',
        port = 3306,
        db = 'Monitor'
    )
    j_dict = {}
    i = 0
    cursor = db.cursor(pymysql.cursors.DictCursor)

    sql="""
    SELECT id, temp, pres FROM (SELECT id, temp, pres FROM sensorvalue ORDER BY id DESC LIMIT 10)
    AS A ORDER BY id ASC"""
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

