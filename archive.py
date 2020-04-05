import json
import preferences
import task
import os.path
from preferences import paths


def readjson_archive():
    if os.path.isfile(paths["archive_path"]):
        with open(paths["archive_path"], "r") as f:
            task.archive = json.load(f)


def writejson_archive():
    with open(paths["archive_path"], "w") as f:
        json.dump(task.archive, f, indent=4)
