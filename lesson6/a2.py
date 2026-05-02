# 1) Import the `turtle` library to draw using the turtle graphics window.
import turtle
# 2) Set the turtle screen background color to "Aqua".
turtle.Screen().bgcolor("aqua")
# 3) Create a Turtle object and store it in `board`.
#    (This turtle will draw the star shape.)
board = turtle.Turtle()
# 4) Draw the first triangle:
#    a) Move forward 100 units to draw the base.
#    b) Turn left 120 degrees and move forward 100 units.
#    c) Turn left 120 degrees and move forward 100 units.
#    (This completes an equilateral triangle.)
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)

# 5) Lift the pen up using `penup()` so the turtle can move without drawing.
board.penup()
# 6) Reposition the turtle to start the second triangle:
#    a) Turn right 150 degrees.
#    b) Move forward 50 units.
board.right(150)
board.forward(50)
# 7) Put the pen down using `pendown()` to start drawing again.
board.pendown()
# 8) Draw the second triangle:
#    a) Turn right 90 degrees and move forward 100 units.
#    b) Turn right 120 degrees and move forward 100 units.
#    c) Turn right 120 degrees and move forward 100 units.
#    (This overlaps with the first triangle to form a star shape.)
board.right(90)
board.forward(100)
board.right(120)
board.forward(100)
board.right(120)
board.forward(100)
# 9) Call `turtle.done()` to keep the turtle window open after drawing finishes.
turtle.done()