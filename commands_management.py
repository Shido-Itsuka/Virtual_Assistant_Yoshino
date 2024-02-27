import json


class Commands:
    def __init__(self):
        new_record = None

    def readfile(self):
        with open("commands.json", "r") as f:
            return json.load(f)

    def writefile(self, data):
        with open("commands.json", "w") as f:
            json.dump(data, f)
            f.close()

    def add_record(self):
        data = self.readfile()
        data.append(self.new_record)
        self.writefile(data)

    def edit_record(self, record):
        data = self.readfile()
        for i in range(len(data)):
            if data[i]["id"] == record["id"]:
                data[i] = record
        self.writefile(data)

    def delete_record(self):
        data = self.readfile()
        for i in range(len(data)):
            if data[i]["id"] == record["id"]:
                del data[i]
        self.writefile(data)


