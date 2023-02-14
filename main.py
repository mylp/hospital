
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PepeSilvia1259#12!",
    database="test"
)

cursor = mydb.cursor()
mydb.autocommit = True

def main():
    cursor.callproc('get_hospitals')
    for result in cursor.stored_results():
        print(result.fetchall())

def main():
    cursor.callproc('get_hospitals')
    for result in cursor.stored_results():
        print(result.fetchall())
    

if __name__ == '__main__':
    main()