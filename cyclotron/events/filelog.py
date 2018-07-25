class FileLog(object):

    def __int__(self, file_path):
        self.event_file = open(file_path, mode='rw')

    def log_event(self, event):
        self.event_file.write(event)
