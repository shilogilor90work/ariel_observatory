import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="shilo",
#   database="IMS"
# )


# to crate a DB
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="shilo",
)
mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE DATABASE IMS")

#to crate a table in the DB
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE weekly_weather (forecast_time VARCHAR(255) , PRIMARY KEY(`forecast_time`) , weather_code VARCHAR(255) , weather VARCHAR(255) , temperature VARCHAR(255)")


# mycursor.execute("SELECT * FROM weather")

# for x in mycursor:
#   print(x)
