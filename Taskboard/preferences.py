import os
import json
from pathlib import Path

prefs = {}
paths = {}


def check_prefs():
    paths['home'] = str(Path.home())
    paths['config'] = paths['home'] + "/.taskboard.conf"
    if os.path.exists(paths['config']):
        read_prefs()
    else:
        set_prefs()
        with open(paths['config'], 'a', encoding="utf-8") as f:
            json.dump(prefs, f, indent=4)


def set_prefs():
    prefs["taskboardDirectory"] = paths['home']


def read_prefs():
    global prefs
    with open(str(paths['config']), 'r') as f:
        prefs = json.load(f)
