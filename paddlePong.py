# Alexander McKeever
# 03/28/2013
# ping pong
from Tkinter import *
master = Tk()

import time



frame = Canvas(master, width=1000, height=600, bg="black")

frame.pack()



#Game board 
frame.create_rectangle(50, 50, 950, 500, outline="white")
frame.create_line(500, 50, 500, 500, fill="white", dash=(6,6))

frame.create_rectangle(40, 220 ,50, 320, fill='black')
frame.create_rectangle(950, 220, 960, 320, fill='black')


ballActive = (True)

paddle1positionX1 = (100)
paddle1positionXn = (115)
paddle1positionY1 = (325)
paddle1positionYn = (275)


paddle2positionX1 = (885)
paddle2positionXn = (900)
paddle2positionY1 = (325)
paddle2positionYn = (275)


#Starting position of the ball
gameBallX1 = (505)
gameBallY1 = (260)
gameBallXn = (495)
gameBallYn = (270)




ballColorVar= (0)

gameBallColor = ('white')
numberColor = ('white')

#speed at which the frame updates
gameBallSpeed = (0.0225)


# amount of pixels moved up or down each time the frame updates
gameBallHorizontalDirection = (3)

gameBallVerticalDirection = (3)


player1Score = (0)
player2Score = (0)


#game Objects
def gameBall (x1, y1, xn, yn):
    frame.create_rectangle(x1, y1, xn, yn, fill=(gameBallColor), tag="gameBall")

def player1paddle (x1, y1, xn, yn):
    frame.create_rectangle(x1, y1, xn, yn, fill="white", tag="paddle1")

def player2paddle (x1, y1, xn, yn):
    frame.create_rectangle(x1, y1, xn, yn, fill="white", tag="paddle2")


#creating starting position of objects

gameBall(gameBallX1, gameBallY1, gameBallXn , gameBallYn)

player1paddle(paddle1positionX1, paddle1positionY1, paddle1positionXn, paddle1positionYn)
player2paddle(paddle2positionX1, paddle2positionY1, paddle2positionXn, paddle2positionYn)


frame.focus_set()


#Reset Button

def restartGameball():
    global ballActive 
    global gameBallX1 
    global gameBallY1 
    global gameBallXn 
    global gameBallYn

    global gameBallHorizontalDirection
    global gameBallVerticalDirection

    if ballActive == (False):
        gameBallX1 = (505)
        gameBallY1 = (260)
        gameBallXn = (495)
        gameBallYn = (270)

        gameBallHorizontalDirection = (3)
        gameBallVerticalDirection = (3)
        
        
        gameBall(gameBallX1, gameBallY1, gameBallXn , gameBallYn)
        ballActive = (True)
        
    


b = Button(master, text="Reset", command=restartGameball)
b.pack()



def mouseClick(Click):
    
    

    print(Click.x, Click.y)


    global ballActive
    global player1Score
    global player2Score	
    global colorMode 
    global ballColorVar

    global gameBallColors
    global gameBallColor
    global gameBallSpeed 

    global paddle1positionY1 
    global paddle1positionYn  #player paddle Coordinates 

    global paddle2positionY1  
    global paddle2positionYn   



    global gameBallX1 
    global gameBallY1 
    global gameBallXn 
    global gameBallYn 

    global gameBallHorizontalDirection  
    global gameBallVerticalDirection  

 
# gameball X1 is the left side of the gameball and gameball Xn is the right side

    while ballActive == (True):

        
            if gameBallXn <= (45) and ballActive == (False):
                player2Score = (player2Score + 1 )
                print (player2Score)

                
          
            if gameBallXn <= 50 :
                ballActive = (False)             
         
              

	    

            


                            
            if (gameBallXn <= (50) and gameBallY1 < (219)) or (gameBallXn <= (115) and gameBallY1 < paddle1positionY1 and gameBallYn > paddle1positionYn ):
                gameBallHorizontalDirection = (-3)
		
		
						 #if it hits the left wall or the left paddle
		

            if (gameBallX1 >= (950) and gameBallY1 < (219)) or  (gameBallXn <= 50 and gameBallY1 > (320)) or (gameBallX1 >= (885) and gameBallY1 < paddle2positionY1 and gameBallYn > paddle2positionYn) :
               gameBallHorizontalDirection = (3) #If it hits the right wall or the right paddle
            		
         
            if gameBallY1 <= (50)  :  #ceiling and floor Collisions 
		gameBallVerticalDirection = (-3)
		

	    if gameBallYn >= (500):
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
	






	    
paddle1and2Speed = (9) # How fast both paddle move up and down in pixels

#player 1 movement
def player1upKey(Up): # paddle 1 moving Up
	global paddle1Speed 
	
	global paddle1positionY1
	global paddle1positionYn

	if paddle1positionYn >= 53:
		paddle1positionY1 = (paddle1positionY1 - (paddle1and2Speed))
		paddle1positionYn = (paddle1positionYn - (paddle1and2Speed))
	
	frame.delete("paddle1")
	player1paddle(100, paddle1positionY1, 115, paddle1positionYn)
	
def player1downKey(Down): # paddle 1 moving Down
	global paddle1and2Speed
	global paddle1positionY1 
	global paddle1positionYn

	if paddle1positionY1 <= 493:
		paddle1positionY1 = (paddle1positionY1 + (paddle1and2Speed))
		paddle1positionYn = (paddle1positionYn + (paddle1and2Speed))

	frame.delete("paddle1")
	player1paddle(100, paddle1positionY1, 115, paddle1positionYn)
	
	#player 2 movement


def player2upKey(Up):
	global paddle1and2Speed
	global paddle2positionY1 
	global paddle2positionYn

	if paddle2positionYn >= 53 :
		paddle2positionY1 = (paddle2positionY1 - (paddle1and2Speed))
		paddle2positionYn = (paddle2positionYn - (paddle1and2Speed))

	frame.delete("paddle2")
	player2paddle(900, paddle2positionY1, 885, paddle2positionYn)
	


def player2downKey(Down):
	global paddle1and2Speed
	global paddle2positionY1 
	global paddle2positionYn

	if paddle2positionY1 <= 490:
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
