def check_operator(symbol, arr, should_sign_num, err):
    if len(arr) == 1 and symbol in ('-', '+') and \
            arr[0] in ('-', '+'):
        arr[:] = [symbol]
        print('hello')
    elif len(arr) == 1 and symbol in ('/', '*') and \
            arr[0] in ('-', '+'):
        err()
    elif len(arr) == 0 and symbol in ('-', '+'):
        arr.append(symbol)
    elif len(arr) == 0 and symbol in ('/', '*'):
        err()
    else:
        if not should_sign_num:
            if arr[len(arr) - 1] in ('-', '+', '*', '/'):
                arr[len(arr) - 1] = symbol
            elif arr[len(arr) - 1] not in ('-', '+', '*', '/'):
                arr.append(symbol)
        else:
            if arr[len(arr) - 1] == '(':
                if symbol in ('+', '-'):
                    arr.append(symbol)
                else:
                    err()
