# Name: Turtlesketch
# Description: Draw simple sketches with console input or a macro file, using the python turtle library
# Author: Nick Roussis (Neek8044)
# Github: https://github.com/neek8044/

# This is a very old project I found on my hard drive. I will try fixing it a little on later commits.

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
        if turtle_shown == 1:
            t.hideturtle()
            turtle_shown = 0
        else:
            t.showturtle()
            turtle_shown = 1

    # Enable/disable pen output
    elif command[0] == "switch":
        if penup == 1:
            t.pendown()
            penup = 0
        else:
            t.penup()
            penup = 1

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


def check_console():
    while True:
        command = input("Command: ").split(" ")
        
        if command[0] == "macro":
            try:
                print("Executing:", command[1])
                with open(command[1]) as macro:
                    for line in macro:
                        execute(line)
            except Exception as ex:
                print("ERROR:", ex, "\n--> Make sure you set the correct path.")
        else:
            execute(command)


turtle_shown = 0
penup = 0

thread = threading.Thread(target=check_console)
thread.start()

turtle.tracer(1,0)
turtle.bgcolor("black")
turtle.left(90)
turtle.mainloop()
