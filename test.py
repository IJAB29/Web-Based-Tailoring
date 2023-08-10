from datetime import datetime
# # import main Flask class and request object
# from flask import Flask, request, render_template
#
# # create the Flask app
# app = Flask(__name__)
#
#
# # allow both GET and POST requests
# @app.route('/form-example', methods=['GET', 'POST'])
# def form_example():
#     # handle the POST request
#     if request.method == 'POST':
#         language = request.form.get('language')
#         framework = request.form.get('framework')
#         return render_template("post_ex.html").format(language, framework)
#
#     # otherwise handle the GET request
#     return render_template("get_ex.html")
#
#
# if __name__ == '__main__':
#     # run app in debug mode on port 5000
#     app.run(debug=True, port=5000)

# import mysql.connector
#
# order = {"jayvhik": {"height": 150, "weight": 100, "age": 15}}
# items = [{"product": "tshirt", "waist": 100, "shoulder": 100, "arm": 100}]
print(datetime.now().date())
"""
SELECT orders_info_tbl.user_order_id, orders_info_tbl.order_date, user_tbl.first_name, user_tbl.middle_name, user_tbl.last_name, user_tbl.contact_info, user_tbl.address, shirts_order_tbl.shirt_chest, shirts_order_tbl.shirt_waist, shirts_order_tbl.shirt_shoulder, shirts_order_tbl.shirt_arm, shirts_order_tbl.shirt_orders, slacks_order_tbl.slacks_hip, slacks_order_tbl.slacks_waist, slacks_order_tbl.slacks_leg, slacks_order_tbl.slacks_pundijuhan, slacks_order_tbl.slacks_orders, skirts_order_tbl.skirt_hip, skirts_order_tbl.skirt_waist, skirts_order_tbl.skirt_length, skirts_order_tbl.skirt_orders
FROM orders_info_tbl 
INNER JOIN user_tbl ON orders_info_tbl.user_id = user_tbl.user_id 
INNER JOIN shirts_order_tbl ON shirts_order_tbl.user_id = user_tbl.user_id 
INNER JOIN slacks_order_tbl ON slacks_order_tbl.user_id = user_tbl.user_id
INNER JOIN skirts_order_tbl ON skirts_order_tbl.user_id = user_tbl.user_id;
"""