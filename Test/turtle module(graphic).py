#import turtle # turtle module ကို import ထုတ်လိုက်ပါတယ်
#turtle.exitonclick()
"""
t = turtle.Turtle() # t = turtle.Turtle() နဲ့ turtle function ကို t အသေးဖြစ် သတ်မှတ် လိုက်ပါတယ်။
t.forward(100)
t.right(90)
t.forward(100)
t.left(90)
t.backward(100)
t.right(90)
t.backward(100)
turtle.exitonclick()

"""
#cicle
"""
turtle.bgcolor("Green")
turtle.title("Hello")
turtle.pensize(15)
turtle.pencolor("blue")
turtle.circle(100)
turtle.exitonclick()
"""
#circle_with_red_color
"""
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()
turtle.exitonclick()
"""
#Draw a triangle with green color
"""
import turtle as t
t.color("black","green")
t.begin_fill()
for i in range(0,3):
    t.forward(100)
    t.left(120)
t.end_fill()
t.exitonclick()
"""
#Draw a square with red color
"""
import turtle as t
t.color("black","red")
t.begin_fill()
for i in range(0,4):
    t.forward(100)
    t.right(90)
t.end_fill()
t.exitonclick()
"""

#Draw a five-point start

import turtle as t
"""
for i in range(0,5):
    t.forward(100)
    t.right(144)
"""
for x in range(0,10):
    for n in range(0,8):
        t.forward(50)
        t.right(45)
        t.right(36)
t.exitonclick()