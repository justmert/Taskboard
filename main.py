import argparse
import preferences as pr
import os
from pathlib import Path
import operations as op
from render import icons, render_items
from jsonparse import readjson_task
from archive import readjson_archive


def check_paths():
    pr.paths['project_dir'] = pr.prefs['taskitDirectory'] + "/.taskit"
    if not os.path.exists(pr.paths['project_dir']):
        os.mkdir(pr.paths['project_dir'])
    pr.paths['task_path'] = pr.paths['project_dir'] + "/tasks.json"
    pr.paths['archive_path'] = pr.paths['project_dir'] + "/archive.json"


def parse_nums(arg):
    return [int(s) for s in arg.split() if s.isdigit()]


def decide():
    ret = ''
    if op.render_pref['success']:
        ret = ' ' + icons['done']
    elif op.render_pref['success'] == False:
        ret = ' ' + icons['fail']

    op.render_pref['success'] = None
    return ret


def parse_input(inp):
    param, arg = inp.split(" ", 1) if " " in inp else (inp, "")

    if param in ["t", "task"]:
        op.add_item(arg, "task")

    elif param in ["n", "note"]:
        op.add_item(arg, "note")

    elif param in ["d", "delete"]:
        op.delete(parse_nums(arg))

    elif param in ["f", "find"]:
        op.find(arg)

    elif param in ["x", "copy"]:
        op.copy(parse_nums(arg))

    elif param in ["s", "star"]:
        op.star(parse_nums(arg))

    elif param in ["a", "archive"]:
        op.archive()

    elif param in ["r", "restore"]:
        op.restore(parse_nums(arg))

    elif param in ["rf", "refactor"]:
        op.refactor()

    elif param in ["l", "list"]:
        op.list_all()

    elif param in ["cl", "clear"]:
        op.clear(pr.paths['archive_path'])

    elif param in ["m", "move"]:
        op.move(arg)

    elif param in ["c", "check"]:
        op.check(parse_nums(arg))

    elif param in ["b", "begin"]:
        op.begin(parse_nums(arg))

    elif param in ["an", "addn"]:
        op.add_notebook(arg)

    elif param in ["e", "edit"]:
        op.edit(arg)

    elif param in ["o", "oneline"]:
        op.oneline()

    elif param in ["p", "priority"]:
        op.priority(arg)

    elif param == "exit":
        exit()


def main():
    pr.check_prefs()
    check_paths()
    readjson_task()
    readjson_archive()

    while True:
        if not op.render_pref['print']:
            op.render_pref['print'] = True
        else:
            render_items()

        inp = input("\nTaskIt{} {} ".format(
            decide(), icons['diamond'])).strip()
        if inp:
            parse_input(inp)


if __name__ == "__main__":
    main()
