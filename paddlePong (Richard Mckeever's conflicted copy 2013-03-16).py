from Tkinter import *
master = Tk()

import time


frame = Canvas(master, width=1000, height=600, bg="black")

frame.pack()

frame.create_rectangle(50, 50, 950, 500, outline="white")
frame.create_line(500, 50, 500, 500, fill="white", dash=(2,4))

paddle1positionY1 = (325)
paddle1positionYn = (275)

paddle2positionY1 = (325)
paddle2positionYn = (275)



gameBallX1 = (505)
gameBallY1 = (260)
gameBallXn = (495)
gameBallYn = (270)

gameBallHorizontalDirection = (3)

gameBallVerticalDirection = (3)


#game Objects
def gameBall (x1, y1, xn, yn):
    frame.create_rectangle(x1, y1, xn, yn, fill="white", tag="gameBall")

def player1paddle (x1, y1, xn, yn):
    frame.create_rectangle(x1, y1, xn, yn, fill="white", tag="paddle1")

def player2paddle (x1, y1, xn, yn):
    frame.create_rectangle(x1, y1, xn, yn, fill="white", tag="paddle2")


#creating starting position of objects

gameBallSpeed = (0.02)


gameBall(gameBallX1, gameBallY1, gameBallXn , gameBallYn)

player1paddle(100, paddle1positionY1, 115, paddle1positionYn)
player2paddle(900, paddle2positionY1, 885, paddle2positionYn)


     

frame.focus_set()


def mouseClick(Click):

    global paddle1positionY1 
    global paddle1positionYn  #player paddle Coordinates 

    global paddle2positionY1  
    global paddle2positionYn   

    

    


    global gameBallSpeed     
    

    global gameBallX1 
    global gameBallY1 
    global gameBallXn 
    global gameBallYn 

    global gameBallHorizontalDirection  
    global gameBallVerticalDirection  

    gameBallSpeed = (gameBallSpeed - 0.005)

    



    while gameBall > 0:
        
            if gameBallX1 < (55) or (gameBallX1 <= (115) and gameBallY1 < paddle1positionY1 and gameBallYn > paddle1positionYn ) :
                gameBallHorizontalDirection = (-3) #if it hits the left wall

            if gameBallXn > (945) or (gameBallX1 >= (885) and gameBallY1 < paddle2positionY1 and gameBallYn > paddle2positionYn) : #If it hits the right wall
                gameBallHorizontalDirection = (3)

           
            if gameBallY1 < (58):
                gameBallVerticalDirection = (-3)

        if gameBallYn > (500):
        gameBallVerticalDirection = (3)
                

        

 
                
            


                
            #gameBall movement
            gameBallX1 = (gameBallX1 - (gameBallHorizontalDirection))
            gameBallXn = (gameBallXn - (gameBallHorizontalDirection))
            
            gameBallY1 = (gameBallY1 - (gameBallVerticalDirection))
            gameBallYn = (gameBallYn - (gameBallVerticalDirection))
           


            gameBall(gameBallX1, gameBallY1, gameBallXn , gameBallYn)

            frame.update()
  
            frame.delete("gameBall")
            
            time.sleep(gameBallSpeed )
    


paddle1and2Speed = (8) # How fast both paddle move up and down in pixels

#player 1 movement
def player1upKey(Up): # paddle 1 moving Up
    global paddle1Speed 
    
    global paddle1positionY1
    global paddle1positionYn

    if paddle1positionYn > 53:
        paddle1positionY1 = (paddle1positionY1 - (paddle1and2Speed))
        paddle1positionYn = (paddle1positionYn - (paddle1and2Speed))
    
    frame.delete("paddle1")
    player1paddle(100, paddle1positionY1, 115, paddle1positionYn)
    
def player1downKey(Down): # paddle 1 moving Down
    global paddle1and2Speed
    global paddle1positionY1 
    global paddle1positionYn

    if paddle1positionY1 < 497:
        paddle1positionY1 = (paddle1positionY1 + (paddle1and2Speed))
        paddle1positionYn = (paddle1positionYn + (paddle1and2Speed))

    frame.delete("paddle1")
    player1paddle(100, paddle1positionY1, 115, paddle1positionYn)
    
    #player 2 movement


def player2upKey(Up):
    global paddle1and2Speed
    global paddle2positionY1 
    global paddle2positionYn

    if paddle2positionYn > 53 :
        paddle2positionY1 = (paddle2positionY1 - (paddle1and2Speed))
        paddle2positionYn = (paddle2positionYn - (paddle1and2Speed))

    frame.delete("paddle2")
    player2paddle(900, paddle2positionY1, 885, paddle2positionYn)
    


def player2downKey(Down):
    global paddle1and2Speed
    global paddle2positionY1 
    global paddle2positionYn

    if paddle2positionY1 < 490:
        paddle2positionY1 = (paddle2positionY1 + (paddle1and2Speed))
        paddle2positionYn = (paddle2positionYn + (paddle1and2Speed))

    frame.delete("paddle2")
    player2paddle(900, paddle2positionY1, 885, paddle2positionYn)



     

   
frame.bind("<Button-1>", mouseClick)

frame.bind("<Up>", player2upKey)
frame.bind("<Down>", player2downKey)

frame.bind("<w>", player1upKey)
frame.bind("<s>", player1downKey)

frame.pack()
mainloop()
