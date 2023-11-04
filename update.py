import mysql.connector

db_name = "python_test_db"

mydbconnection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database = db_name
)

mycursor = mydbconnection.cursor()


sqlquery = """
            update student
            set name = "AR"
            where name = "NILOY"
            """


mycursor.execute(sqlquery)
mydbconnection.commit()
print("update successfully")

