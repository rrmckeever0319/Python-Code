from Tkinter import *
from random import randrange 
master = Tk()

import time

screen = Canvas(master, width = 600, height=600, bg='white')

screen.pack()


creepMovement = (.5)

creepDirection = randrange(1,100)

moveClick = (100)

moveDirectionX = (0)
moveDirectionY = (0)


creepX1 = (100)
creepY1 = (150)
creepXn = (110)
creepYn = (160)


def creep (x1, y1, xn, yn):
    screen.create_oval(x1, y1, xn ,yn, fill=("black"), tag="creep")
                        
    


creep(creepX1, creepY1, creepXn, creepYn )

def startGame(Click):


    global creepX1
    global creepY1
    global creepXn
    global creepYn
    global moveDirectionX
    global moveDirectionY


    moveClickX = Click.x
    moveClickY = Click.y
    



    if moveClickX > creepX1 and moveClickY > creepY1:
        moveDirectionX = (moveClickX/ creepX1)
        
    
        moveDirectionY = (moveClickY/ creepY1)
    
    if moveClickX < creepX1 and moveClickY < creepY1:
        
        moveDirectionX = -(creepX1/ moveClickX)
        
    
        moveDirectionY = -(creepY1/ moveClickY)
 

    while creepX1 != moveClickX and creepY1 != moveClickY:

        creepX1 = (creepX1 + (moveDirectionX ))
        creepXn = (creepXn + (moveDirectionX ))
        
        creepY1 = (creepY1 + (moveDirectionY))
        creepYn = (creepYn + (moveDirectionY))

        creep(creepX1, creepY1, creepXn, creepYn )

        screen.update()

        screen.delete("creep")

        creep(creepX1, creepY1, creepXn, creepYn )

        time.sleep(0.03)

       

        

                
        

    
    
   
                        

    







screen.bind("<Button-1>", startGame)
mainloop()
