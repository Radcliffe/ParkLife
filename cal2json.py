from json import JSONEncoder
import json
from datetime import datetime
from icalendar import Calendar, vDDDTypes, Event

class ICalendarEncoder(JSONEncoder):
    def default(self, obj, markers=None):

        try:
            if obj.__module__.startswith("icalendar.prop"):
                return (obj.to_ical())
        except AttributeError:
            pass

        if isinstance(obj, datetime):
            return (obj.now().strftime('%Y-%m-%dT%H:%M:%S'))

        return JSONEncoder.default(self,obj)    


cal = Calendar.from_ical(open('basic.ics','rb').read())

event_list = []
for event in cal.walk(name="VEVENT"):
    suspect = json.dumps(event, cls=ICalendarEncoder)
    working = json.loads(suspect)
    event_list.append(working)
    
with open('cal.json', 'w') as f:
    cal_js = json.dumps(event_list)
    f.write(cal_js)