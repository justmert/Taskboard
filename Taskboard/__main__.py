import os
import sys
import Taskboard.preferences as pr
import Taskboard.task as task
from Taskboard.render import icons, render_items, colors
from Taskboard.jsonparse import read_json_archive, read_json_items
import Taskboard.operations as op
from Taskboard.help import help_message, examples


def check_paths():
    pr.paths['project_dir'] = pr.prefs['taskboardDirectory'] + "/.taskboard"
    if not os.path.exists(pr.paths['project_dir']):
        os.mkdir(pr.paths['project_dir'])
    pr.paths['task_path'] = pr.paths['project_dir'] + "/tasks.json"
    pr.paths['archive_path'] = pr.paths['project_dir'] + "/archive.json"


def parse_nums(arg):
    return [int(s) for s in arg.split() if s.isdigit()]


def feedback():
    ret = ''
    if op.render_prefs['success']:
        ret = ' ' + icons['done']

    elif op.render_prefs['success'] == False:
        ret = ' ' + icons['fail']

    op.render_prefs['success'] = None
    return ret


def split_input(inp):
    param, arg = inp.split(" ", 1) if " " in inp else (inp, "")
    arg = arg.strip()
    return param, arg


def parse_input(param, arg):

    op.render_prefs['success'] = False

    if param in ["t", "task"]:
        op.add_item(arg, "task")

    elif param in ["n", "note"]:
        op.add_item(arg, "note")

    elif param in ["sn", "snippet"]:
        op.add_item(arg, "snippet")

    elif param in ["b", "begin"]:
        x = parse_nums(arg)
        op.begin(x) if x else None

    elif param in ["c", "check"]:
        x = parse_nums(arg)
        op.check(x) if x else None

    elif param in ["e", "edit"]:
        op.edit(arg)

    elif param in ["d", "delete"]:
        x = parse_nums(arg)
        op.delete(x) if x else None

    elif param in ["f", "find"]:
        op.find(arg) if arg else None

    elif param in ["s", "star"]:
        x = parse_nums(arg)
        op.star(x) if x else None

    elif param in ["p", "priority"]:
        op.priority(arg)

    elif param in ["m", "move"]:
        op.move(arg)

    elif param in ["l", "list"]:
        op.list_boards()

    elif param in ["y", "copy"]:
        op.copy(parse_nums(arg))

    elif param in ["a", "archive"]:
        op.archive()

    elif param in ["r", "restore"]:
        x = parse_nums(arg)
        op.restore(x) if x else None

    elif param in ["v", "view"]:
        op.view(parse_nums(arg))

    elif param in ["at", "attach"]:
        op.attach_to_board(arg)

    elif param in ["cc", "copycon"]:
        op.copy_content(parse_nums(arg))

    elif param in ["ec", "editcon"]:
        op.edit_content(parse_nums(arg))

    elif param in ["fc", "findcon"]:
        op.find_content(arg) if arg else None

    elif param in ["rf", "refactor"]:
        op.refactor()

    elif param in ["cl", "clear"]:
        op.clear(pr.paths['archive_path'])

    elif param in ["tl", "timeline"]:
        op.timeline()

    elif param in ["h", "help"]:
        op.render_prefs['print'] = False
        op.render_prefs['success'] = None
        print(help_message)

    elif param in ["ex", "examples"]:
        op.render_prefs['print'] = False
        op.render_prefs['success'] = None
        print(examples)

    elif param == "exit":
        exit()

    else:
        op.render_prefs['success'] = None


def main():
    pr.check_prefs()
    check_paths()
    read_json_archive()
    read_json_items()

    if len(sys.argv)>1:
        op.switch_param = ' '.join(sys.argv[1:]).strip()

    while True:
        if not op.render_prefs['print']:
            op.render_prefs['print'] = True

        elif op.switch_param:
            render_items(op.switch_initilize(),
                         rn_boards=False, board=op.switch_param)
        else:
            render_items()

        inp = input("\n {}{}Taskboard{}{} {} ".format(
            colors.BLUE2, colors.BOLD, colors.END,
            feedback(), icons['diamond'])).strip()

        param, arg = split_input(inp)

        if param in ["sw", "switch"]:
            op.switch(arg)

        elif inp:
            parse_input(param, arg)


if __name__ == "__main__":
    main()
