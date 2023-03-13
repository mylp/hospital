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
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/signup')
def showSignUp():
    return render_template('signup.html')

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

@app.route('/api/validateLogin',methods=['POST'])
def validateLogin():
    try:
        _username = request.form['inputEmail']
        _password = request.form['inputPassword']
        # connect to mysql 
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('sp_validateLogin',(_username,))
        data = cursor.fetchall()
        if len(data) > 0:
            if check_password_hash(str(data[0][3]),_password):
                session['user'] = data[0][0]
                return redirect('/userHome')
            else:
                return render_template('error.html',error = 'Wrong Email address or Password')
        else:
            return render_template('error.html',error = 'Wrong Email address or Password')
    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        cursor.close()
        con.close()

@app.route('/api/signup', methods=['POST'])
def signUp():
    _first = request.form['inputFirst']
    # _middle = request.form['inputMiddle']
    _last = request.form['inputLast']
    _street = request.form['inputStreet']
    _city = request.form['inputCity']
    _state = request.form['inputState']
    _zip = request.form['inputZip']
    # _dropdown = request.form['dropdown']
    _phone = request.form['inputPhone']
    _dob = request.form['inputDOB']
    _sex = request.form['inputSex']
    _email = request.form['inputEmail']
    _verifyEmail = request.form['inputVerifyEmail']
    _password = request.form['inputPassword']
    _verifyPassword = request.form['inputVerifyPassword']

    if all(_first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email, _verifyEmail, _password, _verifyPassword):
        if _email != _verifyEmail:
            return json.dumps({'error': 'Emails do not match'})
        if _password != _verifyPassword:
            return json.dumps({'error': 'Passwords do not match'})
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_createUser', (_first, _last, _street, _city, _state, _zip, _phone, _dob, _sex, _email, _verifyEmail, _password, _verifyPassword))
        data = cursor.fetchall()

        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'User created successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})
    """ except:
        return json.dumps({'error':'An error occurred'})
    finally:
        cursor.close()
        conn.close() """


if __name__ == '__main__':
    app.run(debug=True)
