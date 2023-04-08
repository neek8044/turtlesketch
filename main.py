# Name: Turtlesketch
# Description: Draw simple sketches with console input or macro file, using the turtle library
# Author: Nick Roussis (Neek8044)
# Github: https://github.com/neek8044/

# This is a very old project I found on my hard drive. I will try fixing it a little on later commits.

import turtle as turtle
from threading import Thread

t = turtle.Turtle()

########################################

# future me here. i have no idea why i used separate functions to parse input
class cli:
	def run(command):
		out = None
		command = command.split(" ")

		if command[0] == "turn":
			out = "$" + command[1]

		elif command[0] == "go":
			out = "!" + command[1]

		elif command[0] == "toggle":
			out = "toggle"

		elif command[0] == "switch":
			out = "switch"

		elif command[0] == "set":
			out = "&" + command[1]

		else:
			return "error"
		return out

def check_console():
	tur_shown = 0
	penup = 0

	print(
		"""
		MADE BY NEEK8044
                                                                   
		COMMANDS:
		\tgo [pixels] - Forwards for specified distance, backwards with a negative
		\tturn [degrees] - Right for specified degrees, left with a negative
		\ttoggle - Toggle to show drawing pointer; useful with complex sketches
		\tswitch - Switch between normal and blank output (pen down/pen up)
		\tset [color] - Sets brush to specified color; Black can be used as an eraser

		"""
	)

	####################

	while True:
		out = cli.run(input("Command: "))

		if out == "error":
			print("Please check spelling and try again.")

		elif out == "toggle":
			if tur_shown == 1:
				t.hideturtle()
				tur_shown = 0
			else:
				t.showturtle()
				tur_shown = 1

		elif out == "switch":
			if penup == 1:
				t.pendown()
				penup = 0
			else:
				t.penup()
				penup = 1
		
		# future me here. i have no idea why i used symbols here
		elif out[0] == "&":
			out = out.replace("&", "")
			t.color(out)

		elif out[0] == "!":
			out = out.replace("!", "")
			t.forward(int(out))

		elif out[0] == "$":
			out = out.replace("$", "")
			t.right(int(out))

########################################

t.hideturtle()
t.tracer(1,0)
t.pensize(5)

t.color("white")
t.bgcolor("black")

t.pendown()

t = Thread(target=check_console)
t.start()

t.left(90)

t.mainloop()