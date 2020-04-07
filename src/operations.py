import task
from jsonparse import writejson_task
from archive import writejson_archive
from render import render_items, render_oneline, colors, render_detail, render_find, calculate_stats, pr_stats
import pyperclip
import re
import editor
import os
render_pref = {"success": None, "print": True, "print_b": True}


def parse_boards(arg):
    args = arg.split(" ")
    boards = []
    indexes = []
    for index, item in enumerate(args):
        if "@" in item and item[0] == "@" and len(item) != 1 and item[1] != "@":
            boards.append(''.join(item[1:]))
            indexes.append(index)
    args = [y for x, y in enumerate(args) if x not in indexes]
    header = ' '.join(args)
    return header, boards


def timeline():
    render_pref['print'] = False
    render_pref['success'] = True
    timeline_dict = {}
    for item in task.items:
        if item['date'][0] not in timeline_dict:
            timeline_dict[item['date'][0]] = [item]
        else:
            timeline_dict[item['date'][0]].append(item)
    for key, value in timeline_dict.items():
        render_items(value, key, print_stats=False, print_day=False)

    c, s, p = calculate_stats()
    pr_stats(c, s, p)


def add_item(arg, item_type):
    render_pref['success'] = False
    if not arg:
        return
    header, boards = parse_boards(arg)
    num = task.items[-1]["number"]+1 if task.items else 1
    note_type = item_type
    prior = 1
    det = editor.snippet_geteditor() if item_type == "snippet" else None
    if det is not None and (det == "" or det.isspace()):
        return

    if det is not None:
        det = det[0:-1]

    status = "undone" if item_type == "task" else None
    task.items.append(task.Task(note_type, num, header,
                                det, status, prior, boards).to_dict())
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


def view(nums):
    render_pref['success'] = False
    if len(nums) != 1:
        return

    found = [x for x in task.items if x['number']
             == nums[0] and x['type'] == "snippet"]
    render_pref['success'] = True if found else False
    if render_pref['success']:
        render_pref['print'] = False
        print("\n"+found[0]['detail'])


def edit_detail(nums):
    render_pref['success'] = False
    if len(nums) != 1:
        return

    findex = -1
    for index, item in enumerate(task.items):
        if item['number'] == nums[0] and item['type'] == "snippet":
            findex = index
            break

    render_pref['success'] = True if findex != -1 else False
    if render_pref['success']:
        task.items[findex]['detail'] = editor.snippet_geteditor(
            contents=task.items[findex]['detail'])
        writejson_task()


def copy_detail(nums):
    render_pref['success'] = False
    if len(nums) != 1:
        return

    found = [x for x in task.items if x['number']
             == nums[0] and x['type'] == "snippet"]
    render_pref['success'] = True if found else False
    if render_pref['success']:
        pyperclip.copy(found[0]['detail'])


def find_detail(arg):
    render_pref['success'] = False
    if not arg or arg.isspace():
        return
    for item in task.items:
        if item['type'] == "snippet" and arg in item['detail']:
            render_pref['success'] = True
            render_pref['print'] = False
            indexes = [m.start() for m in re.finditer(arg, item['detail'])]
            content = ""
            start_inx = 0
            last_inx = indexes[-1]
            for index in indexes:
                content = content + item['detail'][start_inx:index] + colors.BLUE + item['detail'][index:index+len(arg)] + \
                    colors.END
                start_inx = index + len(arg)
            content = content + item['detail'][last_inx+len(arg):]
            render_detail(item['header'], content)


def find(arg):
    render_pref['success'] = False
    if not arg or arg.isspace():
        return
    is_itfirst = True
    for item in task.items:
        if arg in item['header']:
            render_pref['success'] = True
            render_pref['print'] = False
            indexes = [m.start() for m in re.finditer(arg, item['header'])]
            content = ""
            start_inx = 0
            last_inx = indexes[-1]
            for index in indexes:
                content = content + item['header'][start_inx:index] + colors.BLUE + item['header'][index:index+len(arg)] + \
                    colors.END
                start_inx = index + len(arg)
            content = content + item['header'][last_inx+len(arg):]
            render_find(item, content, True) if is_itfirst else render_find(
                item, content)
            is_itfirst = False


def copy(nums):
    render_pref['success'] = False
    if len(nums) != 1:
        return

    found = [x for x in task.items if x['number'] == nums[0]]
    render_pref['success'] = True if found else False
    if render_pref['success']:
        pyperclip.copy(found[0]['header'])


def restore(nums):
    render_pref['success'] = False
    if not nums:
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
    render_pref['print'] = False
    render_items(task.archive, "Archive", False)


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
    board_dict = {"My Board":[]}
    for item in task.items:
        if not item['board name']:
            board_dict['My Board'].append(item)
            
        for b in item['board name']:
            if b not in board_dict:
                board_dict[b] = [item]
            else:
                board_dict[b].append(item)

    render_pref['print'] = False
    render_pref['success'] = True
    for key, value in board_dict.items():
        render_items(value, key, print_stats=False, print_boards=False)

    c, s, p = calculate_stats()
    pr_stats(c, s, p)


def edit(arg):
    render_pref['success'] = False
    num, header = arg.lsplit(" ", 1) if " " in arg else (arg, "")
    if not header:
        return
    for item in task.items:
        if item['number'] == num:
            render_pref['success'] = True
            item['header'] = header

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
    writejson_archive()
    render_pref['success'] = True


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
    if not nums:
        return
    for item in task.items:
        if item['number'] in nums:  # there is some error. check later
            if book not in item['board name']:
                item['board name'].clear()
                bookst = book.strip()
                if bookst:
                    item['board name'].append(bookst)
                render_pref['success'] = True
    writejson_task() if render_pref['success'] else None
