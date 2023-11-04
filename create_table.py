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
            CREATE TABLE STUDENT(
                ROLL VARCHAR(5),
                NAME VARCHAR(30)
            )

            """


mycursor.execute(sqlquery)

