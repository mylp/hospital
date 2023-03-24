from flask import Flask, render_template, request, json, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flaskext.mysql import MySQL

from datetime import datetime
import sys

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Gooster1225!2'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/signup')
def showSignUp():
    return render_template('signup.html')


@app.route('/setHours')
def showSetHours():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    p_names = getPhysiciansByNameAndId().keys()
    schedules = getPhysicianSchedules()
    return render_template('setHours.html', days=days, p_names=p_names, schedules=schedules)


@app.route('/setHoursSuccess')
def setHoursSuccess():
    return render_template('setHoursSuccess.html')


@app.route('/api/setHours', methods=['POST'])
def setHours():
    _mon = request.form['Monday']
    _tue = request.form['Tuesday']
    _wed = request.form['Wednesday']
    _thurs = request.form['Thursday']
    _fri = request.form['Friday']
    _sat = request.form['Saturday']
    _sun = request.form['Sunday']
    try:
        _pid = getPhysiciansByIdUsingName(request.form["physician"])
    except:
        _pid = ''

    _monTL = ''
    _tueTL = ''
    _wedTL = ''
    _thursTL = ''
    _friTL = ''
    _satTL = ''
    _sunTL = ''

    if request.form["MondayTimes"] is not None and _mon == "1":
        _monTL = request.form["MondayTimes"]
    if request.form["TuesdayTimes"] is not None and _tue == "1":
        _tueTL = request.form["TuesdayTimes"]
    if request.form["WednesdayTimes"] is not None and _wed == "1":
        _wedTL = request.form["WednesdayTimes"]
    if request.form["ThursdayTimes"] is not None and _thurs == "1":
        _thursTL = request.form["ThursdayTimes"]
    if request.form["FridayTimes"] is not None and _fri == "1":
        _friTL = request.form["FridayTimes"]
    if request.form["SaturdayTimes"] is not None and _sat == "1":
        _satTL = request.form["SaturdayTimes"]
    if request.form["SundayTimes"] is not None and _sun == "1":
        _sunTL = request.form["SundayTimes"]

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_setHours',
                    (
                        _pid, int(_mon), int(_tue), int(_wed), int(_thurs), int(_fri), int(_sat), int(_sun), _monTL,
                        _tueTL,
                        _wedTL, _thursTL, _friTL, _satTL, _sunTL))
    data = cursor.fetchall()
    if len(data) == 0:
        conn.commit()
        json.dumps({'message': 'Hours add successfully!'})
        return redirect('/setHoursSuccess')
    else:
        return json.dumps({'error': str(data[0])})


def getPhysiciansByNameAndId():
    listOfPhysicianNamesIds = []
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_getPhysiciansByNameAndId')
    data = cursor.fetchall()
    if len(data) > 0:
        conn.commit()
        listOfPhysicianNamesIds = data
        json.dumps({'message': 'Physician names grabbed successfully'})
    l = {}
    for tup in listOfPhysicianNamesIds:
        l[tup[0] + " " + tup[1]] = tup[2]
    return l


def getPhysiciansByIdUsingName(name):
    phyDict = getPhysiciansByNameAndId()
    return phyDict[name]


def getPhysicianSchedules():
    lst = []
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_getPhysicianSchedules')
    data = cursor.fetchall()
    if len(data) > 0:
        conn.commit()
        listOfPhysicianNamesIds = data
        json.dumps({'message': 'Physician schedule successfully'})
    lst = data
    formatted = []
    for tup in lst:
        individual = []
        name = [k for k, v in getPhysiciansByNameAndId().items() if v == tup[0]][0]
        individual.append(name)
        for time in tup[8:]:
            individual.append(time)
        formatted.append(individual)

    return formatted


@app.route('/appointment')
def showAppointment():
    return render_template('appointment.html')


@app.route('/createAppointment')
def showScheduleAppointment():
    return render_template('createAppointment.html')


@app.route('/login')
def showLogin():
    return render_template('login.html')


@app.route('/userHome')
def userHome():
    return render_template('userHome.html')


@app.route('/adminHome')
def adminHome():
    return render_template('adminHome.html')


@app.route('/createPhysician')
def createPhysician():
    return render_template('createPhysician.html')


@app.route('/createNurse')
def createNurse():
    return render_template('createNurse.html')


@app.route('/createAdmin')
def createAdmin():
    return render_template('createAdmin.html')


@app.route('/PhysicianHome')
def PhysicianHome():
    return render_template('PhysicianHome.html')


@app.route('/api/refreshAppointment', methods=['POST'])
def refreshAppointment():
    _date = request.form['inputDate']

    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.callproc('get_appointments', (_date,))
    dates = cursor.fetchall()

    return render_template("createAppointment.html", dates=dates)


@app.route('/api/createAppointment', methods=['POST'])
def createAppointment():
    _date = request.form['inputDate']
    _time = request.form['inputTime']
    _physician = request.form['inputPhysician']
    _patient = request.form['inputPatient']
    _reason = request.form['inputReason']

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_createAppointment', (_date, _time, _physician, _patient, _reason))
    data = cursor.fetchall()

    if len(data) == 0:
        conn.commit()
        return json.dumps({'message': 'Appointment created successfully !'})
    else:
        return json.dumps({'error': str(data[0])})


@app.route('/api/login', methods=['POST'])
def login():
    _username = request.form['inputUsername']
    _password = request.form['inputPassword']

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_validateLogin', (_username, _password))
    data = cursor.fetchall()

    if len(data) > 0:
        return json.dumps({'message': 'User successfully logged in'})
    else:
        return json.dumps({'error': 'Invalid username or password'})


@app.route('/api/validateLogin', methods=['POST'])
def validateLogin():
    try:
        _username = request.form['inputEmail']
        _password = request.form['inputPassword']
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('sp_validateLogin', (_username, _password))
        data = cursor.fetchall()
        if len(data) > 0:
            if check_password_hash(str(data[0][3]), _password):
                session['user'] = data[0][0]
                return redirect('/userHome')
            else:
                return render_template('error.html', error='Wrong Email address or Password')
        else:
            return render_template('error.html', error='Wrong Email address or Password')
    except Exception as e:
        return render_template('error.html', error=str(e))
    finally:
        cursor.close()
        con.close()


@app.route('/api/signup', methods=['POST'])
def signUp():
    _username = request.form['inputUsername']
    _first = request.form['inputFirst']
    _last = request.form['inputLast']
    _street = request.form['inputStreet']
    _city = request.form['inputCity']
    _state = request.form['inputState']
    _zip = request.form['inputZip']
    _phone = request.form['inputPhone']
    _dob = request.form['inputDOB']
    _sex = request.form['inputSex']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    if all((_username, _password, _first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email)):

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_createUser',
                        (_username, _password, _first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email))
        data = cursor.fetchall()

        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'User created successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route('/api/signupPhysician', methods=['POST'])
def signupPhysician():
    _username = request.form['inputUsername']
    _password = request.form['inputPassword']
    _first = request.form['inputFirst']
    _last = request.form['inputLast']
    _street = request.form['inputStreet']
    _city = request.form['inputCity']
    _state = request.form['inputState']
    _zip = request.form['inputZip']
    _phone = request.form['inputPhone']
    _dob = request.form['inputDOB']
    _sex = request.form['inputSex']
    _email = request.form['inputEmail']
    _type = request.form['Type']
    _spec = request.form['Specialization']
    _rank = request.form['Rank']
    _deptId = request.form['DepartmentID']
    _clinicId = request.form['ClinicID']

    if all((_username, _password, _first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email, _type, _spec,
            _rank, _deptId, _clinicId)):

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_createPhysician', (
            _username, _password, _first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email, _type, _spec,
            _rank, _deptId, _clinicId))
        data = cursor.fetchall()

        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'Physician created successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


if __name__ == '__main__':
    app.run(debug=True)
