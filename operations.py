import task
from jsonparse import writejson_task
from archive import writejson_archive
from render import render_items, render_oneline
import pyperclip
import os
render_pref = {"success": None, "print": True}


def parse_boards(arg):
    args = arg.split(" ")
    boards = []
    indexes = []
    for index, item in enumerate(args):
        if "@" in item and item[0] == "@" and len(item) != 1 and item[1] != "@":
            boards.append(''.join(item[1:]))
            indexes.append(index)
    args = [y for x, y in enumerate(args) if x not in indexes]
    desc = ' '.join(args)
    return desc, boards


def add_item(arg, item_type, special_num=None):
    if not arg:
        render_pref['success'] = False
        return
    desc, boards = parse_boards(arg)
    num = task.items[-1]["number"]+1 if task.items else 1
    if special_num:
        num = special_num
    note_type = item_type
    prior = 1
    boards.append("My Board")
    status = "undone"
    task.items.append(
        task.Task(note_type, num, desc, status, prior, boards).to_dict())
    writejson_task()
    render_pref['success'] = True


def delete(nums):
    render_pref['success'] = False
    if not nums:
        return
    indexes = [x for x, y in enumerate(task.items) if y['number'] in nums]

    for index in indexes:
        task.items[index]["number"] = task.archive[-1]["number"] + \
            1 if task.archive else 1
        task.archive.append(task.items[index])

    for index in reversed(indexes):
        del task.items[-1 * (len(task.items) - index)]

    render_pref['success'] = True if indexes else False
    writejson_task()
    writejson_archive() if render_pref['success'] else None


def find(arg):
    found = [x for x in task.items if arg in x['description']]
    render_pref['success'] = True if found else False
    if render_pref['success']:
        render_pref['print'] = False
        render_items(found, "Found Items")


def copy(nums):
    render_pref['success'] = False
    if len(nums) != 1:
        return

    found = [x for x in task.items if x['number'] == nums[0]]
    render_pref['success'] = True if found else False
    if render_pref['success']:
        pyperclip.copy(found[0]['description'])


def restore(nums):
    if not nums:
        render_pref['success'] = False
        return
    indexes = [x for x, y in enumerate(task.archive) if y['number'] in nums]

    for index in indexes:
        task.archive[index]["number"] = task.items[-1]["number"] + \
            1 if task.items else 1
        task.items.append(task.archive[index])
    for index in reversed(indexes):
        del task.archive[-1 * (len(task.archive) - index)]

    render_pref['success'] = True if indexes else False
    writejson_task()
    writejson_archive() if render_pref['success'] else None


def archive():
    render_items(task.archive, "Archive")
    render_pref['print'] = False


def check(nums):
    render_pref['success'] = False
    for item in task.items:
        if item['number'] in nums and item["type"] == "task":
            if item['status'] == "undone":
                item['status'] = "done"

            elif item['status'] == "done":
                item['status'] = "undone"

            elif item['status'] == "in-progress":
                item['status'] = "done"

            render_pref['success'] = True
    writejson_task() if render_pref['success'] else None


def priority(arg):
    render_pref['success'] = False
    nums, prior = arg.rsplit(" ", 1) if " " in arg else (arg, "")
    nums = [int(s) for s in nums.split() if s.isdigit()]
    if len(prior) < 2 or prior[0] != '*':
        return
    word = prior[1:]
    x = int(word) if word.isdigit() else None
    for item in task.items:
        if item["number"] in nums and x in task.Task.prip_dict.keys():
            item["priority"] = task.Task.prip_dict[x]
            render_pref['success'] = True

    writejson_task() if render_pref['success'] else None


def star(nums):
    render_pref['success'] = False
    for item in task.items:
        if item['number'] in nums:
            if item['starred']:
                item['starred'] = False
            else:
                item['starred'] = True
            render_pref['success'] = True

    writejson_task() if render_pref['success'] else None


def list_all():
    board_dict = {}
    for item in task.items:
        for b in item['board name']:
            if b not in board_dict:
                board_dict[b] = [item]
            else:
                board_dict[b].append(item)

    render_pref['print'] = False
    render_pref['success'] = True
    for key, value in board_dict.items():
        render_items(value, key)


def edit(arg):
    render_pref['success'] = False
    num, desc = arg.lsplit(" ", 1) if " " in arg else (arg, "")
    if not desc:
        return
    for item in task.items:
        if item['number'] == num:
            render_pref['success'] = True
            item['description'] = desc

    writejson_task() if render_pref['success'] else None


def oneline():
    render_pref['print'] = False
    render_oneline()
    pass


def begin(nums):
    render_pref['success'] = False
    for item in task.items:
        if item['number'] in nums and item["type"] == "task":
            if item['status'] != "in-progress":
                item['status'] = "in-progress"

            else:
                item['status'] = "undone"
            render_pref['success'] = True
    writejson_task() if render_pref['success'] else None


def refactor(do_archive=True):
    for inx, item in enumerate(task.items):
        item['number'] = inx + 1
    writejson_task()

    if do_archive:
        for inx, item in enumerate(task.archive):
            item['number'] = inx + 1
        writejson_archive()
    render_pref['success'] = True


def clear(path):
    if os.path.exists(path):
        os.remove(path)
    task.archive.clear()
    refactor(False)
    render_pref['success'] = True
    pass


def add_notebook(arg):
    render_pref['success'] = False
    nums, book = arg.rsplit(" ", 1) if " " in arg else (arg, "")
    nums = [int(s) for s in nums.split() if s.isdigit()]
    if not book or not nums:
        return
    for item in task.items:
        if item['number'] in nums and item['type']:
            if book not in item['board name']:
                item['board name'].append(book)
                render_pref['success'] = True

    writejson_task() if render_pref['success'] else None


def move(arg):
    render_pref['success'] = False
    nums, book = arg.rsplit(" ", 1) if " " in arg else (arg, "")
    nums = [int(s) for s in nums.split() if s.isdigit()]
    if not book or not nums:
        return
    for item in task.items:
        if item['number'] in nums and item['type']:
            if book not in item['board name']:
                item['board name'].clear()
                item['board name'].append('My Board')
                item['board name'].append(book)
                render_pref['success'] = True

    writejson_task() if render_pref['success'] else None
