import sqlite3
import json
import time
conn = sqlite3.connect('log.db')
print('数据库打开')
f = open("select.html", "r", encoding='utf-8').read()

#登录
def Login(arg):
    print("arg:"+arg)
    args = dict(item.split("=", 1) for item in arg.split("&", 2))
    global conn
    c = conn.cursor()
    sql = "SELECT * FROM user WHERE username='{}' and password='{}'".format(args['username'],args['password'])
    print("sql:"+sql)
    try:
        c.execute(sql)
        uid = c.fetchone()
        print("uid",uid,uid!=None,uid[0])
        print("UPDATE user SET app_count=app_count+1 WHERE id = {}".format(uid[0]))
        if uid!=None:
            c.execute("UPDATE user SET app_count=app_count+1 WHERE id = {}".format(uid[0]))
            conn.commit()
            return "uid"+str(uid[0])
        else:
            return "false username is None"
    except(sqlite3.DatabaseError) as e:
        print(e)
        return "false"

#添加
def AddLog(log):
    args = dict(item.split("=", 1) for item in log.split("&", 2))
    global conn
    c = conn.cursor()
    print(args['uid'])
    print(type(int(args['uid'])))
    
    sql = "INSERT INTO log (uid,app_name,log_level,log_info,time,app_count) VALUES "
    for item in json.loads(args["log"]):
        print(item['info'])
        print(item['level'])
        sql += "({0},'{1}',{2},'{3}','{4}',(SELECT app_count FROM user WHERE id={0})),".format(int(args['uid']),args['name'],item['level'], item['info'],item['time'])
    sql = sql[:-1]+';'
    print(sql)
    try:
        c.execute(sql)
        conn.commit()
        return "true"
    except:
        c.rollback()
        return "false" 

#查询
def GetLog(arg):
    #args = dict(item.split("=", 1) for item in arg.split("&", 2))
    global conn
    c = conn.cursor()
    sql = "SELECT * FROM log WHERE "+arg+' and id IN (select min(id) from log group by log_info)'
    print(sql)
    try:
        c.execute(sql)
        global f
        html = ''
        for row in c.fetchall():
            html = html+('<tr class="alt"><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(
                row[0], row[2], row[3], row[4], row[5], row[6]))
        return f.replace('command', html)
    except:
        return "false"

#删除
def DelLog(arg):
    global conn
    c = conn.cursor()
    sql = "DELETE FROM log WHERE "+arg
    print(sql)
    try:
        c.execute(sql)
        conn.commit()
        return "true"
    except:
        c.rollback()
        return "false"

def Quit():
    global conn
    c = conn.cursor()
    c.close()