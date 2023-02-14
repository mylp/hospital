
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PepeSilvia1259#12!",
    database="test"
)

try:
    cursor = mydb.cursor()
    mydb.autocommit = True
except:
    print("Error connecting to database")

def main():
    cursor.callproc('get_hospitals')
    for result in cursor.stored_results():
        print(result.fetchall())

if __name__ == '__main__':
    main()