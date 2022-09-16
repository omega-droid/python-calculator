def check_bracket(arr):
    if len(arr) == 0:
        arr.append('(')
    elif arr[len(arr) - 1] in ('(', '-', '+', '/', '*'):
        arr.append('(')
        should_sign_num = True
        return should_sign_num
    else:
        how_many_open_bracket = 0
        how_many_closed_bracket = 0
        for brackets in arr:
            if brackets == '(':
                how_many_open_bracket = how_many_open_bracket + 1
            if brackets == ')':
                how_many_closed_bracket = how_many_closed_bracket + 1
        if how_many_open_bracket > how_many_closed_bracket:
            arr.append(')')
        else:
            arr.append('(')
            should_sign_num = True
            return should_sign_num
