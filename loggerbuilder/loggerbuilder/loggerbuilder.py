import logging
import json
import datetime


class LogMessage:
    current = {}

    def __init__(self, logMessageBuilder):
        self.json = None
        if not isinstance(logMessageBuilder, self.LogMessageBuilder):
            return None
        self.current = str(logMessageBuilder.data)

    def toJson(self):
        self.json = json.dumps(self.current)
        return self.json

    class LogMessageBuilder:

        def __init__(self):
            self.data = {}

        def add(self, key, value):
            if value is not None:
                self.data[key] = value
            return self

        def build(self):
            return LogMessage(self)


logging.basicConfig(level=logging.DEBUG, format='Date & Time: %(asctime)s, Level: %(levelname)s, Message :%(message)s, service": "Discovery"', datefmt='%m/%d/%Y %I:%M:%S %p')

logMessage2 = LogMessage.LogMessageBuilder()

now = datetime.datetime.now()

message = logMessage2.add("test", "test").add("1", 1).add("key", "value").add("test2", "test3").add("current date",now.strftime("%Y-%m-%d %H:%M")).build().toJson()

logging.warning(message)







