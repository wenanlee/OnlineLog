import sqlite3
import json
import pymysql

conn = sqlite3.connect('log.db')
print('数据库打开')
def AddLog(log):
    args=json.loads(log)
    global conn
    c=conn.cursor()
    sql="INSERT INTO log (app_name,log_level,log_info) VALUES "
    for item in args["log"]:
        sql+="('{0}',{1},'{2}'),".format(args['name'],item['level'],item['info'])
    sql=sql[:-1]+';'
    c.execute(sql)
    conn.commit()
    return "ok"

def GetLog(json):
    #args=json.loads(log)
    global conn
    c=conn.cursor()
    sql="SELECT * FROM log"
    c.execute(sql)
    f = open("select.html", "r",encoding='utf-8').read()
    html=''
    for row in c.fetchall():
        html=html+('<tr class="alt"><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(row[0],row[1],row[2],row[3],row[4],row[5]))
    return f.replace('command',html)