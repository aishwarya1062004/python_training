import mysql.connector


def insert_d(id,name,email,password):
    mydb=mysql.connector.connect(

        host="localhost",
      user="root",
        password="roottoor",
        database="raksh_cse"
    )
    mycursor=mydb.cursor()