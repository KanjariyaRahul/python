
#checking the connection 

# import mysql.connector
# mydb = mysql.connector.connect(host='localhost', user='root', password='')
# print(mydb)

# ===============================================================================
#creating the database

# import mysql.connector
# mydb = mysql.connector.connect(host='localhost', user='root', password='')
# mycursor = mydb.cursor()
# mycursor.execute('create database python')
# print(mydb)

# ===============================================================================
#showing the list of database 

# import mysql.connector
# mydb= mysql.connector.connect(host='localhost', user='root', password = '')
# mycursor = mydb.cursor()
# mycursor.execute('show databases' ) 
# for i in mycursor : 
#     print(i)

# ===============================================================================
# creating the table 

# import mysql.connector
# mydb = mysql.connector.connect(host='localhost', user='root' , password = '', database='python')
# mycursor = mydb.cursor()
# mycursor.execute('create table stad_data (roll int primary key auto_increment, name varchar(255))')
    
# ===============================================================================
# Inserting the records into the table stud_data in the database python 

# import mysql.connector
# mydb = mysql.connector.connect(host='localhost', user='root', password = '', database='python')

# Creating a cursor object to execute SQL queries
# cursor = mydb.cursor()

# sql = 'insert into stud_data (roll , name) values (%s, %s)'
# val = [(1,'jeet'), (2,'paras')]

# Executing the insert query with multiple records
# cursor.executemany(sql,val)

# mydb.commit()
# cursor.close()
# mydb.close()

# ===============================================================================
# To display all the records  

# import mysql.connector
# mydb = mysql.connector.connect(host='localhost', user='root', password='', database= 'python')

# mycursor = mydb.cursor()

# mycursor.execute('select * from stud_data')
# myresult = mycursor.fetchall()
# for i in myresult :
#     print (i)

# ===============================================================================
# To update the record

# import mysql.connector
# mydb = mysql.connector.connect(host='localhost' , user='root', password='', database= 'python')

# mycursor = mydb.cursor()
# mycursor.execute("update stud_data set name='jeetu bhai' where roll= 3")
# mydb.commit()
# mydb.close()

# ===============================================================================
# To delete the record 

# import mysql.connector
# mydb = mysql.connector.connect(host='localhost', user='root' , password= '', database = 'python')
# mycursor = mydb.cursor()
# mycursor.execute("delete from stud_data where roll=4")

# mydb.commit()
# mydb.close()







