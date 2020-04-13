from enum import Enum
from datetime import datetime
from time import localtime, strftime

items = []
archive = []


def _get_datetime():
    return strftime("%a %b %d %Y", localtime())


class Task:
    prip_dict = {"*1": "low", "*2": "medium", "*3": "high"}

    def __init__(self, task_type, number, header, detail, status, priority, where, is_starred=False):
        self.type = task_type
        self.number = number
        self.header = header
        self.detail = detail
        self.status = status
        self.priority = priority
        self.where = where
        self.is_starred = is_starred
        self.time = [_get_datetime(), 0]

    def to_dict(self):
        return {"type": self.type,
                "number": self.number,
                "header": self.header,
                "detail": self.detail,
                "status": self.status,
                "priority":  Task.prip_dict[self.priority],
                "board name": self.where,
                "starred": self.is_starred,
                "date": self.time}
