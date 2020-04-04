from enum import Enum
import datetime

items = []
archive = []


class Task:
    prip_dict = {1: "low", 2: "medium", 3: "high"}

    def __init__(self, task_type, number, header, detail, status, priority, where, is_starred=False):
        self.type = task_type
        self.number = number
        self.header = header
        self.detail = detail
        self.status = status
        self.priority = priority
        self.where = where
        self.is_starred = is_starred
        self.time = str(datetime.datetime.now())

    def to_dict(self):
        return {"type": self.type,
                "number": self.number,
                "header": self.header,
                "detail": self.detail,
                "status": self.status,
                "priority":  Task.prip_dict[self.priority],
                "board name": self.where,
                "starred": self.is_starred,
                "create time": self.time}
