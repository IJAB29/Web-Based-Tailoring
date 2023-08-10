from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os
import ast
from datetime import datetime

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = os.environ["USER"]
app.config["MYSQL_PASSWORD"] = os.environ["PASS"]
app.config["MYSQL_DB"] = os.environ["DB"]

mysql = MySQL(app)


class StoreInfo:
    def __init__(self, req):
        self.skirt_id = None
        self.slacks_id = None
        self.shirt_id = None
        self.customer_id = None
        info = req.form
        self.first_name = info["firstName"]
        self.middle_name = info["middleName"]
        self.last_name = info["lastName"]
        self.contact_info = info["contactInfo"]
        self.address = info["address"]

        self.shirt_chest = info["shirtChestVal"]
        self.shirt_waist = info["shirtWaistVal"]
        self.shirt_shoulder = info["shirtShoulderVal"]
        self.shirt_arm = info["shirtArmVal"]
        self.shirt_orders = info["shirtOrdersVal"]
        self.shirt_design = info["shirtDesignVal"]

        self.slacks_hip = info["slacksHipVal"]
        self.slacks_waist = info["slacksWaistVal"]
        self.slacks_leg = info["slacksLegVal"]
        self.slacks_pundijuhan = info["slacksPundijuhanVal"]
        self.slacks_orders = info["slacksOrdersVal"]
        self.slacks_design = info["slacksDesignVal"]

        self.skirt_hip = info["skirtsHipVal"]
        self.skirt_waist = info["skirtsWaistVal"]
        self.skirt_length = info["skirtsLengthVal"]
        self.skirt_orders = info["skirtsOrdersVal"]
        self.skirt_design = info["skirtDesignVal"]

    def store_customer_info(self):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO users_tbl(user_id, first_name, middle_name, last_name, contact_info, address) "
            "VALUES (%s,%s,%s,%s,%s,%s)",
            (self.customer_id, self.first_name, self.middle_name, self.last_name, self.contact_info, self.address)
        )
        customer_id = cursor.lastrowid
        mysql.connection.commit()
        cursor.close()
        return customer_id

    def store_shirt_orders(self):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO shirts_order_tbl(user_id, shirt_chest, shirt_waist, shirt_shoulder, shirt_arm, shirt_orders, shirt_design) "
            "VALUES (%s,%s,%s,%s,%s,%s,LOAD_FILE(%s))",
            (self.customer_id, self.shirt_chest, self.shirt_waist, self.shirt_shoulder, self.shirt_arm, self.shirt_orders, self.shirt_design)
        )
        shirt_id = cursor.lastrowid
        mysql.connection.commit()
        cursor.close()
        return shirt_id

    def store_slacks_orders(self):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO slacks_order_tbl(user_id, slacks_hip, slacks_waist, slacks_leg, slacks_pundijuhan, slacks_orders, slacks_design) "
            "VALUES (%s,%s,%s,%s,%s,%s,LOAD_FILE(%s))",
            (self.customer_id, self.slacks_hip, self.slacks_waist, self.slacks_leg, self.slacks_pundijuhan, self.slacks_orders, self.slacks_design)
        )
        slacks_id = cursor.lastrowid
        mysql.connection.commit()
        cursor.close()
        return slacks_id

    def store_skirt_orders(self):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO skirts_order_tbl(skirt_hip, skirt_waist, skirt_length, skirt_orders, skirt_design) "
            "VALUES (%s,%s,%s,%s,LOAD_FILE(%s))",
            (self.skirt_hip, self.skirt_waist, self.skirt_length, self.skirt_orders, self.skirt_design)
        )
        skirt_id = cursor.lastrowid
        mysql.connection.commit()
        cursor.close()
        return skirt_id

    def store_order_info(self):
        cursor = mysql.connection.cursor()

        self.customer_id = self.store_customer_info()

        if self.shirt_orders:
            self.shirt_id = self.store_shirt_orders()
        if self.slacks_orders:
            self.slacks_id = self.store_slacks_orders()
        if self.skirt_orders:
            self.skirt_id = self.store_skirt_orders()
        cursor.execute(
            "INSERT INTO orders_info_tbl(user_id, shirt_order_id, slacks_order_id, skirt_order_id, order_date) "
            "VALUES (%s,%s,%s,%s,%s)",
            (self.customer_id, self.shirt_id, self.slacks_id, self.skirt_id, datetime.now().date())
        )
        mysql.connection.commit()
        cursor.close()


def get_customers():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users_tbl")
    data = cursor.fetchall()
    user_info = []
    for r in data:
        column = {
            "user_id": r[0],
            "first_name": r[1],
            "middle_name": r[2],
            "last_name": r[3],
            "contact_info": r[4],
            "address": r[5]
        }
        user_info.append(column)
    cursor.close()
    return user_info


def get_shirt_orders(customer_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM shirts_order_tbl WHERE user_id = %s", [customer_id])
    data = cursor.fetchall()
    order_info = []
    for r in data:
        column = {
            "order_id": r[0],
            "user_id": r[1],
            "chest": r[2],
            "waist": r[3],
            "shoulder": r[4],
            "arm": r[5],
            "orders": r[6],
            "design": r[7]
        }
        order_info.append(column)
    cursor.close()
    return order_info


def get_slacks_orders(customer_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM slacks_order_tbl WHERE user_id = %s", [customer_id])
    data = cursor.fetchall()
    order_info = []
    for r in data:
        column = {
            "order_id": r[0],
            "user_id": r[1],
            "hip": r[2],
            "waist": r[3],
            "leg": r[4],
            "pundijuhan": r[5],
            "orders": r[6],
            "design": r[7]
        }
        order_info.append(column)
    cursor.close()
    return order_info


def get_skirt_orders(customer_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM skirts_order_tbl WHERE user_id = %s", [customer_id])
    data = cursor.fetchall()
    order_info = []
    for r in data:
        column = {
            "order_id": r[0],
            "user_id": r[1],
            "hip": r[2],
            "waist": r[3],
            "length": r[4],
            "orders": r[5],
            "design": r[6]
        }
        order_info.append(column)
    cursor.close()
    return order_info


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        order_info = StoreInfo(request)
        order_info.store_order_info()

    # print(get_customers()[0]["first_name"])

    return render_template("info_form.html")


@app.route("/orders")
def orders():
    customer_info = get_customers()
    return render_template("orders.html",
                           customer_info=customer_info)


@app.route("/orders/<data>")
def order_details(data):
    data = ast.literal_eval(data)
    user_id = data["user_id"]
    shirt_orders = get_shirt_orders(user_id)
    slacks_orders = get_slacks_orders(user_id)
    skirt_orders = get_skirt_orders(user_id)
    return render_template("order_details.html",
                           data=data,
                           shirt_orders=shirt_orders,
                           slacks_orders=slacks_orders,
                           skirt_orders=skirt_orders)


# @app.route("/info-form", methods=["GET", "POST"])
# def info_form():
#     if request.method == "POST":
#         user_info = request.form
#         first_name = user_info["first-name"]
#         middle_name = user_info["middle-name"]
#         last_name = user_info["surname"]
#         contact_info = user_info["contact-info"]
#         address = user_info["address"]
#         product = user_info["products"]
#
#         cursor = mysql.connection.cursor()
#         cursor.execute("INSERT INTO users_tbl(first_name, middle_name, last_name, contact_info, address, product) "
#                        "VALUES (%s,%s,%s,%s,%s,%s)", (first_name, middle_name, last_name, contact_info, address,
#                                                       product))
#         mysql.connection.commit()
#         cursor.close()
#     return render_template("customer_info.html")


if __name__ == "__main__":
    app.run(debug=True)
