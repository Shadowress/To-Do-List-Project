import datetime


class Task:

    def __init__(self, title: str, description: str, due_date: datetime, status):  #todo status would be an enum
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        ...

    def to_dict(self):
        ... #todo convert task for saving to json or csv

    @classmethod
    def from_dict(cls):
        ... #todo THE USE OF THIS METHOD IS TO BE DEFINED