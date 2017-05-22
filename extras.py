# extras.py
# Includes various functions and code that all seperate simulations may need to make use of preventing code repitition
# Ethan Peterson
# April 19, 2017


# Function to handle exiting the simulation

# scene parameter takes scene object to properly close the window and detect key presses when that window is selected
def exitOnKeyPress(scene): # exits the simulation when the user presses the escape key
    if scene.kb.keys: # wait for key event to be processed
        key = scene.kb.getkey() # get last key to be to be pressed
        if key == 'esc': # if the user pressed the escape key exit the program
            exit()
        elif key == ' ':
            while True:
                ev = scene.waitfor('keydown')
                if ev.key == 'p':
                    break
                
                

