def check_open_closed_brack(arr, err, finish):
    how_many_open_bracket = 0
    how_many_closed_bracket = 0

    for brackets in arr:
        if brackets == '(':
            how_many_open_bracket = how_many_open_bracket + 1
        if brackets == ')':
            how_many_closed_bracket = how_many_closed_bracket + 1

    if finish:
        if len(arr) == 0:
            return
        elif arr[len(arr) - 1] == '(':
            err()
            return

        while how_many_open_bracket > how_many_closed_bracket:
            arr.append(')')
            how_many_closed_bracket += 1

    else:
        if how_many_open_bracket > how_many_closed_bracket:
            arr.append(')')
        else:
            arr.append('(')
            return True
