# Author: @simonaprs
# ----------------------------------------------------------------------------
# Imports
import operator
import re


def calculate(expression):
    """ Performs operations on RPN depending on conditions """
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '%': operator.mod}
    int_lst = []
    expression_split = expression.split(' ')
    expression_lst = list(expression_split)

    for i in range(0, len(expression_lst)):
        if expression_lst[i].isdigit():
            int_lst.append(expression_lst[i])
        elif not expression_lst[i].isdigit() and i < len(expression_lst) - 1 and expression_lst[i + 1].isdigit():
            result = operators[expression_lst[i]](int(int_lst[len(int_lst) - 2]), int(int_lst[len(int_lst) - 1]))
            del int_lst[-2:]
            int_lst.append(result)
        elif not expression_lst[i].isdigit() and i < len(expression_lst) - 1 and not expression_lst[i + 1].isdigit():
            type(int_lst[-2:-1])
            result = operators[expression_lst[i]](int(int_lst[len(int_lst) - 2]), int(int_lst[len(int_lst) - 1]))
            del int_lst[-2:]
            int_lst.append(result)
        elif not expression_lst[i].isdigit() and i == len(expression_lst) - 1:
            result = operators[expression_lst[i]](int(int_lst[len(int_lst) - 2]), int(int_lst[len(int_lst) - 1]))
            if isinstance(result, float):
                result = int(result)

    print(expression, "equals:", result)

    return result


def check_input(expression):
    """ Checks if input string of numbers and operators is acceptable """
    input_valid = False
    special_char_check = re.compile("[3@_!#$^&()'<>?|}{~:.]")
    operator_lst = ['+', '-', '*', '/', '%']

    if expression and special_char_check.search(expression) is None and not any(i.isalpha() for i in expression) \
            and [o for o in operator_lst if o in expression] is not None:
        print("Correct input, you typed:", expression)
        input_valid = True
    else:
        print("Incorrect format. Try again with whole numbers and supported operators (+, -, *, /, %) "
              "only. You typed:", expression)

    return input_valid


def solve(expression):
    if check_input(expression):
        calculate(expression)


if __name__ == '__main__':
    solve(input())
