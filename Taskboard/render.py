import Taskboard.task as task


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


def render_content(header, content):
    print(f"\n{icons['snippet']} {header}")
    print(content)


def _calculate_stats(arg_list=None):
    arg_list = arg_list if arg_list is not None else task.items
    counts = {"in-progress": 0, "done": 0,
              "undone": 0, "note": 0, "snippet": 0}
    percent = 0
    for item in arg_list:
        if item['type'] == "task":
            counts[item['status']] += 1
        else:
            counts[item['type']] += 1
    total = counts['in-progress'] + counts['done'] + counts['undone']
    percent = 0 if total == 0 else int((100 * counts['done'])/total)
    return counts, total, percent


def _get_coloured(color, count, text, bullet=True):
    return " {}{}{}{}{} {} {}".format(color, colors.BOLD, count, colors.END,
                                      colors.GREY, text, icons['bullet'] if bullet else '')


def render_stats(counts, sum, percent):
    doneph = _get_coloured(colors.GREEN, counts['done'], "done")
    inprogressph = _get_coloured(
        colors.BEIGE2, counts['in-progress'], "in progress")
    pendingph = _get_coloured(colors.VIOLET, counts['undone'], "pending")
    noteph = _get_coloured(colors.BLUE, counts['note'], "notes")
    snippetph = _get_coloured(
        colors.YELLOW, counts['snippet'], "snippets", False)
    print(f"\n {colors.GREY}{percent}% of all tasks completed")
    print(f"{doneph}{inprogressph}{pendingph}{noteph}{snippetph}")


def render_board_header(header, supplement=''):
    print("\n {}{} {}{}{}{}".format(
        icons['heart'], colors.VIOLET, colors.BOLD, header, colors.END, supplement))


def render_one_item(item, header=None, rn_day=True, rn_boards=True):
    if header == None:
        header = item['header']
    _render_id(item)  # render number and star
    _render_item_name(header, item['status'] == "done")
    _render_priority(item['priority'])  # for rendering priority
    _render_boardnames(item['board name']) if rn_boards else None
    _render_day(item['date'][1]) if rn_day else None
    print()


def _render_id(item):
    print(f"{colors.GREY}{item['number']:>4}{colors.END} ", end='')
    print("{0} {1}{2:<1}{3} ".format(icons[item['status']] if item['type'] == "task" else icons[item['type']],
                                     colors.GREY, icons['star'] if item['starred'] else '', colors.END), end='')


def _render_item_name(text, is_done):
    if is_done:
        print("{}{}{}".format(colors.GREY, text, colors.END), end='')
    else:
        print("{} ".format(text), end='')


def _render_boardnames(board_names):
    if board_names:
        print(" {}｢{}｣{}".format(colors.GREY,
                                 ','.join(board_names), colors.END), end='')


def _render_day(day):
    x = '' if day == 0 else str(day) + "d"
    print(" {}{}{}".format(colors.GREY, x, colors.END), end='')


def _render_priority(priority):
    print("{}".format(icons[priority]), end='')


def _make_bar(done, total):
    return colors.GREY + " [{}/{}]".format(done, total) + colors.END


def render_statictic():
    render_stats(*_calculate_stats())


def render_items(arg_l=None, board="My board", rn_stats=True,
                 rn_stats_all=True, rn_boards=True, rn_day=True, makebar=True):

    arg_list = arg_l if arg_l is not None else task.items
    if rn_stats:
        counts, total, percent = _calculate_stats(arg_l)  # calculating stats

    sup = _make_bar(counts['done'], total) if makebar else ''
    render_board_header(board, sup)

    for item in arg_list:
        render_one_item(item, item['header'], rn_day, rn_boards)
    render_stats(counts, sum, percent) if rn_stats_all else None
