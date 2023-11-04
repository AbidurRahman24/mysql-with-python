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
            INSERT INTO STUDENT(ROLL,NAME)
            VALUES (%s, %s)
            val = [
  ('00003', 'Lowstreet'),
  ('00004', 'Apple st'),
  ('00005', 'Mountain')
            """


mycursor.execute(sqlquery)
mydbconnection.commit()
print("insert successfully")

