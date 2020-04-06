import json
import preferences
import task
from datetime import datetime
from time import gmtime, strftime
from preferences import paths
import os.path


def _convert_todatetime():
    curr_time = task.getdatetime()
    curr_date = datetime.strptime(curr_time, "%a %b %d %Y")
    for item in task.items:
        task_time = item['date'][0]
        task_date = datetime.strptime(task_time, "%a %b %d %Y")
        item['date'][1] = (curr_date-task_date).days


def readjson_task():
    if os.path.isfile(paths["task_path"]):
        with open(paths["task_path"], "r") as f:
            task.items = json.load(f)
    _convert_todatetime()


def writejson_task():
    with open(paths["task_path"], "w") as f:
        json.dump(task.items, f, indent=4, default=str)
