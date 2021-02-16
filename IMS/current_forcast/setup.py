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
mycursor.execute("CREATE DATABASE IMS")

#to crate a table in the DB
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE weather (datetime VARCHAR(255) , PRIMARY KEY(`datetime`) , Rain VARCHAR(255) , WSmax VARCHAR(255) , WDmax VARCHAR(255) , WS VARCHAR(255) , WD VARCHAR(255) , STDwd VARCHAR(255) , TD VARCHAR(255) , TW VARCHAR(255) , TDmax VARCHAR(255) , TDmin VARCHAR(255) , WS1mm VARCHAR(255) , Ws10mm VARCHAR(255) , Time VARCHAR(255) , TG VARCHAR(255) , RH VARCHAR(255))")


# mycursor.execute("SELECT * FROM weather")

# for x in mycursor:
#   print(x)
