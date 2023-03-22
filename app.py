from flask import Flask, render_template, request, json, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flaskext.mysql import MySQL

from datetime import datetime
import sys

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'PepeSilvia1259#12!'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['SECRET_KEY'] = '1234567890'
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
    appt_lengths = [15, 30, 60, 120, 240]
    return render_template('setHours.html', days=days, appt_lengths=appt_lengths)


@app.route('/api/setHours', methods=['POST'])
def setHours():
    _mon = request.form['Monday']
    _tue = request.form['Tuesday']
    _wed = request.form['Wednesday']
    _thurs = request.form['Thursday']
    _fri = request.form['Friday']
    _sat = request.form['Saturday']
    _sun = request.form['Sunday']
    _pid = request.form["idphysician"]
    _monTL = ''
    _tueTL = ''
    _wedTL = ''
    _thursTL = ''
    _friTL = ''
    _satTL = ''
    _sunTL = ''

    if request.form["MondayTimes"] is not None:
        _monTL = request.form["MondayTimes"]
    if request.form["TuesdayTimes"] is not None:
        _tueTL = request.form["TuesdayTimes"]
    if request.form["WednesdayTimes"] is not None:
        _wedTL = request.form["WednesdayTimes"]
    if request.form["ThursdayTimes"] is not None:
        _thursTL = request.form["ThursdayTimes"]
    if request.form["FridayTimes"] is not None:
        _friTL = request.form["FridayTimes"]
    if request.form["SaturdayTimes"] is not None:
        _satTL = request.form["SaturdayTimes"]
    if request.form["SundayTimes"] is not None:
        _sunTL = request.form["SundayTimes"]

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_setHours',
                    (_pid, int(_mon), int(_tue), int(_wed), int(_thurs), int(_fri), int(_sat), int(_sun), _monTL, _tueTL, _wedTL, _thursTL, _friTL, _satTL, _sunTL))
    data = cursor.fetchall()
    if len(data) == 0:
        conn.commit()
        return json.dumps({'message': 'Hours add successfully!'})
    else:
        return json.dumps({'error': str(data[0])})


@app.route('/appointment')
def showAppointment():
    return render_template('appointment.html')


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


@app.route('/userHome')
def userHome():
    if session.get('user'):
        return render_template('userHome.html')
    else:
        return render_template('error.html',error = 'Unauthorized Access')

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
        cursor.callproc('sp_changePassword', (_username, _newPassword))
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

@app.route('/api/validateLogin', methods=['POST', 'GET'])
def validateLogin():
    _username = request.form['inputUsername']
    _password = request.form['inputPassword']

    con = mysql.connect()
    cursor = con.cursor()
    cursor.callproc('sp_validateLogin',(_username,_password))
    data = cursor.fetchall()

    if len(data) > 0:
        session['user'] = data[0][0]
        return redirect('/userHome')
    else:
        return render_template('error.html', error='Wrong Email address or Password')


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
    
    if all( (_username,_password,_first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email)):
        
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_createUser', (_username, _password,_first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email))
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
    _type= request.form['Type']
    _spec= request.form['Specialization']
    _rank= request.form['Rank']
    _deptId= request.form['DepartmentID']
    _clinicId= request.form['ClinicID']

    if all( (_username,_password,_first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email,_type,_spec,_rank,_deptId,_clinicId)):
        
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_createPhysician', (_username, _password,_first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email,_type,_spec,_rank,_deptId,_clinicId))
        data = cursor.fetchall()

        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'Physician created successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route('/api/addBed', methods=['POST'])
def addBed():
    idbed= request.form['idBed']
    idclinic= request.form['idClinic']
    room_number= request.form['roomNum']
    occupancy_status= request.form['status']
    idpatient= request.form['idPatien']
    
    
    if all( (idbed,idclinic,room_number,occupancy_status,idpatient)):
        
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_addBeds', (idbed,idclinic,room_number,occupancy_status,idpatient))
        data = cursor.fetchall()

        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'Bed created successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


if __name__ == '__main__':
    app.run(debug=True)
