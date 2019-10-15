# create turtle and set start speed
import turtle as trtl
turtle = trtl.Turtle()
turtle.speed(0)
turtle.pensize(10)
 
# help yourself in the future
def home(x,y):
 turtle.penup()
 turtle.goto(x,y)
 turtle.pendown()
 
# get input for eye color(s)
print("please choose Red or Blue (R/B)")
if input("B" or "b"):
 color1 = "blue"
else:
 color1 = "red"
print("please choose a second color Purple or Green (P/G)")
if input("P" or "p"):
 color2 = "purple"
else:
  color2 = "Green"
print("please pick a final color Yellow or Orange (Y/O")
if input("Y" or "y"):
  color3 = "yellow"
else:
  color3 = "orange"
 
# choose turtle speed
if (color1 == "blue"):
  turtle.speed(15)
else:
  turtle.speed(5)
  
# move turtle to the bottom with no line
turtle.penup()
home(0,-200)
turtle.pendown()
 
# make turtle face angle and move it set pensize (bottom of the neck)
turtle.pensize(5)
turtle.setheading(30)
turtle.forward(100)
 
# make the side of the neck
turtle.setheading(95)
turtle.forward(150)
 
# make one side of the head
turtle.setheading(80)
turtle.forward(45)
 
# make the rest of the side of the head
turtle.setheading(110)
turtle.forward(100)
 
 # make the wolfs ear
turtle.back(5)
turtle.setheading(80)
turtle.forward(75)
turtle.setheading(135)
turtle.back(25)
turtle.setheading(91)
turtle.back(145)
 
# draw the top of the wolfs head
turtle.setheading(110)
turtle.forward(100)
turtle.setheading(180)
turtle.forward(40)
 
# change turtle.speed based on color2
if (color2 == "purple"):
  turtle.speed(20)
else:
  turtle.speed(10)
# move the turtle to where you want the eyes
turtle.penup()
turtle.setheading(270)
turtle.forward(75)
turtle.setheading(0)
turtle.forward(20)
 
# make the eyes
turtle.pendown()
turtle.circle(10)
turtle.fillcolor("black")
turtle.begin_fill()
turtle.back(15)
turtle.setheading(75)
turtle.forward(17)
turtle.end_fill()
turtle.penup()
turtle.setheading(0)
turtle.forward(20)
turtle.fillcolor("black")
turtle.begin_fill()
turtle.pendown()
turtle.forward(10)
turtle.setheading(-130)
turtle.forward(15)
turtle.end_fill()
 
# make the nose
turtle.penup()
home(2.0739538788184486,45.46298852535172)
turtle.pendown()
turtle.setheading(280)
turtle.forward(50)
turtle.setheading(300)
turtle.forward(25)
turtle.setheading(250)
turtle.forward(25)
turtle.setheading(-200)
turtle.forward(15)
 
# make the snout
turtle.fillcolor("black")
turtle.begin_fill()
turtle.back(15)
turtle.setheading(180)
turtle.forward(30)
turtle.setheading(-340)
turtle.forward(15)
turtle.end_fill()
turtle.setheading(50)
turtle.forward(10)
turtle.setheading(360)
turtle.back(10)
turtle.setheading(310)
turtle.forward(10)
 
# move turtle to the bottom with no line
turtle.penup()
home(0,-200)
turtle.pendown()
 
# make turtle face angle and move it set pensize (bottom of the neck) turtle.pensize(5)
turtle.setheading(150)
turtle.forward(100)
 
# make the side of the neck
turtle.setheading(85)
turtle.forward(150)
 
# make one side of the head
turtle.setheading(100)
turtle.forward(45)
 
# make the rest of the side of the head
turtle.setheading(70)
turtle.forward(100)
 
# make the wolfs ear
turtle.back(5)
turtle.setheading(100)
turtle.forward(75)
turtle.setheading(45)
turtle.back(25)
turtle.setheading(89)
turtle.back(145)
# change the turtle speed based on color3
if (color3 == "yellow"):
  turtle.speed(10)
else:
  turtle.speed(0)
  
# draw the top of the wolfs head
turtle.setheading(70)
turtle.forward(100)
turtle.setheading(0)
turtle.forward(60)
turtle.back(20)
 
# draw the other eye
turtle.penup()
home(-27.881300800891175,63.190610801135)
 
# draw the eyes
turtle.pendown()
turtle.circle(10)
 
turtle.fillcolor("black")
turtle.begin_fill()
turtle.forward(20)
turtle.setheading(140)
turtle.forward(20)
turtle.end_fill()
 
turtle.penup()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.setheading(0)
turtle.back(20)
turtle.pendown()
turtle.back(15)
turtle.setheading(330)
turtle.forward(20)
turtle.end_fill()
 
turtle.speed(0)
turtle.fillcolor("white")
turtle.begin_fill()
home(-31,63.190610801135)
turtle.circle(10)
turtle.end_fill()
 
 # make the nose
turtle.penup()
home(-2.0739538788184486,45.46298852535172)
turtle.pendown()
turtle.setheading(260)
turtle.forward(50)
turtle.setheading(240)
turtle.forward(25)
turtle.setheading(290)
turtle.forward(25)
turtle.setheading(-340)
turtle.forward(15)
 
# change the eyecolor repeatedly
turtle.speed(0)
counter1 = 0
while (counter1 <= 5):
  turtle.fillcolor(color1)
  turtle.begin_fill()
  home(-27.881300800891175,63.190610801135)
  turtle.circle(10)
  turtle.end_fill()
  turtle.fillcolor(color2)
  turtle.begin_fill()
  home(27.881300800891175,63.190610801135)
  turtle.circle(10)
  turtle.end_fill()
  counter1 += 1
  counter2 = 0
 
  while (counter2 <= 3):
    turtle.fillcolor(color1)
    turtle.begin_fill()
    home(27.881300800891175,63.190610801135)
    turtle.circle(10)
    turtle.end_fill()
    
    turtle.fillcolor(color3)
    turtle.begin_fill()
    home(-27.881300800891175,63.190610801135)
    turtle.circle(10)
    turtle.end_fill()
    counter2 += 1
    counter3 = 0
    
    while (counter3 <= 1):
      turtle.fillcolor(color2)
      turtle.begin_fill()
      home(-27.881300800891175,63.190610801135)
      turtle.circle(10)
      turtle.end_fill()
      
      turtle.fillcolor(color3)
      turtle.begin_fill()
      home(27.881300800891175,63.190610801135)
      turtle.circle(10)
      turtle.end_fill()
      counter3 += 1
  
  # make the screen freeze
wn = trtl.Screen()
wn.mainloop()
