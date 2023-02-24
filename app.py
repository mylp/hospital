from flask import Flask, render_template, request, json
from werkzeug.security import generate_password_hash, check_password_hash
from flaskext.mysql import MySQL
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

@app.route('/login')
def showLogin():
    return render_template('login.html')

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
    app.run()
