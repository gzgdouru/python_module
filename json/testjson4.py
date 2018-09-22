import json

class TestJson:
    def __init__(self):
        self.msgType = "hello"
        self.msgText = "1"
        self.data = {}
        self.data["da"] = 0.00

    def serialization(self):
        print self.__dict__
        print json.dumps(self.__dict__, skipkeys=True, indent=4)

if __name__ == "__main__":
    test = TestJson();
    test.serialization()