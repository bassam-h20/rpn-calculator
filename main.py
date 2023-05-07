import RPi.GPIO as GPIO
import oled_lib
import time
from sy import tokenize, shunt


class Stack():
    def __init__(self):
        self.value = []
        
    def push(self, elem):
        self.value.append(elem)
    
    def pop(self):
        return self.value.pop()
    
    def top(self):
        return self.value[-1] if len(self.value) > 0 else None

    def empty(self):
        return len(self.value) == 0
    
    def print_elem(self):
        print(self.value)

class rpn():
    def check_rpn(input: str) -> int:
        for char in input:
            if char.isdigit():
                string += char
            if char in ['-','+','*',"/"]:
                num1 = Stack.pop()
                num2 = Stack.pop()
                
                print("First Number:",num1,"\nSecond Number:",num2)
                
                final_value = 0
                
                if char == "-":
                    final_value = num1 - num2
                elif char == "+":
                    final_value = num1 + num2
                elif char == "*":
                    final_value = num1 * num2
                elif char == "/":
                    final_value = num1 / num2
                
                if final_value != None:
                    Stack.push(final_value)

        return Stack.pop()
        
    def check_string(self, input: str):
        if len(input) < 2:
            return(False)
        
        rpn_string = ''
        
        if input[-1].isdigit():
            rpn_string = "".join(shunt(tokenize(input)))
        else:
            rpn_string = input
        
        final_value = 0
        
        """try:
            final_value = rpn.check_rpn()
        except Exception as e:
            print(rpn, e)
        """
        return True
            
        

class matrix:
    def __init__(self, rows, cols, keypad):
        self.rows = rows
        self.cols = cols
        self.keypad = keypad  
        self.state = []
        self.state2 = []
        for i in 4:
            self.state.append([False,False,False,False])
            self.state2.append([False,False,False,False])
        self.setup()
    
    def setup(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        for row in self.rows:
            GPIO.setup(row, GPIO.OUT)
            GPIO.output(row, GPIO.HIGH)

        for col in self.cols:
            GPIO.setup(col, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def get_key(self):
        for i in range(len(self.rows)):
            GPIO.output(self.rows[i], GPIO.LOW)
            for j in range(len(self.cols)):
                if GPIO.input(self.cols[j]) == GPIO.LOW:
                    key = self.keypad[i][j]
                    while GPIO.input(self.cols[j]) == GPIO.LOW:
                        time.sleep(0.01)  # wait for key release
                    GPIO.output(self.rows[i], GPIO.HIGH)
                    return key
            GPIO.output(self.rows[i], GPIO.HIGH)
        return None
    
    def button_state(self):
        state_result = []
        for i in 4:
            GPIO.output(self.column[i], GPIO.LOW)
            for j in 4:
                self.state
            
    def pressed(self, row, col):
        return self.state[row][col]
    
    
    def calc_func(string):
        full_value, value = rpn.check_string(string)
        if full_value != None:
            return f'={value}'
        else:
            return f''
        
        

ROW_PINS = [12, 20, 21, 5]
COL_PINS = [6, 13, 19, 26]

MATRIX =[
    [1, 2, 3, '-'],
    [4, 5, 6, '+'],
    [7, 8, 9, '*'],
    ['>', 0, '#', '/']]


if __name__ == "__main__":
    prog_control = False
    oled_lib.__init__(ROW_PINS, COL_PINS, MATRIX)
    button_value = matrix.get_key()
    input_string = ''
    value_string = ''
    Stack_string = ''
    #screen_clear()
    while prog_control != True:
        if button_value != None:
            
            if button_value == ">":
                Stack_string += button_value
                input_string = ""
                value_string = ""
                #screen_clear()
                #continue
            
            elif button_value == "#":
                Stack_string += button_value
                input_string = input_string[:-1]
                #screen_clear()
                
            elif  button_value <= 999:
                input_string += button_value
                Stack_string = ""
            
            else:
                input_string += button_value
                Stack_string = ''
                
            value_string = matrix.calc_func(input_string)
            
            oled_lib.oledWriteString(2, 1, input_string[0:32], 0)
            
            if len(Stack_string) == 2 and Stack_string[0] != Stack_string[1]:
                print("\n\nError Occured, try again.")
                prog_control = True
            time.sleep(0.5)
            
    #oled_lib.shutdown()
            
                
            
                