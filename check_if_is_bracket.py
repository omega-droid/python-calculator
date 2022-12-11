from __checkOpenClosedBracket import check_open_closed_brack

check_bracket_num = check_open_closed_brack


def check_bracket(arr, err):
    if len(arr) == 0:
        arr.append('(')
    elif arr[len(arr) - 1] in ('(', '-', '+', '/', '*'):
        arr.append('(')
        return True
    else:
        return check_bracket_num(arr, err, False)
