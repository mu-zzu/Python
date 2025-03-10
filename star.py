from turtle import Turtle

def star(t,length):
    t.down()
    t.right(72)
    t.forward(length)
    t.right(144)
    t.forward(length)
    t.right(144)
    t.forward(length)
    t.right(144)
    t.forward(length)
    t.right(144)
    t.forward(length)
    t.right(72)

def pattern(t,radius,length,shape,num):
    angle=360/num
    for i in range (num):
        t.up()
        currentangel=i*angle
        t.right(currentangel)
        t.forward(radius)
        t.left(currentangel)
        t.down()
        shape(t,length)
        t.up()
        t.home()



num=int(input("Enter the number of star:"))
length=int(input("Enter the length of the sizes of the star:"))
radius=2*length
t=Turtle()
t.speed(1)
pattern(t,radius,length,star,num)