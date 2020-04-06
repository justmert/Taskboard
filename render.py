import task

icons = {"heart": "♥",
         "note": "●",
         "snippet": "◆",
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


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def render_detail(header, detail):
    print("\n {0} {1}".format(icons['snippet'], header))
    print("{0}".format(detail))


def render_find(item, colourized_header, print_h=False):
    if print_h:
        print("\n {0} {1}".format(icons['heart'], "Found Items"))
    print("{0} ".format(item['number']).rjust(6), end="")
    print("{0} {1:<1} {2} ".format(icons[item['status']] if item['type'] == "task" else icons[item['type']],
                                   icons['star'] if item['starred'] else '', colourized_header), end='')
    print("{0}".format(icons[item['priority']]), end='')
    if item['board name']:
        print(" ｢{0}｣".format(','.join(item['board name'])), end='')
    print()


def calculate_stats(arg_list=None):
    arg_list = arg_list if arg_list is not None else task.items
    counts = {"in-progress": 0, "done": 0,
              "undone": 0, "note": 0, "snippet": 0}
    percent = 0
    for item in arg_list:
        if item['type'] == "task":
            counts[item['status']] += 1
        else:
            counts[item['type']] += 1
    summ = counts['in-progress'] + counts['done'] + counts['undone']
    percent = 0 if summ == 0 else int((100 * counts['done'])/summ)
    return counts, summ, percent


def pr_stats(counts, sum, percent):
    print("\n {0}% of all tasks completed\n {1} done · {2} in-progress · {3} pending · {4} notes\n".
          format(percent, counts['done'], counts['in-progress'], counts['undone'], counts['note']), end='')


def render_items(arg_l=None, board="My board", print_stats=True, print_boards=True, print_day=True):
    arg_list = arg_l if arg_l is not None else task.items
    counts, sum, percent = calculate_stats(arg_l)
    print("\n {0} {1} [{2}/{3}]".format(icons['heart'],
                                        board, counts['done'], sum))
    for item in arg_list:
        print("{0} ".format(item['number']).rjust(6), end="")
        print("{0} {1:<1} {2} ".format(icons[item['status']] if item['type'] == "task" else icons[item['type']],
                                       icons['star'] if item['starred'] else '', item['header']), end='')
        print("{0}".format(icons[item['priority']]), end='')

        if print_boards and item['board name']:
            print(" ｢{0}｣ ".format(','.join(item['board name'])), end='')

        if print_day:
            x = '' if item['date'][1] == 0 else str(item['date'][1]) + "d"
            print("{0}".format(x), end='')

        print()
    if print_stats:
        pr_stats(counts, sum, percent)


def render_oneline(arg_list=None, board="My board"):
    arg_list = arg_list if arg_list else task.items
    print()
    for item in arg_list:
        print("{0} ".format(item['number']).rjust(6), end="")
        print("{0} {1:<1} {2} ".format(icons[item['status']] if item['type'] == "task" else icons[item['type']],
                                       icons['star'] if item['starred'] else '', item['header']), end='')
        print("{0}".format(icons[item['priority']]))
