#creating the database

import sqlite3
cnt = sqlite3.connect('mydb.dp')


# ===============================================================================
# creating the table  stud_data

# cnt.execute('CREATE TABLE stud_data (roll integer , name varchar)')
# print('table created successfully')
    
# ===============================================================================
# Inserting the records into the table stud_data 

# cnt.execute('insert into stud_data values(1,"jeetu"), (2,"rahul"), (3,"dhaval")')
# print('table inserted successfully')
# cnt.commit()


# ===============================================================================
# To display all the records  

cursor = cnt.execute('select * from stud_data')
for i in cursor:
    print(i)
                

# ===============================================================================
# To update the record

# sql_update = "update stud_data  set name='paras' where roll=1"
# cnt.execute(sql_update)
# cursor = cnt.execute('select * from stud_data')
# for i in cursor:
#     print(i)

# ===============================================================================
# To delete the record 

# sql_delete = "delete from stud_data where roll=2"

# cnt.execute(sql_delete)

# cursor = cnt.execute('select * from stud_data')
# for i in cursor:
#     print(i)
