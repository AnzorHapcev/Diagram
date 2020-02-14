import turtle
import math

lang = ['C++', 'Python', 'Java', 'Python', 'PHP', 'C++', 'Python', 'C++', 'PHP', 'Java', 'Java', 'Java']
dct = {}


def analysis():
    for i in lang:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1


analysis()

pet = turtle.Turtle()
pet.screen.setup(1000, 800)
pet.up()
pet.width(2)


def draw_diagram(height_diagram):
    pet.down()
    m = 2
    while m > 0:
        pet.fd(60)
        pet.left(90)
        pet.fd(height_diagram)
        pet.left(90)
        m -= 1
    pet.up()


pet.goto(0, 0)
color = ['green', 'blue', 'pink', 'yellow', 'brown']
n = 0

for i in sorted(dct):
    pet.pencolor(color[n])
    pet.fillcolor(color[n])
    pet.begin_fill()
    draw_diagram((400*dct[i])/len(lang))
    pet.end_fill()
    pet.pencolor('black')
    pet.fd(5)
    pet.write(int((100 * dct[i]) / len(lang)), move=False, align="left")
    pet.fd(12)
    pet.write('%', move=False, align="left")
    pet.fd(12)
    pet.write(i, move=False, align="left")
    pet.fd(55)
    n += 1
n = 0
pet.goto(-200, 0)
for i in sorted(dct):
     pet.pencolor(color[n])
     pet.fillcolor(color[n])
     pet.begin_fill()
     degree = int((360 * dct[i]) / len(lang))
     pet.circle(150, degree)
     pet.end_fill()
     n += 1

pet.hideturtle()
pet.screen.exitonclick()
pet.screen.mainloop()
