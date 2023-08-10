import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="web_tailorDB"
)

my_cursor = db.cursor()

create_db = "CREATE DATABASE web_tailorDB"
q1 = "CREATE TABLE users_tbl (" \
     "user_id int AUTO_INCREMENT," \
     "PRIMARY KEY (user_id)," \
     "first_name VARCHAR(50), " \
     "middle_name VARCHAR(50), " \
     "last_name VARCHAR(50), " \
     "contact_info VARCHAR(50), " \
     "address VARCHAR(50))"
q2 = "CREATE TABLE shirts_order_tbl (" \
     "shirt_order_id int AUTO_INCREMENT," \
     "user_id int," \
     "PRIMARY KEY (shirt_order_id)," \
     "FOREIGN KEY (user_id) REFERENCES users_tbl(user_id)," \
     "shirt_chest FLOAT," \
     "shirt_waist FLOAT," \
     "shirt_shoulder FLOAT," \
     "shirt_arm FLOAT," \
     "shirt_orders int," \
     "shirt_design BLOB)"
q3 = "CREATE TABLE slacks_order_tbl(" \
     "slacks_order_id int AUTO_INCREMENT," \
     "user_id int," \
     "PRIMARY KEY (slacks_order_id)," \
     "FOREIGN KEY (user_id) REFERENCES users_tbl(user_id)," \
     "slacks_hip FLOAT," \
     "slacks_waist FLOAT," \
     "slacks_leg FLOAT," \
     "slacks_pundijuhan FLOAT," \
     "slacks_orders int," \
     "slacks_design BLOB)"
q4 = "CREATE TABLE skirts_order_tbl(" \
     "skirt_order_id int AUTO_INCREMENT," \
     "user_id int," \
     "PRIMARY KEY (skirt_order_id)," \
     "FOREIGN KEY (user_id) REFERENCES users_tbl(user_id)," \
     "skirt_hip FLOAT," \
     "skirt_waist FLOAT," \
     "skirt_length FLOAT," \
     "skirt_orders int," \
     "skirt_design BLOB)"
q5 = "CREATE TABLE orders_info_tbl(" \
     "user_order_id int AUTO_INCREMENT," \
     "user_id int," \
     "shirt_order_id int," \
     "slacks_order_id int," \
     "skirt_order_id int," \
     "order_date DATE," \
     "PRIMARY KEY (user_order_id)," \
     "FOREIGN KEY (user_id) REFERENCES users_tbl(user_id)," \
     "FOREIGN KEY (shirt_order_id) REFERENCES shirts_order_tbl(shirt_order_id)," \
     "FOREIGN KEY (slacks_order_id) REFERENCES slacks_order_tbl(slacks_order_id)," \
     "FOREIGN KEY (skirt_order_id) REFERENCES skirts_order_tbl(skirt_order_id))"

queries = [q1, q2, q3, q4, q5]

for q in queries:
    my_cursor.execute(q)

# test = "DROP DATABASE web_tailorDB"
# my_cursor.execute(q5)
#
# my_cursor.execute("CREATE DATABASE web_tailorDB")

for i in my_cursor:
    print(i)
