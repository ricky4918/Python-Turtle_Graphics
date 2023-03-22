from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=1500, height=800)

# Store the colors and y-axis positions
colors = ["red", "orange", "green", "yellow", 'blue', 'DarkBlue',
          "DarkMagenta", "DeepPink", 'cyan']
y_positions = [280, 210,140, 70, 0, -70, -140, -210, -280]

# Create the turtles and set their attributes
all_turtles = []
for turtle_index in range(len(y_positions)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.speed('fastest')
    new_turtle.shapesize(stretch_wid=3.5, stretch_len=3.5)
    new_turtle.goto(x=-680, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

is_race_on = True
# Move the Turtles
while is_race_on:
    for turtle in all_turtles:
        # Turtle has crossed the finish line
        if turtle.xcor() > 680:
            is_race_on = False
            winning_color = turtle.pencolor()

            print(f"The {winning_color} turtle is the winner!")

        # Move the turtle
        rand_distance = random.randint(0, 20)
        turtle.forward(rand_distance)
count = 0
lst = []
for turtle in all_turtles:
    lst.append(turtle.xcor())
    print(f"turtle({colors[count]}): {turtle.xcor()}")   
    count += 1   

min_index = lst.index(min(lst))
print(f"The last turtle is : turtle({colors[min_index]})")


# Exit Screen on click
screen.exitonclick()
