from google.appengine.ext import ndb

class Event(ndb.Model):
    summary = ndb.StringProperty()
    description = ndb.StringProperty()
    start = ndb.StringProperty()
    end = ndb.StringProperty()
    date = ndb.StringProperty()
    location = ndb.StringProperty()
    uid = ndb.StringProperty()