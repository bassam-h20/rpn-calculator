from main import Stack
from sy import tokenize, shunt


def rpn_eval(expression: str) -> int:
    # Create a stack object to hold the values of the expression as it is evaluated
    stack = Stack()
    
    # A string variable to hold the current numeric value being read in
    num1 = ''
    
    # Loop through each character in the expression
    for char in expression:
        # If the character is a digit, add it to the num1 variable
        if char.isdigit():
            num1 += char
            
        # If the character is a space, check if num1 is a digit and push it onto the stack
        if char == ' ':
            if num1.isdigit():
                stack.stack_push(int(num1))
                num1 = ''

        # If the character is an operator (+, -, *, /), pop two values from the stack and apply the operator
        # The result is then pushed onto the stack
        if char in ['+', '-', '*', '/']:
            RV1 = stack.stack_pop()
            RV2 = stack.stack_pop()

            result = None
            if char == '+':
                result = RV2 + RV1
            elif char == '-':
                result = RV2 - RV1
            elif char == '*':
                result = RV2 * RV1
            elif char == '/':
                result = RV2 / RV1

            if result is not None:
                stack.stack_push(result)

    # After the expression has been evaluated, there should be one value left on the stack.
    # Return this value as the result of the function.
    return stack.stack_pop()


def evaluate_expression(expression: str):
    # If the expression is less than two characters long, it cannot be evaluated and the function returns (False, 0)
    if len(expression) < 2:
        return (False, 0)
    
    # Create an empty string to hold the RPN expression
    rpn = ''

    # If the last character of the expression is a digit, assume it is an infix expression and convert it to RPN
    # using the shunt function from the sy module
    if expression[-1].isdigit():
        rpn = " ".join(shunt(tokenize(expression)))
    # Otherwise, assume the expression is already in RPN format
    else:
        rpn = expression

    # Use the rpn_eval function to evaluate the RPN expression and catch any exceptions that may occur
    result = 0
    
    try:
        result = rpn_eval(rpn)
    except Exception as e:
        # If an exception is caught, print the RPN expression and the error message and return (False, -1)
        print(rpn, e)
        return (False, -1)

    # If the expression is successfully evaluated, return (True, result)
    return (True, result)


if __name__ == '__main__':
    # Start an infinite loop to allow the user to enter expressions to be evaluated
    while True:
        expression = input('Please enter your expression: ')
        result, ans = evaluate_expression(expression)
        print('=', ans)