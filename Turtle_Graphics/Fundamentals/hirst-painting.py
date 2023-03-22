import colorgram
import turtle as t
import random
# rgb_colors = []
# colors = colorgram.extract('/Users/sanghyunryu/Desktop/Sanghyun Ryu/Scripts/100_days_of_code/Turtle_Graphics/image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

t.colormode(255)
tim = t.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
color_list = [(217, 151, 104), (121, 165, 207), (40, 105, 164), (204, 67, 22), (211, 132, 155), (238, 208, 88), (151, 62, 92), (118, 194, 156), (233, 77, 47), (220, 71, 101), (29, 131, 61), (190, 159, 36), (36, 47, 133), (151, 23, 46), (170, 20, 10), (24, 23, 67), (102, 112, 181), (241, 164, 154), (5, 107, 35), (236, 166, 181), (157, 211, 188), (61, 24, 37), (69, 23, 16), (53, 166, 138), (170, 184, 226), (246, 203, 0)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count %10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = t.Screen()
screen.exitonclick()

