import json


class Form:
    def __init__(self) -> None:
        self.data = {
            "Firstname": "",
            "Lastname": "",
            "Email": "",
            "Reason of contact": "",
            "Urgency": None,
        }

    def update_data(self, response: dict) -> None:
        for key in self.data:
            if key in response:
                self.data[key] = response[key]

    def is_complete(self) -> bool:
        isCompleted = all(
            value not in ("", "Null") and value is not None
            for value in self.data.values()
        )
        return isCompleted

    def to_json(self) -> str:
        response = json.dumps(self.data, indent=4, ensure_ascii=False)
        return response
