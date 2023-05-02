from flask import Flask, render_template, request, json, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()


def connect_to_db(app):
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'PepeSilvia1259#12!'
    app.config['MYSQL_DATABASE_DB'] = 'test'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    app.config['SECRET_KEY'] = '1234567890'
    mysql.app = app
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
    cursor.callproc('sp_addContactUsMessage',
                    (_fname, _lname, _email, _message))
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
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    p_names = getPhysiciansByNameAndId().keys()
    schedules = getPhysicianSchedules()
    return render_template('setHours.html', days=days, p_names=p_names, schedules=schedules)


@app.route('/ownSchedule')
def ownSchedule():
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    p_names = getPhysiciansByNameAndId().keys()
    schedules = getPhysicianSchedulesById()
    return render_template('ownSchedule.html', days=days, p_names=p_names, schedules=schedules)


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
                        _pid, int(_mon), int(_tue), int(_wed), int(
                            _thurs), int(_fri), int(_sat), int(_sun), _monTL,
                        _tueTL, _wedTL, _thursTL, _friTL, _satTL, _sunTL))
    data = cursor.fetchall()
    if len(data) == 0:
        conn.commit()
        json.dumps({'message': 'Hours add successfully!'})
        return redirect('/setHours')
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
        name = [k for k, v in getPhysiciansByNameAndId().items()
                if v == tup[0]][0]
        individual.append(name)
        for time in tup[8:]:
            individual.append(time)
        formatted.append(individual)

    return formatted


def getPhysicianNameByID(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_getPhysicianNameByID', (id,))
    data = cursor.fetchall()
    if len(data) > 0:
        conn.commit()
        json.dumps({'message': 'Physician name successfully'})
    return data[0][0] + " " + data[0][1]


def getPhysicianSchedulesById():

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_getPhysicianSchedulesById', (session['user'],))
    data = cursor.fetchall()
    if len(data) > 0:
        conn.commit()
        json.dumps({'message': 'Physician schedule successfully'})
    lst = data
    formatted = []
    for tup in lst:
        individual = []
        name = [k for k, v in getPhysiciansByNameAndId().items()
                if v == tup[0]][0]
        individual.append(name)
        for time in tup[8:]:
            individual.append(time)
        formatted.append(individual)

    return formatted


def getAppointments():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_getAppointments', (session['user'],))
    appointments = cursor.fetchall()
    formatted = []
    for appointment in appointments:
        individual = [appointment[0], appointment[1],
                      appointment[2], appointment[3]]
        formatted.append(individual)
    return formatted


def getStatements():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_getStatements', (session['user'],))
    statements = cursor.fetchall()
    return statements

@app.route('/api/changeInsurance', methods=['GET','POST'])
def changeInsurance():
    try:
        _insurance = request.form['inputInsurance']
    except:
        return render_template('account.html', error='Please enter an insurance provider')
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_changeInsurance', (session['user'], _insurance))
    data = cursor.fetchall()
    if len(data) == 0:
        conn.commit()
        return redirect(url_for('account', insurance=_insurance))
    else:
        return json.dumps({'error': str(data[0])})

@app.route('/billing')
def showBilling():
    user_statements = getStatements()
    unpaid = []
    paid = []
    for statement in user_statements:
        if not statement[3]:  # Unpaid
            unpaid.append(statement)
        else:
            paid.append(statement)
    return render_template('billing.html', unpaid=unpaid, paid=paid)


@app.route('/showStatement', methods=['GET','POST'])
def showStatement():
    statement_id = request.args.get(('statement_id'))
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_getInvoices', (statement_id,))
    invoices = cursor.fetchall()
    return render_template('statement.html', invoices=invoices)



@app.route('/appointment')
def showAppointment():
    user_appointments = getAppointments()
    for appointment in user_appointments:
        appointment[2] = getPhysicianNameByID(appointment[2])
    return render_template('appointment.html', appointments=user_appointments)


@app.route('/createAppointment')
def showScheduleAppointment():
    p_names = getPhysiciansByNameAndId().keys()
    return render_template('createAppointment.html', p_names=p_names)


@app.route('/login')
def showLogin():
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
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


headings = ("Bed Id", "Clinic Id", "Room Number",
            "Occupancy Status", "Patient Id")


@app.route('/ManageBeds')
def ManageBeds():

    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.callproc('sp_getBeds')
    beds = cursor.fetchall()
    print(beds)
    return render_template('ManageBeds.html', headings=headings, beds=beds)


@app.route('/api/createAppointment', methods=['POST'])
def createAppointment():
    p_names = getPhysiciansByNameAndId().keys()
    _date = request.form['inputDate'] + " " + request.form['inputTime']
    _physician = getPhysiciansByIdUsingName(request.form["physician"])
    _patient = session['user']
    _reason = request.form['inputReason']

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_createAppointment',
                    (_date, _physician, _patient, _reason))
    data = cursor.fetchall()

    if len(data) == 0:
        conn.commit()
        new_appointments = getAppointments()
        return render_template('appointment.html', appointments=new_appointments)
    else:
        return json.dumps({'error': str(data[0])})


@app.route('/api/saveAppointment', methods=['POST'])
def saveAppointment():
    _date = request.form['inputDate'] + " " + request.form['inputTime']
    _physician = getPhysiciansByIdUsingName(request.form["physician"])
    _reason = request.form['inputReason']
    _appointmentID = request.form['inputID']

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_modifyAppointment',
                    (_appointmentID, _date, _physician, _reason))
    data = cursor.fetchall()

    if len(data) == 0:
        conn.commit()
        return redirect('/appointment')
    else:
        return json.dumps({'error': str(data[0])})


@app.route('/api/modifyAppointment', methods=['GET', 'POST'])
def modifyAppointment():
    appointments = getAppointments()
    phys = getPhysiciansByNameAndId().keys()
    _appointmentID = int(request.args.get('appointment_id'))
    unselected = []
    selected = None
    for appointment in appointments:
        if appointment[0] == _appointmentID:
            selected = appointment
        else:
            unselected.append(appointment)
    date = selected[1]
    time = date.time()
    date = date.strftime("%Y-%m-%d")
    selected = [selected[0], date, time, selected[2], selected[3]]
    appointments = [
        appointment for appointment in appointments if appointment[0] != _appointmentID]
    for appointment in appointments:
        appointment[2] = getPhysicianNameByID(appointment[2])
    selected_phys = getPhysicianNameByID(selected[3])
    return render_template('modifyAppointment.html', appointments=unselected, p_names=phys, selected=selected, selected_phys=selected_phys)


@app.route('/api/deleteAppointment', methods=['GET', 'POST'])
def deleteAppointment():
    _appointmentID = int(request.args.get('appointment_id'))
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_deleteAppointment', (_appointmentID,))
    data = cursor.fetchall()
    if len(data) == 0:
        conn.commit()
        return redirect('/appointment')
    else:
        return json.dumps({'error': str(data[0])})


@app.route('/api/validateLogin', methods=['POST', 'GET'])
def validateLogin():
    _username = request.form['inputUsername']
    _password = request.form['inputPassword']

    con = mysql.connect()
    cursor = con.cursor()
    cursor.callproc('sp_validateLogin', (_username,))
    data = cursor.fetchall()

    if len(data) > 0:
        # definitely not safe security wise but need to be able to login in with original admin
        if check_password_hash(str(data[0][2]), _password) or (_username == 'admin' and _password == 'admin'):
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


userHeadings = ("First Name", "Last Name", "Street", "City",
                "State", "Zip", "Phone Number", "DOB", "Sex", "Email")


@app.route('/userHome')
def userHome():
    conn = mysql.connect()
    cursor = conn.cursor()
    id = session['user']
    cursor.callproc('sp_getUser', (id,))
    data = cursor.fetchall()
    return render_template('userhome.html', headings=userHeadings, data=data[0][3:-1])


appointmentHeadings = ("Appointment Date", "Description",
                       "Physician First Name", "Physician last Name")


@app.route('/seeOwnAppointment')
def seeOwnAppointment():
    conn = mysql.connect()
    cursor = conn.cursor()
    id = session['user']
    cursor.callproc('sp_getAppointments', (id,))
    data = cursor.fetchall()
    return render_template('seeOwnAppointment.html', headings=appointmentHeadings, data=data)


phyAppHeadings = ("Appointment Date", "Description",
                  "Patient Id", "Patient First Name", "Patient last Name")


@app.route('/seePhysSchedule')
def seePhysSchedul():
    conn = mysql.connect()
    cursor = conn.cursor()
    id = session['user']
    cursor.callproc('sp_getPhysicianAppointments', (id,))
    data = cursor.fetchall()
    return render_template('seePhysSchedule.html', headings=phyAppHeadings, data=data)


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
    _username = request.form['inputUsername']
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
    _spec = request.form['Specialization']
    _rank = request.form['Rank']
    _deptId = request.form['DepartmentID']
    _clinicId = request.form['ClinicID']

    if all((_username, _password, _first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email, _spec,
            _rank, _deptId, _clinicId)):
        password = generate_password_hash(_password)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_createPhysician', (
            _username, password, _first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email, _spec,
            _rank, _deptId, _clinicId))
        data = cursor.fetchall()

        if len(data) == 0:
            conn.commit()
            return redirect('/adminHome')
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route('/api/signupNurse', methods=['POST'])
def signupNurse():
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
    _classification = request.form['Classification']
    _deptId = request.form['DepartmentID']
    _clinicId = request.form['ClinicID']

    if all((_username, _password, _first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email, _classification, _deptId, _clinicId)):
        password = generate_password_hash(_password)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_createNurse', (_username, password, _first, _last, _street, _city,
                        _state, _zip, _phone, _dob, _sex, _email, _classification, _deptId, _clinicId))
        data = cursor.fetchall()

        if len(data) == 0:
            conn.commit()
            return redirect('/adminHome')
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
            return redirect('/adminHome')
        else:
            return json.dumps({'error': data})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route('/api/addBed', methods=['POST'])
def addBed():
    idbed = request.form['idBed']
    idclinic = request.form['idClinic']
    room_number = request.form['roomNum']
    occupancy_status = request.form['status']
    idpatient = request.form['idPatient']

    if all((idbed, idclinic, room_number, occupancy_status, idpatient)):

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_addBeds', (idbed, idclinic,
                        room_number, occupancy_status, idpatient))
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
    idbed = request.form['idBed']

    if all((idbed)):

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_deleteBeds', (idbed,))
        data = cursor.fetchall()

        if len(data) == 0:
            conn.commit()
            return redirect('/ManageBeds')
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route('/api/assignBed', methods=['POST'])
def assignBed():
    idbed = request.form['idBed']
    idpatient = request.form['idpatient']

    if all((idbed, idpatient)):

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_assignBed', (idbed, idpatient))
        data = cursor.fetchall()

        if len(data) == 0:
            conn.commit()
            return redirect('/seePhysSchedule')
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


# for testing purposes only
###############################
def deleteUser(username):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_deleteUser', (username,))
    conn.commit()


def createPhysician(uname, pwd, fname, lname, st, city, state, zip, ph, dob, s, e, spec, rank, dID, cID):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_createPhysician', (uname, pwd, fname, lname,
                    st, city, state, zip, ph, dob, s, e, spec, rank, dID, cID,))
    conn.commit()


def deleteSchedule(pid):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_deleteSchedule', (pid,))
    conn.commit()
###############################


if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True)
