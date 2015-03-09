from Tkinter import *
master = Tk()

import time


frame = Canvas(master, width=1000, height=600, bg="black")

frame.pack()

frame.create_rectangle(50, 50, 950, 500, outline="white")
frame.create_line(500, 50, 500, 500, fill="white", dash=(2,4))

paddle1positionY1 = (325)
paddle1positionYn = (275)



gameBallX1 = (505)
gameBallY1 = (260)
gameBallXn = (495)
gameBallYn = (270)


text = Text(master)
text.insert(INSERT,(gameBallX1, gameBallY1 ))
text.pack()





#game Objects
def gameBall (x1, y1, xn, yn):
    frame.create_rectangle(x1, y1, xn, yn, fill="white", tag="gameBall")

def player1paddle (x1, y1, xn, yn):
    frame.create_rectangle(x1, y1, xn, yn, fill="white", tag="player1paddle")

def player2paddle (x1, y1, xn, yn):
    frame.create_rectangle(x1, y1, xn, yn, fill="white", tag="player2paddle")


#creating starting position of objects

player1paddle(100, paddle1positionY1, 115, paddle1positionYn)

gameBall(gameBallX1, gameBallY1, gameBallXn , gameBallYn)


     



def mouseClick(Click):
    
	
	


		 
   
    gameStart = (1)

    global gameBallX1 
    global gameBallY1 
    global gameBallXn 
    global gameBallYn 

    gameBallHorizontalDirection = (3)
    gameBallVerticalDirection = (3)

    



    while gameBall > 0:
        
            if gameBallX1 < (55) or gameBallX1 == (115) :
                gameBallHorizontalDirection = (-3) #if it hits the left wall

            if gameBallXn > (945): #If it hits the right wall
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
            
            time.sleep(0.02)
	

def playerMove(click):
	text.insert(INSERT,("Hello"))
	text.pack()


     

   
frame.bind("<Up>", playerMove)
frame.bind("<Button-1>", mouseClick)

mainloop()
