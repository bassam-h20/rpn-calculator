
<h1 align="center"> Reverse Polish Notation Calculator </h1>




By: Yousef Ali (22002656), Bassam Ali (2100000)
---------------------

We have implemented a RPN calculator by using our raspberry pi 0 to manipulate our matrix keypad and oled screen. We have also built a library for the oled screen.


<h1 align="center"> Instructions to run </h1>


1. Compile and Install Library: Run <mark>cd oled_lib </mark>, then run <mark>python setup.py</mark>
2. Now you can run the main file using <mark>python main.py</mark>


# Software (Task 1)

The software for the RPN calculator is written in Python and is split into several modules:

main.py: This is the main module that runs the RPN calculator. It initializes the keypad and OLED display, and then enters a loop that waits for user input. When the user enters a number or operator, the program performs the appropriate action (e.g. pushing the number onto the stack or performing the calculation) and updates the display accordingly.
keypad.py: This module contains the code for reading input from the keypad. It uses the gpiozero library to listen for keypress events and maps the keys to their corresponding numbers and operators.
display.py: This module contains the code for updating the OLED display. It uses the adafruit_ssd1306 library to create a display object and writes text to the display using the text() method.

![Step 3](./Images/flag_working.png)

# Hardware components (Task 2)

Components Used: 

* Raspberry pi zero w 
* 4 x 4 Matrix Keypad 
* 64 x 32 pixel OLED screen 


<img src="./images/Hardware.JPG" alt="My Image" width="200" align="center">

<h1 align="left"> Stack Implementation  </h1>

The RPN calculator uses a stack data structure to perform the calculations. The stack is initialized as an empty list at the start of the program.


![Step 4](./Images/Lost_submit.png)


<h1 align="left"> Written Tests  </h1>




![Step 5](./Won.png)
<h1 align="left"> UML diagram  </h1>
![Step 2](./submit2.png)












![Step 6](./gamefunction.png)




![Step 7](./Error1.png)






