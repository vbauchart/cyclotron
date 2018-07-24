

class EventDispatcher(object):
    def __init__(self):
        self.dispatchers = []


    def add_dispatcher(self, dispatcher):

        self.dispatchers.append(dispatcher)