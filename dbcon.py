from mysql import connector as c

def connect():
    return c.connect(host='localhost',user='root',password='',database='school_management')