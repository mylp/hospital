from flask import Flask, render_template, request, json, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root3069'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['SECRET_KEY'] = '1234567890'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('homepage.html')


@app.route('/signup')
def showSignUp():
    return render_template('signup.html')


@app.route('/api/contacted', methods=['POST'])
def showContacted():
    _fname = request.form['fname']
    _lname = request.form['lname']
    _email = request.form['email']
    _message = request.form['message']

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_addContactUsMessage', (_fname, _lname, _email, _message))
    data = cursor.fetchall()
    if len(data) == 0:
        conn.commit()
        return render_template('/contacted.html')
    else:
        return json.dumps({'error': str(data[0])})


@app.route('/contactUsMessageInbox')
def showCUMessages():
    data = getCUMessages()
    if data is not None:
        data = [d[1:] for d in data]
        return render_template('/contactUsMessages.html', data=data)
    else:
        return render_template('/contactUsMessages.html', data=[])


def getCUMessages():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_getContactUsMessages')
    data = cursor.fetchall()
    if len(data) == 0:
        return None
    else:
        return data


@app.route('/setHours')
def showSetHours():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    p_names = getPhysiciansByNameAndId().keys()
    schedules = getPhysicianSchedules()
    return render_template('setHours.html', days=days, p_names=p_names, schedules=schedules)


@app.route('/setHoursSuccess')
def setHoursSuccess():
    return render_template('setHoursSuccess.html')

@app.route('/seePhysSchedule')
def seePhysSchedule():
    return render_template('seePhysSchedule.html')

@app.route('/api/setHours', methods=['POST'])
def setHours():
    _mon = request.form['Monday']
    _tue = request.form['Tuesday']
    _wed = request.form['Wednesday']
    _thurs = request.form['Thursday']
    _fri = request.form['Friday']
    _sat = request.form['Saturday']
    _sun = request.form['Sunday']
    _pid = getPhysiciansByIdUsingName(request.form["physician"])
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
                        _tueTL, _wedTL, _thursTL, _friTL, _satTL, _sunTL))
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
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_getPhysicianSchedules')
    data = cursor.fetchall()
    if len(data) > 0:
        conn.commit()
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
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.callproc('sp_getAppointments', (session['user'],))
    appointments = cursor.fetchall()
    formatted = []
    for appointment in appointments:
        individual = []
        individual.append(str(appointment[1])) # Date)
        individual.append(appointment[3]) # Physician ID (This should display the physician name)
        individual.append(appointment[4]) # Description
        formatted.append(individual)
    unordered_list = "<ul><li>" + "</li><li>".join(str(x) for x in formatted) + "</li></ul>"
    return render_template('appointment.html', appointments=unordered_list)


@app.route('/createAppointment')
def showScheduleAppointment():
    return render_template('createAppointment.html')


@app.route('/login')
def showLogin():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/')


@app.route('/nurseHome')
def nurseHome():
    return render_template('nurseHome.html')

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

@app.route('/physicianHome')
def physicianHome():
    return render_template('physicianHome.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/api/changePassword', methods=['POST'])
def changePassword():
    _username = session['user']
    _password = request.form['inputPassword']
    _newPassword = request.form['inputConfirmPW']

    conn = mysql.connect()
    cursor = conn.cursor()
    if _password == _newPassword:
        password = generate_password_hash(_password)
        cursor.callproc('sp_changePassword', (_username, password))
    else:
        return json.dumps({'error': 'Passwords do not match!'})
    data = cursor.fetchall()

    return render_template("account.html", data=data)

headings=("Bed Id","Clinic Id","Room Number","Occupancy Status","Patient Id")

@app.route('/ManageBeds')
def ManageBeds():


    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.callproc('sp_getBeds')
    beds = cursor.fetchall()
    print(beds)
    return render_template('ManageBeds.html',headings=headings,beds=beds)


@app.route('/api/refreshAppointment', methods=['POST'])
def refreshAppointment():
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.callproc('sp_getAppointments', (session['user'],))
    dates = cursor.fetchall()

    return render_template("createAppointment.html", dates=dates)


@app.route('/api/createAppointment', methods=['POST'])
def createAppointment():
    _date = request.form['inputDate'] + " " + request.form['inputTime']
    _physician = request.form['inputPhysician']
    _patient = session['user']
    _reason = request.form['inputReason']

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_createAppointment', (_date, _physician, _patient, _reason))
    data = cursor.fetchall()

    if len(data) == 0:
        conn.commit()
        cursor.callproc('sp_getAppointments', (session['user'],))
        appointments = cursor.fetchall()
        formatted = []
        for appointment in appointments:
            individual = []
            individual.append(str(appointment[1])) # Date)
            individual.append(appointment[3]) # Physician ID (This should display the physician name)
            individual.append(appointment[4]) # Description
            formatted.append(individual)
        unordered_list = "<ul><li>" + "</li><li>".join(str(x) for x in formatted) + "</li></ul>"
        return render_template('appointment.html', appointments=unordered_list)
    else:
        return json.dumps({'error': str(data[0])})

@app.route('/api/deleteAppointment', methods=['POST'])
def deleteAppointment():
    _appointmentID = request.form['inputAppointmentID']
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_deleteAppointment', (_appointmentID,))
    data = cursor.fetchall()

    if len(data) == 0:
        return render_template('appointment.html')
    else:
        return json.dumps({'error': str(data[0])})

@app.route('/api/validateLogin', methods=['POST', 'GET'])
def validateLogin():
    _username = request.form['inputUsername']
    _password = request.form['inputPassword']

    con = mysql.connect()
    cursor = con.cursor()
    cursor.callproc('sp_validateLogin',(_username,))
    data = cursor.fetchall()

    if len(data) > 0:
        # definitely not safe security wise but need to be able to login in with original admin
        if check_password_hash(str(data[0][2]),_password) or (_username =='admin' and _password=='admin'):
            session['user'] = data[0][0]
            if data[0][13] == "user":
                return redirect('/userHome')
            elif data[0][13] == "phys":
                return redirect('/physicianHome')
            elif data[0][13] == "nurse":
                return redirect('/nurseHome')
            else:
                return redirect('/adminHome')
        else:
            return render_template('error.html', error='Wrong Email address or Password')
    else:
        return render_template('error.html', error='Wrong Email address or Password')

@app.route('/userHome')
def userHome():
    conn = mysql.connect()
    cursor = conn.cursor()
    id = session['user']
    cursor.callproc('sp_getUser', (id,))
    data = cursor.fetchall()
    return render_template('userhome.html', headings=headings,data=data)

@app.route('/api/signup', methods=['POST'])
def signUp():
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
    _username=request.form['inputUsername']
    _password = request.form['inputPassword']

    if all((_username, _password, _first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email)):

        password = generate_password_hash(_password)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_createUser',
                        (_username, password, _first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email))
        data = cursor.fetchall()

        if len(data) == 1:
            conn.commit()
            session['user'] = data[0][0]
            return redirect('/userHome')
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
        password = generate_password_hash(_password)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_createPhysician', (
            _username, password, _first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email, _type, _spec,
            _rank, _deptId, _clinicId))
        data = cursor.fetchall()

        if len(data) == 0:
            conn.commit()
            return render_template('adminHome.html')
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

@app.route('/api/signupNurse', methods=['POST'])
def signupNurse():
    _username=request.form['inputUsername']
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
    _classification= request.form['Classification']
    _deptId= request.form['DepartmentID']
    _clinicId= request.form['ClinicID']

    if all( (_username,_password,_first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email,_classification,_deptId,_clinicId)):
        password = generate_password_hash(_password)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_createNurse', (_username, password,_first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email,_classification,_deptId,_clinicId))
        data = cursor.fetchall()

        if len(data) == 0:
            conn.commit()
            return render_template('adminHome.html')
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route('/api/signupAdmin', methods=['POST'])
def signupAmin():
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
    _deptId = int(request.form['DepartmentID'])

    if all((_username, _password, _first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email, _type,
            _deptId)):
        password = generate_password_hash(_password)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_createAdmin', (
            _username, password, _first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email, _type,
            _deptId))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return render_template('adminHome.html')
        else:
            return json.dumps({'error': data})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route('/api/addBed', methods=['POST'])
def addBed():
    idbed= request.form['idBed']
    idclinic= request.form['idClinic']
    room_number= request.form['roomNum']
    occupancy_status= request.form['status']
    idpatient= request.form['idPatient']


    if all( (idbed,idclinic,room_number,occupancy_status,idpatient)):

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_addBeds', (idbed,idclinic,room_number,occupancy_status,idpatient))
        data = cursor.fetchall()

        if len(data) == 0:
            conn.commit()
            return redirect('/ManageBeds')
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

@app.route('/api/deleteBed', methods=['POST'])
def adddeleteBed():
    idbed= request.form['idBed']


    if all( (idbed)):

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_deleteBeds', (idbed))
        data = cursor.fetchall()

        if len(data) == 0:
            conn.commit()
            return redirect('/ManageBeds')
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})





if __name__ == '__main__':
    app.run(debug=True)
