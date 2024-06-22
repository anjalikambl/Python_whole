#import a library
import mysql.connector

#step1 call connect method and create an object of method
x=mysql.connector.connect(host='localhost',
               user='root',
               password='Kamble@123',
               database='python_test_db')
if x:
    print('Successfully established connection')
else:
    print('Please try again')
#step2:call user 
y=x.cursor()
#step3 :execute sql queries by using cursor object
y.execute("create table if not exists empdata(emp_name text,emp_skill text)")
y.execute("insert into empdata(emp_name,emp_skill) values ('Nikhil','Cyber Security')")
y.execute('select*from empdata')
data=y.fetchall()
print(data)