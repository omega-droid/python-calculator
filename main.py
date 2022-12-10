from check_if_is_operator import check_operator
from check_if_is_number import check_number
from check_if_is_bracket import check_bracket


def syntax_error(message='invalid combination'):
    print(message)


stores_digits_and_operator = []
enter_digits_and_OPERATOR = input('enter digit or operator: ')
want_two_operator = False

validate_operator = check_operator
validate_number = check_number
validate_bracket = check_bracket

while enter_digits_and_OPERATOR != 'cal.py':
    if enter_digits_and_OPERATOR == 'b':
        brackets = enter_digits_and_OPERATOR
        want_two_operator = validate_bracket(stores_digits_and_operator)

    elif enter_digits_and_OPERATOR in ('-', '+', '*', '/'):
        operator = enter_digits_and_OPERATOR
        validate_operator(symbol=operator, arr=stores_digits_and_operator,
                          should_sign_num=want_two_operator, err=syntax_error)
        if want_two_operator:
            want_two_operator = False
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
            validate_number(symbol=digit, arr=stores_digits_and_operator,
                            err=syntax_error,
                            data_type=is_it_integer)
            if want_two_operator:
                want_two_operator = False
    print(stores_digits_and_operator)
    enter_digits_and_OPERATOR = input('enter digit or operator: ')
