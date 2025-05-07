import json


class Form:
    def __init__(self):
        self.data = {
            "Firstname": "",
            "Lastname": "",
            "Email": "",
            "Reason of contact": "",
            "Urgency": "",
        }

    def validate_data(self): ...

    def update_data(self, response: dict):
        for key in self.data:
            if key in response:
                self.data[key] = response[key]

    def is_complete(self):
        isCompleted = all(value != "" for value in self.data.values())
        return isCompleted

    def to_json(self):
        response = json.dumps(self.data, indent=4, ensure_ascii=False)
        return response
