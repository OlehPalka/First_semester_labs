from turtle import *

#make body
color("black", "yellow")
begin_fill()
circle(100)
end_fill()

#jump
penup()
goto(-40, 120)
pendown()

#make eye 1
color("black", "white")
begin_fill()
circle(15)
end_fill()
color("black", "black")
begin_fill()
circle(7)
end_fill()

#jump
penup()
goto(40, 120)
pendown()

#make eye 2
color("black", "white")
begin_fill()
circle(15)
end_fill()
color("black", "black")
begin_fill()
circle(7)
end_fill()

#jump
penup()
goto(-40, 85)
pendown()

#make mouth
width(3)
right(90)
circle(40, 180)

done()