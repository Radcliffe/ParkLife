from datetime import datetime
from pytz import timezone
utc = timezone('utc')
central = timezone('US/Central')

def utc_to_central(s):
    dt = datetime.strptime(s, '%Y%m%dT%H%M%SZ')
    dt = utc.localize(dt)
    return dt.astimezone(central)

def today():
    dt = datetime.utcnow()
    dt = utc.localize(dt)
    dt = dt.astimezone(central)
    return datetime.strftime(dt, '%Y%m%d')

def time_to_string(t):
    s = str(1 + ((t.hour - 1) % 12))
    if t.minute:
        s += ':%02d' % t.minute
    if t.hour > 11:
        s += 'pm'
    else:
        s += 'am'
    return s