from remove_config import DAYS_COUNT_BACK, table_names
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="shilo",
  database="IMS"
)
mycursor = mydb.cursor()
for table, column in table_names.items():
    string = "delete from " + table + " where STR_TO_DATE(LEFT(" + column + " , 10), '%Y-%m-%d') > CURDATE() - INTERVAL " + str(DAYS_COUNT_BACK) + " DAY"
    mycursor.execute(string)
mydb.commit()
