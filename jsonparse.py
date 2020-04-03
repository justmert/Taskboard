import json
import preferences
import task
import os.path
from preferences import paths


def readjson_task():
    if os.path.isfile(paths["task_path"]):
        with open(paths["task_path"], "r") as f:
            task.items = json.load(f)


def writejson_task():
    with open(paths["task_path"], "w", encoding="utf-8") as f:
        json.dump(task.items, f, indent=4)
