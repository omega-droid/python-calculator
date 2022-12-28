from __checkOpenClosedBracket import check_open_closed_brack
from exp_comp import CreateNode
from __check_negative import check_for_negative

check_bracket_num = check_open_closed_brack

operator = ['-', '+', '*', '/', '^', '(', ')']

precedence = [4, 4, 3, 3, 2, 1, 1]

asc = ['l', 'l', 'l', 'l', 'r']

operator_stack = CreateNode()
operand_stack = CreateNode()


def cal_num(op):
    sec_num = operand_stack.pop()
    first_num = operand_stack.pop()
    if op == '+':
        new_num = first_num + sec_num
        operand_stack.push(new_num)
    elif op == '-':
        new_num = first_num - sec_num
        operand_stack.push(new_num)
    elif op == '/':
        new_num = first_num / sec_num
        operand_stack.push(new_num)
    elif op == '*':
        new_num = first_num * sec_num
        operand_stack.push(new_num)


def calculate_expression(arr, err):
    check_bracket_num(arr, err, True)

    index_of_negative = check_for_negative(arr)

    for i in range(len(arr)):
        if arr[i] in ('-', '+', '*', '/'):
            if operator_stack.show_size() == 0:
                operator_stack.push(arr[i])
            else:
                is_ordered = False
                arr_pre = operator.index(arr[i])
                stack_pre = operator.index(operator_stack.head.item)

                while not is_ordered:
                    if operator_stack.head.item == '(':
                        operator_stack.push(arr[i])
                        if i in index_of_negative:
                            operator_stack.head.negate = True
                        is_ordered = True

                    elif precedence[arr_pre] < precedence[stack_pre]:
                        operator_stack.push(arr[i])
                        is_ordered = True

                    elif precedence[arr_pre] > precedence[stack_pre]:
                        current_op = operator_stack.pop()
                        cal_num(current_op)

                        if operator_stack.is_empty():
                            operator_stack.push(arr[i])
                            is_ordered = True
                        else:
                            stack_pre = operator.index(operator_stack.head.item)

                    elif precedence[arr_pre] == precedence[stack_pre]:
                        current_op = operator_stack.pop()
                        cal_num(current_op)

                        if operator_stack.is_empty():
                            operator_stack.push(arr[i])
                            is_ordered = True
                        else:
                            stack_pre = operator.index(operator_stack.head.item)
        elif arr[i] == '(':
            operator_stack.push(arr[i])
        elif arr[i] == ')':
            is_open_b = operator_stack.head.item
            while is_open_b != '(':
                if operator_stack.head.negate:
                    operand_stack.head.item = -operand_stack.head.item
                    operator_stack.pop()
                else:
                    current_op = operator_stack.pop()
                    cal_num(current_op)
                is_open_b = operator_stack.head.item

            operator_stack.pop()
        else:
            operand_stack.push(arr[i])

    while operator_stack.show_size() > 0:
        current_op = operator_stack.pop()
        cal_num(current_op)

    print(operand_stack.head.item)
