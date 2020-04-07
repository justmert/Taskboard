import task


class colors:
    END = '\33[0m'
    BOLD = '\33[1m'
    UNDERLINE = '\33[4m'
    ITALIC = '\33[3m'
    BLINK = '\33[5m'
    RED = '\33[31m'
    GREEN = '\33[32m'
    YELLOW = '\33[33m'
    BLUE = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE = '\33[36m'
    GREY = '\33[90m'
    RED2 = '\33[91m'
    GREEN2 = '\33[92m'
    YELLOW2 = '\33[93m'
    BLUE2 = '\33[94m'
    VIOLET2 = '\33[95m'
    BEIGE2 = '\33[96m'
    WHITE = '\33[37m'


icons = {"heart": colors.RED2 + "♥" + colors.END,
         "note": colors.BLUE + "●" + colors.END,
         "snippet": colors.YELLOW + "◆" + colors.END,
         "undone": colors.VIOLET + "☐" + colors.END,
         "in-progress": colors.BEIGE2 + "⋯"+colors.END,
         "star": colors.YELLOW2 + "★" + colors.END,
         "done": colors.GREEN+"✔"+colors.END,
         "fail": colors.RED + "✘" + colors.END,
         "diamond": colors.WHITE + "❖" + colors.END,
         "bullet": colors.WHITE + "·" + colors.END,
         "low": "",
         "medium": colors.BLUE2 + "✦" + colors.END,
         "high": colors.BLUE2 + "✦✦" + colors.END,
         }


def render_detail(header, detail):
    print(f"\n{icons['snippet']} {header}")
    print("{0}".format(detail))


def render_find(item, colourized_header, print_h=False):
    if print_h:
        print(
            f"\n {icons['heart']}{colors.VIOLET} {colors.BOLD}Found Items{colors.END}")
    print(f"{colors.GREY}{item['number']:>4}{colors.END} ", end='')
    print("{0} {1}{2:<1}{3} ".format(icons[item['status']] if item['type'] == "task" else icons[item['type']],
                                     colors.GREY, icons['star'] if item['starred'] else '', colors.END), end='')
    # header
    if item['status'] == "done":
        print("{0}{1}{2}".format(colors.GREY,
                                 colourized_header, colors.END), end='')
    else:
        print("{0} ".format(colourized_header), end='')

    print("{0}".format(icons[item['priority']]), end='')
    if item['board name']:
        print(" {0}｢{1}｣{2}".format(colors.GREY, ','.join(
            item['board name']), colors.END), end='')

    x = '' if item['date'][1] == 0 else str(item['date'][1]) + "d"
    print(" {0}{1}{2}".format(colors.GREY, x, colors.END), end='')
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
    print(f"\n{colors.GREY} {percent}% of all tasks completed\n {colors.GREEN}{colors.BOLD}{counts['done']}{colors.END}{colors.GREY} done {icons['bullet']} " +
          f"{colors.BEIGE2}{colors.BOLD}{counts['in-progress']}{colors.END}{colors.GREY} in progress {icons['bullet']} {colors.VIOLET}{colors.BOLD}{counts['undone']}{colors.END} {colors.GREY}" +
          f"pending {icons['bullet']} {colors.BLUE}{colors.BOLD}{counts['note']}{colors.END} {colors.GREY}notes {icons['bullet']} {colors.YELLOW}{colors.BOLD}{counts['snippet']}{colors.END} {colors.GREY} snippets {colors.END}")


def render_items(arg_l=None, board="My board", print_stats=True, print_boards=True, print_day=True):
    arg_list = arg_l if arg_l is not None else task.items
    counts, sum, percent = calculate_stats(arg_l)
    print(f"\n {icons['heart']}{colors.VIOLET} {colors.BOLD}{board}{colors.END}" +
          f" {colors.GREY}[{counts['done']}/{sum}]{colors.END}")
    for item in arg_list:
        print(f"{colors.GREY}{item['number']:>4}{colors.END} ", end='')
        print("{0} {1}{2:<1}{3} ".format(icons[item['status']] if item['type'] == "task" else icons[item['type']],
                                         colors.GREY, icons['star'] if item['starred'] else '', colors.END), end='')
        # header
        if item['status'] == "done":
            print("{0}{1}{2}".format(colors.GREY,
                                     item['header'], colors.END), end='')
        else:
            print("{0} ".format(item['header']), end='')

        print("{0}".format(icons[item['priority']]), end='')
        if print_boards and item['board name']:
            print(" {0}｢{1}｣{2}".format(colors.GREY, ','.join(
                item['board name']), colors.END), end='')

        if print_day:
            x = '' if item['date'][1] == 0 else str(item['date'][1]) + "d"
            print(" {0}{1}{2}".format(colors.GREY, x, colors.END), end='')

        print()
    if print_stats:
        pr_stats(counts, sum, percent)


def render_oneline(arg_list=None, board="My board"):
    arg_list = arg_list if arg_list is not None else task.items
    print()
    for item in arg_list:
        print(f"{colors.GREY}{item['number']:>4}{colors.END} ", end='')
        print("{0} {1}{2:<1}{3} ".format(icons[item['status']] if item['type'] == "task" else icons[item['type']],
                                         colors.GREY, icons['star'] if item['starred'] else '', colors.END), end='')
        # header
        if item['status'] == "done":
            print("{0}{1}{2}".format(colors.GREY,
                                     item['header'], colors.END), end='')
        else:
            print("{0} ".format(item['header']), end='')

        print("{0}".format(icons[item['priority']]), end='')
        print()
