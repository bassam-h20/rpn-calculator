from rpn import rpn_eval

def test_addition():
    calculator = rpn_eval('5 10 +')
    assert calculator == 15

def test_subtraction():
    calculator = rpn_eval('5 10 -')
    assert calculator == -5

def test_multiplication():
    calculator = rpn_eval('5 10 *')
    assert calculator == 50

def test_division():
    calculator = rpn_eval('10 2 /')
    assert calculator == 5.0
