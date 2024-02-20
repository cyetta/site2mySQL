#!/usr/bin/env python3
import site_parser
import mysql.connector
from sqlalchemy import create_engine


# Function search given table on site and write it
# to mysql database test, table test
def site_table_to_db(site_url, table_class_name):
    try:
        df = site_parser.print_table(site_url, table_class_name)
    except Exception as e:
        print(f'{e}')
        raise
# Create a SQLAlchemy engine to connect to the MySQL database
    mydb = create_engine("mysql+mysqlconnector://test:test@localhost/test")

# Convert the Pandas DataFrame to a format for MySQL table test insertion
    df.to_sql('test', con=mydb, if_exists='replace', index=False)
    return


site_table_to_db(
    'https://www.w3schools.com/html/html_tables.asp', 'ws-table-all')

print("\nDB control reading...")
# Reading table 'test'
mydb = mysql.connector.connect(
    host="localhost",
    user="test",
    password="test",
    database="test"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM test")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
