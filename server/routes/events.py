import json
from flask import Blueprint, render_template


app1 = Blueprint('events', __name__)

events = [{'id': 1, 'name': 'Intro to Hacking', 'time': '12:00PM', 'date': '02-11-2019'},
          {'id': 2, 'name': 'Github ke basics', 'time': '1:00PM', 'date': '02-11-2019'}]
@app1.route('/events') 
def about():
    return json.dumps(events)


