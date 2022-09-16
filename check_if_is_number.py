def check_number(symbol, arr, should_sign_num, err, data_type):
    def concatenate_number_as_int(is_integer):
        former_digit = arr[len(arr) - 1]
        del arr[len(arr) - 1]
        joined_num = str(former_digit) + str(symbol)
        if is_integer:
            arr.append(int(joined_num))
        else:
            arr.append(float(joined_num))

    change_to_string = str(symbol)
    if change_to_string[:1] in ('-', '+', '/', '*'):
        err()
    else:
        if len(arr) == 1 and arr[0] in ('-', '+'):
            if arr[0] == '+':
                arr[:] = ['(', +symbol]
            else:
                arr[:] = ['(', -symbol]
        elif len(arr) == 0:
            arr.append(symbol)
        else:
            if should_sign_num:
                if arr[len(arr) - 1] in ('-', '+'):
                    store_neg_or_pos = arr[len(arr) - 1]
                    del arr[len(arr) - 1]
                    negative_dig = store_neg_or_pos + str(symbol)
                    arr.append(float(negative_dig))
                    should_sign_num = False
                    return should_sign_num
                else:
                    arr.append(symbol)
                    should_sign_num = False
                    return should_sign_num
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
                    arr.append(symbol)
