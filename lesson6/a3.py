# 1) Import the `turtle` library to use turtle graphics.
import turtle
# 2) Create a turtle screen window and store it in `my_wn`.
my_wn = turtle.Screen()
# 3) Set up the screen:
#    a) Change the background color to "light blue".
#    b) Set the window title to "Turtle".
my_wn.bgcolor("light blue") 
my_wn.title("Turtle")
# 4) Create a Turtle object and store it in `my_pen`.
#    (This turtle will draw the pattern.)
my_pen = turtle.Turtle()
# 5) Initialize `size = 0`.
#    (This variable controls how long each side of the square will be.)
size = 0
# 6) Start an infinite loop using `while True` so the drawing continues forever.
while True:
    for i in range(4):
        my_pen.forward(size+1)
        my_pen.right(90)
        size = size-5
    size = size+1

# 7) Inside the infinite loop, draw a square using a `for` loop that runs 4 times:
#    a) Move the turtle forward by `size + 1`.
#    b) Turn the turtle left by 90 degrees to make a right angle.
#    c) Decrease `size` by 5 after each side.

# 8) After completing one square (4 sides), increase `size` by 1.
#    (This changes the size value for the next iteration, creating a repeating pattern.)