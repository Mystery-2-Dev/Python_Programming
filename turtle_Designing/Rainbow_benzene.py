#Using tutle library to build a rainbow benzene design

from turtle import *
colors = ['red', 'violet', 'blue', 'green', 'orange', 'yellow']  #You can have colours of your choice
obj=Turtle()  #turtle object
Sc=Screen() #screen object
Sc.bgcolor("black")
for i in range(360):
    obj.pencolor(colors[i%6])
    obj.width(i/100+1)
    obj.forward(i)
    obj.left(59)
    
# try  changing values in the lines(9-12)and observe changing design.

# Try building new simple designs

# contributed by -Abhinav Pathak.
   
        
 
