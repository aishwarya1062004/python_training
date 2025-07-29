import mysql.connector


def insert_d(id,name,email,password):
    mydb=mysql.connector.connect(

        host="localhost",
        user="root",
        password="roottoor",
        database="raksh_cse"
    )
    mycursor=mydb.cursor()

    sql="insert into user(id, name, email, password) values (%s,%s,%s,%s)"

    val=(id, name, email,password)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    mydb.close()
    print(mycursor.rowcount,"record inserted.")

id=input("enter id: ")
name=input("enter name: ")
email=input("enter the email:")
password=input("enter the password: ")

insert_d(id,name,email,password)

