import re

from flask import Flask, render_template, request, json, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flaskext.mysql import MySQL

app = Flask(__name__)


import logging
app.logger.setLevel(logging.DEBUG)

mysql = MySQL()


def connect_to_db(app):
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'Gooster1225!2'
    app.config['MYSQL_DATABASE_DB'] = 'test'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    app.config['SECRET_KEY'] = '1234567890'
    app.config['DEBUG'] = True
    mysql.app = app
    mysql.init_app(app)


@app.route('/')
def main(first='', last='', email='', message='', error='', success=''):
    return render_template('homepage.html', first=first, last=last, email=email, message=message, error=error, success=success)


@app.route('/signup')
def showSignUp(username='', password='', first='', last='', street='', city='', state='', zip='', phone='', dob='', sex='', email='', errors=[]):
    return render_template('signup.html', username=username, password=password, first=first, last=last, street=street, city=city, state=state, zip=zip, phone=phone, dob=dob, sex=sex, email=email, errors=errors)


@app.route('/api/contacted', methods=['POST'])
def showContacted():
    error=''
    _fname = request.form['fname']
    _lname = request.form['lname']
    _email = request.form['email']
    _message = request.form['message']

    if not bool(re.match(r"^\S+@\S+\.\S+$", _email)):
        error="Email not in correct example@email.com format"

    if error != '':
        return main(_fname, _lname, _email, _message, error, '')
    else:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_addContactUsMessage',
                        (_fname, _lname, _email, _message))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return main('','','','','','Message sent successfully!')



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
def showSetHours(errors=[], mon='', tue='', wed='', thurs='', fri='', sat='', sun='', physician='choose'):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    p_names = getPhysiciansByNameAndId().keys()
    schedules = getPhysicianSchedules()
    return render_template('setHours.html', days=days, p_names=p_names, schedules=schedules, errors=errors, mon=mon, tue=tue, wed=wed, thurs=thurs, fri=fri, sat=sat, sun=sun, physician=physician)


@app.route('/ownSchedule')
def ownSchedule():
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    p_names = getPhysiciansByNameAndId().keys()
    schedules = getPhysicianSchedulesById()
    return render_template('ownSchedule.html', days=days, p_names=p_names, schedules=schedules)


@app.route('/api/setHours', methods=['POST'])
def setHours():
    errors = []
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    times = [request.form["MondayTimes"], request.form["TuesdayTimes"], request.form["WednesdayTimes"],
             request.form["ThursdayTimes"], request.form["FridayTimes"], request.form["SaturdayTimes"],
             request.form["SundayTimes"]]
    for i in range(7):
        if times[i] != '':
            if not bool(re.match(
                    r"[0|1]\d:[012345]\d\s((PM)|(AM))-[0|1]\d:[012345]\d\s(P|A)M(,\s[0|1]\d:[012345]\d\s(P|A)M-[0|1]\d:[012345]\d\s(P|A)M)*",
                    times[i])):
                errors.append("Time format is incorrect for " + days[i])

    if len(errors) != 0 or request.form["physician"] == 'choose':
        return showSetHours(errors, times[0], times[1], times[2], times[3], times[4], times[5], times[6], request.form["physician"])
    else:

        _pid = getPhysiciansByIdUsingName(request.form["physician"])

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_setHours',
                        (
                            int(_pid), times[0],
                            times[1], times[2], times[3], times[4], times[5], times[6]))
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
        for time in tup[1:]:
            individual.append(time)
        formatted.append(individual)

    return formatted


def getPhysicianNameByID(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_getPhysicianNameByID', (id,))
    data = cursor.fetchall()
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
        individual = [appointment[0], appointment[1], appointment[2], appointment[3], appointment[4]]
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
def showStatement(errors=[], payment=0, statementid='', success=''):
    if statementid == '':
        statementid = request.args.get(('statement_id'))
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_getInvoices', (statementid,))
    invoices = cursor.fetchall()
    outstanding_balance = None
    statements = getStatements()
    cursor.callproc('sp_paymentHistory', (session["user"], statementid,))
    history = cursor.fetchall()[::-1]
    newHistory = [[h[1],h[2]] for h in history if h[2] > 0]
    for s in statements:
        if str(s[0]) == str(statementid):
            outstanding_balance = s[2]
    return render_template('statement.html', invoices=invoices, outBal=outstanding_balance, id=statementid, history=newHistory, errors=errors, payment=payment, success=success)

@app.route('/makePayment', methods=["POST"])
def makePayment():
    statements = getStatements()
    statement_id = request.form["statementID"]
    statement_balance = None
    for s in statements:
        if str(s[0]) == str(statement_id):
            statement_balance = s[2]
    errors = []
    payment = request.form["amount"]
    try:
        payment = int(payment)
    except:
        return showStatement(["Payment not in correct format"], payment, statement_id)

    if type(payment) != int:
        payment = 0
    if payment <= 0:
        errors.append("Please input a payment amount greater than 0.")
    elif payment > statement_balance:
        errors.append("You cannot pay more than your outstanding balance.")

    if errors:
        return showStatement(errors, payment, statement_id, '')
    else:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_updateStatementBalance', (str(session['user']), request.form["amount"], statement_id,))
        conn.commit()
        return showStatement(errors, 0, statement_id,'Payment recieved successfully!')

@app.route('/appointment')
def showAppointment():
    user_appointments = getAppointments()
    for appointment in user_appointments:
        appointment[3] = getPhysicianNameByID(appointment[3])
    return render_template('appointment.html', appointments=user_appointments)


@app.route('/createAppointment')
def showScheduleAppointment():
    p_names = getPhysiciansByNameAndId().keys()
    return render_template('createAppointment.html', p_names=p_names)


@app.route('/login')
def showLogin(error=''):
    return render_template('login.html', error=error)


@app.route('/loginBilling')
def showLoginBilling(error=''):
    return render_template('loginBilling.html', error=error)


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

    _date = request.form['inputDate'] + " " + request.form['inputTime']
    _physician = getPhysiciansByIdUsingName(request.form["physician"])
    _patient = session['user']
    _reason = request.form['inputReason']

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_createAppointment', (_date, int(_physician), int(_patient), _reason))
    data = cursor.fetchall()

    if len(data) == 1:
        conn.commit()
        return redirect('/appointment?appointment_id=' + str(data[0][0]))
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
    selected = [selected[0], date, time, selected[2], selected[3], selected[4]]
    appointments = [appointment for appointment in appointments if appointment[0] != _appointmentID]
    for appointment in appointments:
        appointment[2] = getPhysicianNameByID(appointment[2])
    selected_phys = getPhysicianNameByID(selected[4])
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
            return showLogin('Wrong Email address or Password')

@app.route('/api/validateLoginBilling', methods=['POST', 'GET'])
def validateLoginBilling():
    _username = request.form['inputUsername']
    _password = request.form['inputPassword']

    con = mysql.connect()
    cursor = con.cursor()
    cursor.callproc('sp_validateLogin', (_username,))
    data = cursor.fetchall()

    if len(data) > 0:
        if check_password_hash(str(data[0][2]), _password):
            session['user'] = data[0][0]
            if data[0][13] == "user":
                return redirect('/billing')
        else:
            return showLogin('Wrong Email address or Password')

userHeadings = ("First Name", "Last Name", "Street", "City",
                "State", "Zip", "Phone Number", "DOB", "Sex", "Email")


@app.route('/userHome')
def userHome():
    conn = mysql.connect()
    cursor = conn.cursor()
    id = session['user']
    cursor.callproc('sp_getUser', (id,))
    data = cursor.fetchall()
    return render_template('userhome.html', headings=userHeadings, data=data[0])


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
    errors = []
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
    if not bool(re.match(r"^\d{2}/\d{2}/\d{4}$", _dob)):
        errors.append("DOB is not in MM/DD/YYYY format")

    if not bool(re.match("^\d{3}-\d{3}-\d{4}$", _phone)):
        errors.append("Phone number is not in XXX-XXX-XXXX format")

    if len(_zip) != 5:
        errors.append("Invalid zipcode")

    if _sex not in ['M', 'F', 'Other']:
        errors.append("Gender must be one of the following: M, F, Other")

    numCapitals = sum([1 for ch in _password if ch.isupper()])
    numNumbers = sum([1 for ch in _password if ch.isdigit()])
    specialChar = sum([1 for ch in _password if ch in "!?$"])
    if numCapitals == 0 or numNumbers == 0 or specialChar == 0 or len(_password)<8:
        errors.append("Password must contain at least: 1 number, 1 capital letter, 1 special character (!?$) and be at least 8 characters long")

    if not bool(re.match(r"^\S+@\S+\.\S+$", _email)):
        errors.append("Email not in correct example@email.com format")

    if errors:
        return showSignUp(_username, _password, _first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email, errors)
    else:
        password = generate_password_hash(_password)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_createUser',
                        (_username, password, _first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email))
        data = cursor.fetchall()

        if str(data[0])!='(\'Username exists!!\',)':
            conn.commit()
            session['user'] = data[0][0]
            return redirect('/userHome')
        elif str(data[0])=='(\'Username exists!!\',)':
            errors.append("Username already exists!")
            # json.dumps({'error': str(data[1])})
            return showSignUp(_username, _password, _first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email, errors)

@app.route('/signupPhysician')
def showSignUpPhysician(username='', pwd='', first='', last='', street='', city='', state='', zip='', phone='', dob='', sex='', email='', spec='', rank='', dID='', cID='', errors=''):
    return render_template('createPhysician.html', username=username, password=pwd, first=first, last=last, street=street, city=city, state=state, zip=zip, phone=phone, dob=dob, sex=sex, email=email, spec=spec, rank=rank, dID=dID, cID=cID, errors=errors)

@app.route('/api/signupPhysician', methods=['POST'])
def signupPhysician():
    errors = []
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
    _spec = request.form['inputSpec']
    _rank = request.form['inputRank']
    _deptId = request.form['inputDept']
    _clinicId = request.form['inputClinic']

    if not bool(re.match(r"^\d{2}/\d{2}/\d{4}$", _dob)):
        errors.append("DOB is not in MM/DD/YYYY format")

    if not bool(re.match("^\d{3}-\d{3}-\d{4}$", _phone)):
        errors.append("Phone number is not in XXX-XXX-XXXX format")

    if len(_zip) != 5:
        errors.append("Invalid zipcode")

    if _sex not in ['M', 'F', 'Other']:
        errors.append("Gender must be one of the following: M, F, Other")

    numCapitals = sum([1 for ch in _password if ch.isupper()])
    numNumbers = sum([1 for ch in _password if ch.isdigit()])
    specialChar = sum([1 for ch in _password if ch in "!?$"])
    if numCapitals == 0 or numNumbers == 0 or specialChar == 0 or len(_password)<8:
        errors.append("Password must contain at least: 1 number, 1 capital letter, 1 special character (!?$) and be at least 8 characters long")

    if not bool(re.match(r"^\S+@\S+\.\S+$", _email)):
        errors.append("Email not in correct example@email.com format")

    try:
        int(_deptId)
    except:
        errors.append("Dept ID must be a number")

    try:
        int(_clinicId)
    except:
        errors.append("Clinic ID must be a number")

    if errors:
        return showSignUpPhysician(_username, _password, _first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email, _spec,_rank, _deptId, _clinicId, errors)

    else:
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
            errors.append("Username already exists!")
            # json.dumps({'error': str(data[0])})
            return showSignUpPhysician(_username, _password, _first, _last, _street, _city, _state, _zip, _phone, _dob,
                                       _sex, _email, _spec, _rank, _deptId, _clinicId, errors)

@app.route('/signupNurse')
def showSignUpNurse(username='', password='', first='', last='', street='', city='', state='', zip='', phone='', dob='',
                                       sex='', email='', classification='', deptId='', clinicId='', errors=[]):
    return render_template('createNurse.html', username=username, password=password, first=first, last=last, street=street, city=city, state=state, zip=zip, phone=phone, dob=dob,
                                       sex=sex, email=email, classification=classification , deptId=deptId, clinicId=clinicId, errors=errors)


@app.route('/api/signupNurse', methods=['POST'])
def signupNurse():
    errors = []
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
    _classification = request.form['inputClassification']
    _deptId = request.form['inputDept']
    _clinicId = request.form['inputClinic']

    if not bool(re.match(r"^\d{2}/\d{2}/\d{4}$", _dob)):
        errors.append("DOB is not in MM/DD/YYYY format")

    if not bool(re.match("^\d{3}-\d{3}-\d{4}$", _phone)):
        errors.append("Phone number is not in XXX-XXX-XXXX format")

    if len(_zip) != 5:
        errors.append("Invalid zipcode")

    if _sex not in ['M', 'F', 'Other']:
        errors.append("Gender must be one of the following: M, F, Other")

    numCapitals = sum([1 for ch in _password if ch.isupper()])
    numNumbers = sum([1 for ch in _password if ch.isdigit()])
    specialChar = sum([1 for ch in _password if ch in "!?$"])
    if numCapitals == 0 or numNumbers == 0 or specialChar == 0 or len(_password)<8:
        errors.append("Password must contain at least: 1 number, 1 capital letter, 1 special character (!?$) and be at least 8 characters long")

    if not bool(re.match(r"^\S+@\S+\.\S+$", _email)):
        errors.append("Email not in correct example@email.com format")

    try:
        int(_deptId)
    except:
        errors.append("Dept ID must be a number")

    try:
        int(_clinicId)
    except:
        errors.append("Clinic ID must be a number")

    if errors:
        return showSignUpNurse(_username, _password, _first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email, _classification, _deptId, _clinicId, errors)

    else:
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
            errors.append("Username already exists!")
            # json.dumps({'error': str(data[0])})
            return showSignUpNurse(_username, _password, _first, _last, _street, _city, _state, _zip, _phone, _dob,
                                   _sex, _email, _classification, _deptId, _clinicId, errors)

@app.route('/signupAdmin')
def showSignUpAdmin(username='', pwd='', first='', last='', street='', city='', state='', zip='', phone='', dob='', sex='', email='', dID='', errors=''):
    return render_template("createAdmin.html", username=username, password=pwd, first=first, last=last, street=street, city=city, state=state, zip=zip, phone=phone, dob=dob, sex=sex, email=email, dID=dID, errors=errors)

@app.route('/api/signupAdmin', methods=['POST'])
def signupAmin():
    errors = []
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
    _deptId = int(request.form['inputDept'])

    if not bool(re.match(r"^\d{2}/\d{2}/\d{4}$", _dob)):
        errors.append("DOB is not in MM/DD/YYYY format")

    if not bool(re.match("^\d{3}-\d{3}-\d{4}$", _phone)):
        errors.append("Phone number is not in XXX-XXX-XXXX format")

    if len(_zip) != 5:
        errors.append("Invalid zipcode")

    if _sex not in ['M', 'F', 'Other']:
        errors.append("Gender must be one of the following: M, F, Other")

    numCapitals = sum([1 for ch in _password if ch.isupper()])
    numNumbers = sum([1 for ch in _password if ch.isdigit()])
    specialChar = sum([1 for ch in _password if ch in "!?$"])
    if numCapitals == 0 or numNumbers == 0 or specialChar == 0 or len(_password)<8:
        errors.append("Password must contain at least: 1 number, 1 capital letter, 1 special character (!?$) and be at least 8 characters long")

    if '@' not in _email or '.' not in _email:
        errors.append("Email is not in email@example.com format")

    try:
        int(_deptId)
    except:
        errors.append("Dept ID must be a number")

    if errors:
        return showSignUpAdmin(_username, _password, _first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email, _deptId, errors)

    else:
        password = generate_password_hash(_password)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_createAdmin', (
            _username, password, _first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email,
            _deptId))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return redirect('/adminHome')
        else:
            errors.append("Username already exists!")
            # json.dumps({'error': str(data[0])})
            return showSignUpAdmin(_username, _password, _first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email, _deptId, errors)

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

@app.route('/createBill')
def showCreateBill(patients=[], rates=[], errors=[], success='', chosenPat="", chosenItems={}, default={}):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_getBillRates')
    rates = cursor.fetchall()
    conn.commit()
    cursor.callproc('sp_getPatientsFromAppt')
    patients = ['--choose a patient--']
    patients.extend([el[1]+' '+el[2]+', '+str(el[0]) for el in cursor.fetchall()])
    l = ['--choose billing item--']
    l.extend([desc+", $"+str(charge) for desc, charge in rates])
    return render_template('createBills.html',patients=patients, rates=l, errors=errors, success=success, cp=chosenPat, items=chosenItems, default={})

@app.route('/api/createBill', methods=["POST"])
def createBillAdmin():
    # get value of hidden var to determine num of invoice
    errors = []
    invoiceCount = int(request.form["total_chq"])
    patient = request.form['patient']
    if patient == "--choose a patient--":
        errors.append("You need to select a patient.")

    invoiceValues = {}
    default = {}
    for i in range(1, invoiceCount+1):
        invoice = request.form["new_"+str(i)]
        if i == 1:
            default[i] = invoice
        invoiceValues[str(i)]=invoice
        if invoice == "--choose billing item--":
            errors.append("Select a billing item")

    if errors:
        return showCreateBill([patient], [], errors, '', request.form['patient'], invoiceValues, default)
    else:
        pid = int(patient[patient.index(',')+1:].strip())
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_getBillRates')
        rates = cursor.fetchall()
        cursor.callproc('sp_createStatement',(pid, 0, '06/30/2023',))
        statementID = cursor.fetchall()
        if len(statementID) == 1:
            # get patient insurance info
            cursor.callproc('sp_getPatientInsuranceInfo', (pid,))
            insuranceInfo = cursor.fetchall()
            name, discount, copay = insuranceInfo[0][0], float(insuranceInfo[0][1]), int(insuranceInfo[0][2])
            if len(insuranceInfo) > 0:
                for i in range(1,invoiceCount+1):
                    invoice = request.form['new_'+str(i)]
                    desc = invoice[:invoice.index(',')]
                    charge = int(invoice[invoice.index('$')+1:].strip())
                    cursor.callproc('sp_createInvoice', (statementID[0], charge, int(charge*discount), charge-(int(charge*discount)), desc))
                    cursor.fetchall()
                    conn.commit()
                # notif to patient
            return showCreateBill([],[],[],'Bill created and patient has been notified!', "", [])


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

def createStatement(patientID, balance, due_date):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_createStatement', (patientID, balance, due_date,))
    conn.commit()

def deleteStatement(statementID, patientID):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_deleteStatement', (statementID, patientID))
    conn.commit()

def createInvoice(statementID, date, charge, insurance, total, desc):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_createInvoice', (statementID, date, charge, insurance, total, desc,))
    conn.commit()

def deleteInvoice(statementid):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_getInvoices', (statementid,))
    invoices = cursor.fetchall()
    for inID, sid, date, charge, insurance, total, des in invoices:
        cursor.callproc('sp_deleteInvoice', (inID,))
        conn.commit()

def getStatementId(patientID, date):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_getStatements', (patientID,))
    statements = cursor.fetchall()
    for sid, pid, balance, duedate, paid in statements:
        if date == duedate:
            return sid

def deletePaymentHistory(statementID, userid):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_deletePaymentHistory', (userid,statementID,))
    conn.commit()

def deleteCUMessage(fname, lname, email, message):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_getCUMessageID', (fname, lname, email, message,))
    messageID = cursor.fetchall()[0]
    cursor.callproc('sp_deleteCUMessage', (messageID,))
    conn.commit()

###############################


if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True)
