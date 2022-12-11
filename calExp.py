from __checkOpenClosedBracket import check_open_closed_brack

check_bracket_num = check_open_closed_brack


def calculate_expression(arr, err):
    check_bracket_num(arr, err, True)
    print(arr)
