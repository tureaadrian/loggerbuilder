import json

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





