import json
import psycopg2
from flask import Flask, request
from routes.events import *
from flask_cors import CORS


app = Flask(__name__)
CORS(app1)
app.register_blueprint(app1)


if __name__ == "__main__":
    app.run(debug=True)




# events = [{'id': 1, 'name': 'Intro to Hacking', 'time': '12:00PM'},
#           {'id': 2, 'name': 'Github ke basics', 'time': '1:00PM'}]
# params = {
#     'dbname': 'ecslokmm',
#     'user': 'ecslokmm',
#     'password': 'LIz9iRuz0vI8f9_8CifdGvm7YEdkRhzE',
#     'host': 'john.db.elephantsql.com',
# }
# print(events[0])

# @app.route('/events/<a>')
# def hello_world(a):

#     for i in events:
#         if i['id'] == int(a):
#             return json.dumps(i)
#     return "Not found!"


# @app.route('/home')
# def home():
#     conn = psycopg2.connect(**params)
#     cmd = """
#         CREATE TABLE vendors (
#             vendor_id SERIAL PRIMARY KEY,
#             vendor_name VARCHAR(255) NOT NULL
#         )
#         """
#     cur = conn.cursor()
#     cur.execute(cmd)
#     cur.close()
#     conn.commit()
#     return "IDHAR TAK AGAYA MATLAB CHAL GAYA"


# def func(x):
#     for a in x:
#         print(x)


# y = [0, 1, 2, 3]

# b = filter(func, y)
