import sqlite3
import json
import time
conn = sqlite3.connect('log.db')
print('数据库打开')

def AddLog(log):
    args = dict(item.split("=", 1) for item in log.split("&", 2))
    print(args)
    global conn
    c = conn.cursor()
    sql = "INSERT INTO log (app_name,log_level,log_info) VALUES "
    for item in json.loads(args["log"]):
        sql += "('{0}',{1},'{2}'),".format(args['name'],item['level'], item['info'] )
    sql = sql[:-1]+';'
    print(sql)
    c.execute(sql)
    conn.commit()
    return "ok"
    
#查询
def GetLog(arg):
    #args = dict(item.split("=", 1) for item in arg.split("&", 2))
    global conn
    print(arg)
    c = conn.cursor()
    sql = "SELECT * FROM log WHERE "+arg
    c.execute(sql)
    f = open("select.html", "r", encoding='utf-8').read()
    html = ''
    for row in c.fetchall():
        html = html+('<tr class="alt"><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(
            row[0], row[1], row[2], row[3], row[4], row[5]))
    return f.replace('command', html)