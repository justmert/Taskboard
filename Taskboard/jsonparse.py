import json
import os.path
from datetime import datetime
from Taskboard.preferences import paths
import Taskboard.task as task


def read_json_archive():
    if os.path.isfile(paths["archive_path"]):
        with open(paths["archive_path"], "r") as f:
            task.archive = json.load(f)


def write_json_archive():
    with open(paths["archive_path"], "w") as f:
        json.dump(task.archive, f, indent=4, default=str)


def _find_daydiff():
    curr_time = task._get_datetime()
    curr_date = datetime.strptime(curr_time, "%a %b %d %Y")
    for item in task.items:
        task_time = item['date'][0]
        task_date = datetime.strptime(task_time, "%a %b %d %Y")
        item['date'][1] = (curr_date-task_date).days


def read_json_items():
    if os.path.isfile(paths["task_path"]):
        with open(paths["task_path"], "r") as f:
            task.items = json.load(f)
    _find_daydiff()


def write_json_items():
    with open(paths["task_path"], "w") as f:
        json.dump(task.items, f, indent=4, default=str)
