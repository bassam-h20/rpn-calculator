# Shunting-yard Algorithm implemented in Python.
# Takes a string using infix notation and outputs it in postfix.
# For example: (5+4)*8 -> 5 4 + 8 *
# This is reproduced from the Gist: https://gist.github.com/ollybritton/3ecdd2b28344b0b25c547cbfcb807ddc
# Details of the algorithm can be found here: https://en.wikipedia.org/wiki/Shunting_yard_algorithm

import re
from collections import namedtuple

opinfo = namedtuple('Operator', 'precedence associativity')
operator_info = {
    "+": opinfo(0, "L"),
    "-": opinfo(0, "L"),
    "/": opinfo(1, "L"),
    "*": opinfo(1, "L"),
    "!": opinfo(2, "L"),
    "^": opinfo(2, "R"),
}


def tokenize(input_string):
    cleaned = re.sub(r'\s+', "", input_string)
    chars = list(cleaned)

    output = []
    state = ""
    buf = ""

    while len(chars) != 0:
        char = chars.pop(0)

        if char.isdigit():
            if state != "num":
                output.append(buf) if buf != "" else False
                buf = ""

            state = "num"
            buf += char

        elif char in operator_info.keys() or char in ["(", ")"]:
            output.append(buf) if buf != "" else False
            buf = ""

            output.append(char)

        else:
            if state != "func":
                output.append(buf) if buf != "" else False
                buf = ""

            state = "func"
            buf += char

    output.append(buf) if buf != "" else False
    return output


def shunt(tokens, debug=False):
    tokens += ['end']
    operators = []
    output = []

    while len(tokens) != 1:
        current_token = tokens.pop(0)

        if current_token.isdigit():
            # Is a number
            if debug:
                print("number", current_token)
            output.append(current_token)

        elif current_token in operator_info.keys():
            # Is an operator
            if debug:
                print("op", current_token)

            while True:
                if len(operators) == 0:
                    break

                satisfied = False

                if operators[-1].isalpha():
                    # is a function
                    satisfied = True

                if operators[-1] not in ["(", ")"]:
                    if operator_info[operators[-1]].precedence > operator_info[current_token].precedence:
                        # operator at top has greater precedence
                        satisfied = True

                    elif operator_info[operators[-1]].precedence == operator_info[current_token].precedence:
                        if operator_info[operators[-1]].associativity == "left":
                            # equal precedence and has left associativity
                            satisfied = True

                satisfied = satisfied and operators[-1] != "("

                if not satisfied:
                    break

                output.append(operators.pop())

            operators.append(current_token)

        elif current_token == "(":
            # Is left bracket
            if debug:
                print("left", current_token)
            operators.append(current_token)

        elif current_token == ")":
            # Is right bracket
            if debug:
                print("right", current_token)

            while True:
                if len(operators) == 0:
                    break

                if operators[-1] == "(":
                    break

                output.append(operators.pop())

            if len(operators) != 0 and operators[-1] == "(":
                operators.pop()

        else:
            # Is a function name
            if debug:
                print("func", current_token)
            operators.append(current_token)

    output.extend(operators[::-1])

    return output




tokens = tokenize("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3")
print(" ".join(shunt(tokens)))
