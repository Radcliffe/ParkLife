from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

from util import today
from models import Event
from google.appengine.ext import ndb
import twilio.twiml

@app.route('/message', methods=['GET', 'POST'])
def reply():
    query = Event.query(Event.date == today())
    messages = []
    for event in query:
        messages.append('%s %s (%s)' % 
                        (event.start, event.summary, event.location))
        response = twilio.twiml.Response()
        if len(messages) == 0:
            response.message('No events today')
        else:
            response.message(' | '.join(messages))
    return str(response)
