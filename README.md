# Turtlesketch 🐢

**Draw simple sketches with console input or a macro file, using the python turtle library**

License: [Apache 2.0](/LICENSE)

### Commands
- move [pixels] - Move forward for specified distance, backward with a negative
- turn [degrees] - Turn right for specified degrees, left with a negative
- toggle - Toggle to show pointer (pen position/rotation); useful with complex sketches
- switch - Switch between normal and blank output (pen down/pen up)
- color [color] - Sets brush color to specified (hex supported); Black can be used as an eraser
- macro [path to file] - Runs a macro file.

### Macro file
To use a macro, give the command `macro path/to/file.x`. 

The extension does not matter, but each command has to be separated by a new line, like this:
```arduino
move 100
turn 90
move 100
turn 90
move 100
turn 90
move 100
```
(this creates a square)
