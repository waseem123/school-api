import dbcon as c

def getAllStudents():
    connection = c.connect()
    sql = "SELECT rollno,name,marks,city FROM student"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def getByRollNo(rollno):
    connection = c.connect()
    sql = f"SELECT rollno,name,marks,city FROM student WHERE rollno = {rollno}"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def getStudentsByCity(city):
    connection = c.connect()
    sql = f"SELECT rollno,name,marks,city FROM student WHERE city = '{city}'"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def searchbyname(name):
    connection = c.connect()
    sql = f"SELECT rollno,name,marks,city FROM student WHERE name LIKE '%{name}%'"
    print(sql)
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def loginuser(username,password):
    connection = c.connect()
    sql = f"SELECT rollno,name,city FROM student WHERE username='{username}' AND password='{password}'"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result

def registerStudent(name,username,password,dept):
    connection = c.connect()
    sql = f"INSERT INTO student(name,username,password,dept_id)VALUES('{name}','{username}','{password}','{dept}')"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()
    return {'success':True,'message':'Registration succesful'}
# print(searchbyname('Sarfaraz'))