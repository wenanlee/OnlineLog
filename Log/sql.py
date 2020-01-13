import sqlite3
conn = sqlite3.connect('log.db')
print('数据库打开')
def AddLog(log):
    print(log)
    name=log.split('|',1)[0]
    level=int(log[len(name)+1])
    info=log[len(name)+2:]
    print("name",name,"     level:",level,"  info:",info)
    global conn
    c=conn.cursor()
    c.execute("INSERT INTO log (app_name,log_level,log_info) VALUES ('{0}',{1},'{2}')".format(name,level,info))
    #c.execute("INSERT INTO log (app_name,log_level,log_info) VALUES ('aaa',1,'tesat')")
    conn.commit()
    return "ok"