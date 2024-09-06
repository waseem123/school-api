from flask import Flask,request
import controller as c

app = Flask(__name__)

@app.route("/students")
def allstudents():
    result = c.getAllStudents()
    if len(result)>0:
        return result
    else:
        return {'message':'No data present at this moment'}
    
@app.route('/students/<int:rollno>')
def getStudent(rollno):
    result = c.getByRollNo(rollno)
    return result

@app.route('/students/getbycity',methods=['GET','POST'])
def getStudentsByCity():
    if request.method=='GET':
        city = request.args['city']
        result = c.getStudentsByCity(city)
        print(result)
        return result
    
@app.route('/students/searchbyname',methods=['GET','POST'])
def getStudentsByName():
    if request.method=='GET':
        name = request.args['name']
        result = c.searchbyname(name)
        print(result)
        return result

    
@app.route('/students/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        result = c.loginuser(username,password)
        if result is not None:
            result['status'] = 'success'
            result['message']='Login Successful'
            # result.update({'status':'success','message':'Login Successfull'})
        else:
            result = {'status':'failure','message':'Login Failed due to invalid username or password'}
        return result
    else:
        return {'status':'failure','message':'Login Failed'}
    
@app.route('/students/registration',methods=['GET','POST'])
def register():
    if request.method=='POST':
        name = request.form['studname']
        username = request.form['username']
        password = request.form['password']
        dept = request.form['department']
        result = c.registerStudent(name,username,password,dept)
        return result
    else:
        return {'status':'failure','message':'INVALID METHOD REQUEST'}