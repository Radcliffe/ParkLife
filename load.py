from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

import json
from models import Event
from util import utc_to_central, time_to_string

@app.route('/load')
def load():
    with open('cal.json') as f:
        events = json.load(f)
    for data in events:
        if 'RRULE' in data:  # Recurring event
            continue
        start = utc_to_central(data['DTSTART'])
        end = utc_to_central(data['DTEND'])
        date = "%d%02d%02d" % (start.year, start.month, start.day)
        start_time = time_to_string(start)
        end_time = time_to_string(end)

        event = Event(
            summary = data['SUMMARY'].strip(),
            description = data['DESCRIPTION'].strip(),
            date = date,
            start = start_time,
            end = end_time,
            location = data['LOCATION'].strip(),
            uid = data['UID'])
        event.put()
    return 'OK'
        