from remove_config import DAYS_COUNT_BACK, table_names
import mysql.connector
from datetime import datetime, timedelta

N = DAYS_COUNT_BACK

date_N_days_ago = datetime.now() - timedelta(days=N)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="shilo",
  database="IMS"
)
mycursor = mydb.cursor()
for table, column in table_names.items():
    mycursor.execute(
        """
            delete
            from %s p1
            where STRCMP(%s, p1.%s) == 1
        """,
        (table, date_N_days_ago.strftime('%Y-%m-%d'), column,)
    )
mydb.commit()
