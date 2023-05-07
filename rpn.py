from sy import tokenize, shunt


# This function evaluates an RPN expression and returns its result as an integer
def rpn_eval(expression: str) -> int:
    stack = []  # initialize an empty list to be used as a stack
    num1 = ''

    for char in expression:
        if char.isdigit():  # if the character is a digit, add it to the current number being parsed
            num1 += char
        if char == ' ':  # if the character is a space, the current number is complete and can be added to the stack
            if num1.isdigit():
                stack.append(int(num1))
                num1 = ''
        if char in ['+', '-', '*', '/']:  # if the character is an operator, pop two values from the stack and apply the operator to them
            RV1 = stack.pop()
            RV2 = stack.pop()

            result = None                       
                                                    # apply the operator to the two popped values
            if char == '+':  result = RV2 + RV1
            
            elif char == '-': result = RV2 - RV1
            
            elif char == '*': result = RV2 * RV1
            
            elif char == '/': result = RV2 / RV1

            if result is not None:  # if the operator was applied, push the result onto the stack
                stack.append(result)

    return stack.pop()  # the final value remaining on the stack is the result of the expression


# This function takes an expression as input either in infix or postfix notation. If the expression ends with a digit,
# it is assumed to be an infix expression and is converted to RPN using the shunt function from the sy module.
# Otherwise, the input is assumed to be in RPN format. The RPN expression is passed to the rpn_eval function which uses
# a stack to evaluate the expression
def check_string(string: str):
    if len(string) < 2:
        return (False, 0)

    rpn = ''

    if string[-1].isdigit():  # if the expression ends with a digit, assume it is in infix notation and convert it to RPN
        rpn = " ".join(shunt(tokenize(string)))
    else:
        rpn = string  # otherwise, assume the expression is already in RPN format

    result = 0

    try:
        result = rpn_eval(rpn)  # evaluate the RPN expression using the rpn_eval function
    except Exception as e:
        print(rpn, e)
        return (False, -1)

    return (True, result)  # return a tuple containing a boolean indicating whether the expression was valid and the result


# This is the main loop of the program. It repeatedly asks the user to enter an expression to evaluate until the user
# enters 'q' to quit. Each expression entered by the user is passed to the evaluate_expression function and the result
# is printed to the console
while True:
    user_input = input('Please enter the string (ex: "1 + 2" or "1 2 +")\n(or q to quit): ')
    if user_input == 'q':
        break
    result, ans = check_string(user_input)
    if result:
        print('=', ans)
    else:
        print('Invalid expression')
