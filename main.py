from check_if_is_operator import check_operator


def syntax_error(message='invalid combination'):
    print(message)


def concatenate_number_as_int(is_integer):
    former_digit = stores_digits_and_operator[len(stores_digits_and_operator) - 1]
    del stores_digits_and_operator[len(stores_digits_and_operator) - 1]
    joined_num = str(former_digit) + str(digit)
    if is_integer:
        stores_digits_and_operator.append(int(joined_num))
    else:
        stores_digits_and_operator.append(float(joined_num))


stores_digits_and_operator = []
enter_digits_and_OPERATOR = input('enter digit or operator: ')
want_two_operator = False
validate_operator = check_operator
print('hello')

while enter_digits_and_OPERATOR != 'cal.py':
    if enter_digits_and_OPERATOR == 'b':
        if stores_digits_and_operator[len(stores_digits_and_operator) - 1] in ('(', '-', '+', '/', '*'):
            stores_digits_and_operator.append('(')
            want_two_operator = True
        else:
            how_many_open_bracket = 0
            how_many_closed_bracket = 0
            for brackets in stores_digits_and_operator:
                if brackets == '(':
                    how_many_open_bracket = how_many_open_bracket + 1
                if brackets == ')':
                    how_many_closed_bracket = how_many_closed_bracket + 1
            if how_many_open_bracket > how_many_closed_bracket:
                stores_digits_and_operator.append(')')
            else:
                stores_digits_and_operator.append('(')
                want_two_operator = True
    elif enter_digits_and_OPERATOR in ('-', '+', '*', '/'):
        operator = enter_digits_and_OPERATOR
        # if the legnth of store digit and operator contains only one operator eithe - or +
        validate_operator(symbol=operator, arr=stores_digits_and_operator,
                          should_sign_num=want_two_operator, err=syntax_error)
    else:
        try:
            is_it_integer = True
            digit = enter_digits_and_OPERATOR
            for number in digit:
                if number == '.':
                    is_it_integer = False

            if is_it_integer:
                digit = int(digit)
            else:
                digit = float(digit)
        except ValueError:
            syntax_error(message='please input valid operator or digit')
        else:
            change_to_string = str(digit)
            if change_to_string[:1] in ('-', '+', '/', '*'):
                syntax_error(message='please input valid operator or digit')
            else:
                if len(stores_digits_and_operator) == 1 and stores_digits_and_operator[0] in ('-', '+'):
                    if stores_digits_and_operator[0] == '+':
                        stores_digits_and_operator = ['(', +digit]
                    else:
                        stores_digits_and_operator = ['(', -digit]
                elif len(stores_digits_and_operator) == 0:
                    stores_digits_and_operator.append(digit)
                else:
                    if want_two_operator:
                        if stores_digits_and_operator[len(stores_digits_and_operator) - 1] in ('-', '+'):
                            store_neg_or_pos = stores_digits_and_operator[len(stores_digits_and_operator) - 1]
                            del stores_digits_and_operator[len(stores_digits_and_operator) - 1]
                            negative_dig = store_neg_or_pos + str(digit)
                            stores_digits_and_operator.append(float(negative_dig))
                            want_two_operator = False
                        else:
                            stores_digits_and_operator.append(digit)
                            want_two_operator = False
                    else:
                        if stores_digits_and_operator[len(stores_digits_and_operator) - 1] \
                                not in ('+', '-', '*', '/', '(', ')'):
                            if type(stores_digits_and_operator[len(stores_digits_and_operator) - 1]) == int:
                                if is_it_integer:
                                    concatenate_number_as_int(True)
                                elif not is_it_integer:
                                    concatenate_number_as_int(False)
                            elif type(stores_digits_and_operator[len(stores_digits_and_operator) - 1]) == float:
                                if is_it_integer:
                                    concatenate_number_as_int(False)
                                elif not is_it_integer:
                                    syntax_error()
                        else:
                            stores_digits_and_operator.append(digit)
    print(stores_digits_and_operator)
    enter_digits_and_OPERATOR = input('enter digit or operator: ')
