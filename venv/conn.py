#create the connection object
import mysql.connector
myconn=mysql.connector.connect(host="localhost",user="root",passwd="google")
print(myconn)