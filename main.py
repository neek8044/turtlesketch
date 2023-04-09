# Name: Turtlesketch
# Description: Draw simple sketches with console input or a macro file, using the python turtle library
# Author: Nick Roussis (Neek8044)
# Github: https://github.com/neek8044/
# License: Apache 2.0


import turtle as turtle
import threading


__banner__ = """
Coded by Nick Roussis (Neek8044)
License: Apache 2.0
Github: https://github.com/neek8044/turtlesketch

COMMANDS:
\tmove [pixels] - Move forward for specified distance, backward with a negative
\tturn [degrees] - Turn right for specified degrees, left with a negative
\ttoggle - Toggle to show pointer (pen position/rotation); useful with complex sketches
\tswitch - Switch between normal and blank output (pen down/pen up)
\tcolor [color] - Sets brush color to specified (hex supported); Black can be used as an eraser
\tmacro [path to file] - Runs a macro file. Check the Github for more information about macros (look above)
"""


t = turtle.Turtle()
t.hideturtle()
t.pensize(5)
t.color("white")
t.pendown()

print(__banner__)


def execute(command):
    global turtle_shown
    global penup

    # Toggle pointer (turtle) on/off
    if command[0] == "toggle":
        if turtle_shown == True:
            t.hideturtle()
            turtle_shown = False
        else:
            t.showturtle()
            turtle_shown = True

    # Enable/disable pen output
    elif command[0] == "switch":
        if penup == True:
            t.pendown()
            penup = False
        else:
            t.penup()
            penup = True

    # Change color based on given value
    elif command[0] == "color":
        try:
            t.color(command[1])
        except turtle.TurtleGraphicsError:
            print("ERROR: Invalid input value.")

    # Move forward (or backward with a negative value)
    elif command[0] == "move":
        try:
            t.forward(int(command[1]))
        except ValueError:
            print("ERROR: Invalid input value.")

    # Turn clockwise (or counter-clockwise with a negative value)
    elif command[0] == "turn":
        try:
            t.right(int(command[1]))
        except ValueError:
            print("ERROR: Invalid input value.")

    # If no valid commands were met, print the following.
    else:
        print("--> Please check spelling and try again.")


class console:
    def execute_macro(command):
        print("Executing:", command[1])
        with open(command[1]) as macro:
            for line in macro:
                line = line.replace("\n", "")
                execute(line.split(" "))

    def parse():
        command = input("Command: ").split(" ")
        if command[0] == "macro":
            try:
                console.execute_macro(command)
            except FileNotFoundError:
                print("--> Please set the correct path.")
            except IndexError:
                print("--> Please set a path.")
        else:
            execute(command)

    def check():
        while True:
            console.parse()


turtle_shown = False
penup = False

thread = threading.Thread(target=console.check)
thread.start()

turtle.tracer(1,0)
turtle.bgcolor("black")
turtle.left(90)
turtle.mainloop()
