import mysql.connector
import mysqldb

mydb=mysql.connector.connect(host="localhost",user="venky",password="1234")

mycursor=mydb.cursor()


# mycursor.execute("show databases")
# for i in mycursor:
#     print((i))


#  mycursor.execute("select * from student")
#  for i in mycursor:
#
#   print(i)
#

# mycursor.execute("select * from student")
# result=mycursor.fetchall()
# for i in result:
#     print(i)
#
