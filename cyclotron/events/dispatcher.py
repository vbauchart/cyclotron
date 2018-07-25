import json


class Event(object):
    def __init__(self, message):
        self.message = message
        self.files = []

    def __str__(self):
        return json.dumps({'message': self.message})


class EventDispatcher(object):
    class __EventDispatcherSingleton(object):
        def __init__(self):
            self.dispatchers = []

        def __str__(self):
            return '%s' % self.dispatchers

    instance = None

    def __new__(c):
        if c.instance is None:
            c.instance = super(EventDispatcher, c).__new__(c)
        return c.instance

    def __init__(self):
        self.dispatchers = []

    def add_dispatcher(self, dispatcher):
        self.instance.dispatchers.append(dispatcher)

    def log_event(self, event):
        for dispatcher in self.instance.dispatchers:
            dispatcher.log_event(event)


class DummyDispatcher(object):
    def log_event(self, event):

        if isinstance(event, Event):
            msg = event
        else:
            msg = Event(event)

        print(msg)
