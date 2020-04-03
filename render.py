import task

icons = {"heart": "♥",
         "note": "●",
         "undone": "☐",
         "in-progress": "⋯",
         "star": "★",
         "done": "✔",
         "fail": "✘",
         "diamond": "❖",
         "low": "",
         "medium": "(!)",
         "high": "(!!)",
         }


def render_items(arg_list=None, board="My board"):
    arg_list = arg_list if arg_list else task.items
    print("\n {0} {1}".format(icons['heart'], board))
    counts = {"in-progress": 0, "done": 0, "undone": 0, "note": 0}

    for item in arg_list:
        if item['type'] == "note":
            counts['note'] += 1
        else:
            counts[item['status']] += 1
        sum = counts['in-progress'] + counts['done'] + counts['undone']
        percent = 0 if sum == 0 else int((100 * counts['done'])/sum)
        print("{0}. ".format(item['number']).rjust(6), end="")
        print("{0}  {1} ".format(icons['note'] if item['type'] == "note" else icons[item['status']],
                                 item['description']), end='')
        print("{0} {1}".format(
            icons[item['priority']], icons['star'] if item['starred'] else ''), end='')
        for item in item['board name']:
            if item != "My Board":
                print(f"♥{item} ", end='')
        print()
    print("\n {0}% of all tasks completed\n {1} done · {2} in-progress · {3} pending · {4} notes".
          format(percent, counts['done'], counts['in-progress'], counts['undone'], counts['note']))


def render_oneline(arg_list=None, board="My board"):
    arg_list = arg_list if arg_list else task.items
    for item in arg_list:
        print("{0}. ".format(item['number']).rjust(6), end="")
        print("{0}  {1} ".format(icons['note'] if item['type'] == "note" else icons[item['status']],
                                 item['description']), end='')
        print("{0} {1}".format(
            icons[item['priority']], icons['star'] if item['starred'] else ''), end='')
        print()
