def check_number(symbol, arr, err, data_type, should_sign):
    def concatenate_number_as_int(is_integer):
        former_digit = arr[len(arr) - 1]
        del arr[len(arr) - 1]
        joined_num = str(former_digit) + str(symbol)
        if is_integer:
            arr.append(int(joined_num))
        else:
            arr.append(float(joined_num))

    change_to_string = str(symbol)
    print(change_to_string[:1])
    # this is to check if a user input a negative number
    if change_to_string[:1] in ('-', '+', '/', '*'):
        err()
        if should_sign:
            return True
        else:
            return False
    else:
        if len(arr) == 1 and arr[0] in ('-', '+'):
            if arr[0] == '+':
                arr[:] = ['(', symbol]
            else:
                arr[:] = ['(', -symbol]
            return False
        elif len(arr) == 0:
            arr.append(symbol)
        else:
            if arr[len(arr) - 1] \
                    not in ('+', '-', '*', '/', '(', ')'):
                if type(arr[len(arr) - 1]) == int:
                    concatenate_number_as_int(data_type)
                elif type(arr[len(arr) - 1]) == float:
                    if data_type:
                        concatenate_number_as_int(False)
                    elif not data_type:
                        err()
            else:
                if should_sign:
                    if arr[len(arr) - 1] == '+':
                        arr[len(arr) - 1] = symbol
                    elif arr[len(arr) - 1] == '-':
                        arr[len(arr) - 1] = -symbol
                    else:
                        arr.append(symbol)
                    return False
                else:
                    arr.append(symbol)
