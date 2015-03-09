
from Tkinter import *
master = Tk()

gameboard = Canvas(master, width=300, height=300) #Window size

gameboard.pack()

gameboard.create_line(100, 0, 100, 300) #Tic tac to board
gameboard.create_line(200, 0, 200, 300)
gameboard.create_line(0, 100, 300, 100)
gameboard.create_line(0, 200, 300, 200)


 # variable for determining turn

    
playerTurn = (2)
square1 = (0)
square2 = (0)
square3 = (0)
square4 = (0)
square5 = (0)
square6 = (0)
square7 = (0)
square8 = (0)
square9 = (0)

#For determining a win for X
Xa = (0)
Xb = (0)
Xc = (0)
Xa1 = (0)
Xb1 = (0)
Xc1 = (0)
Xa2 = (0)
Xb2 = (0)

Oa = (0)
Ob = (0)
Oc = (0)
Oa1 = (0)
Ob1 = (0)
Oc1 = (0)
Oa2 = (0)
Ob2 = (0)



        
def oxMoves  (playerMove):
    global playerTurn
    global square1 #for not allowing double placements
    global square2 
    global square3 
    global square4 
    global square5 
    global square6  
    global square7  
    global square8
    global square9
    
    #for determining a win for X's
    global Xa 
    global Xb 
    global Xc 
    global Xa1 
    global Xb1 
    global Xc1 
    global Xa2 
    global Xb2 

    #for determining a win for O's
    global Oa # for a win straight across the top
    global Ob #for a win straight across the midlle
    global Oc #for a win straight across the bottom
    global Oa1 #for a win straight down the left
    global Ob1 #for a win straight down the middle
    global Oc1 #for a win straight down the right
    global Oa2  #for a win diagonally from the upper left to the bottom right
    global Ob2 #for a win diagonally from the bottom left to the upper right

    
    #while loop for O's
    while (playerTurn == 0):
        playerTurn = (playerTurn + 1)

        
  #while loop for X's 
    while (playerTurn == 3):
        playerTurn = (playerTurn - 1)


    #OMoves
        #O position left 1 
    if   playerTurn == (1) and playerMove.x < 100 and playerMove.y < 100 and square1 == (0) :
        gameboard.create_oval(5, 5, 95, 95, outline="Blue")
        playerTurn = (playerTurn + 2)
        square1 = (square1 + 1)
        Oa = (Oa + 1)
        Oa1 = (Oa1 + 1)
        Oa2 = (Oa2 + 1)
        
        
        #O position left 2 
    elif playerTurn == (1) and playerMove.x < 100 and playerMove.y > 100 and playerMove.y < 200 and square2 == (0):
        gameboard.create_oval(5, 105, 95, 195, outline="Blue")
        playerTurn = (playerTurn + 2)
        square2 = (square2 + 1)
        Oa = (Oa + 1)
        Ob1 = (Ob1 + 1)
        
        
        #O position left 3 
    elif playerTurn  == (1) and playerMove.x < 100 and playerMove.y > 200 and playerMove.y < 300 and square3 == (0):
        gameboard.create_oval(5, 205, 95, 295, outline="Blue")
        playerTurn = (playerTurn + 2)
        square3 = (square3 + 1)
        Oa = (Oa + 1)
        Oc1 = (Oc1 + 1)
        Ob2 = (Ob2 + 1)
        
        
        #O position middle 1 
    elif playerTurn == (1) and playerMove.x > 100 and playerMove.x < 200 and playerMove.y < 100 and square4 == (0):
        gameboard.create_oval(105, 5, 195, 95, outline="Blue")
        playerTurn = (playerTurn + 2)
        square4 = (square4 + 1)
        Ob = (Ob + 1)
        Oa1 = (Oa1 + 1)
        
        
        #O position middle 2         
    elif playerTurn == (1) and playerMove.x > 100 and playerMove.x < 200 and playerMove.y > 100 and playerMove.y < 200 and square5 == (0):
        gameboard.create_oval(105, 105, 195, 195, outline="Blue")
        playerTurn = (playerTurn + 2)
        square5 = (square5 + 1)
        Ob = (Ob + 1)
        Ob1 = (Ob1 + 1)
        Oa2 = (Oa2 + 1)
        Ob2 = (Ob2 + 1)
        

        
        #O position middle 3
    elif playerTurn == (1) and playerMove.x > 100 and playerMove.x < 200 and playerMove.y > 200 and playerMove.y < 300 and square6 == (0) :
        gameboard.create_oval(105, 205, 195, 295, outline="Blue")
        playerTurn = (playerTurn + 2)
        square6 = (square6 + 1)
        Ob = (Ob + 1)
        Oc1 = (Oc1 + 1)
        

        
        #O position right 1  
    elif playerTurn == (1) and playerMove.x > 200 and playerMove.x < 300 and playerMove.y < 100 and playerMove.y > 0 and square7 == (0):
        gameboard.create_oval(205, 5, 295, 95, outline="Blue")
        playerTurn = (playerTurn + 2)
        square7 = (square7 + 1)
        Oc = (Oc + 1)
        Oa1 = (Oa1 + 1)
        Ob2 = (Ob2 + 1)
        

         #O position right 2 
    elif playerTurn == (1) and playerMove.x > 200 and playerMove.x < 300 and playerMove.y < 200 and playerMove.y > 100 and square8 == (0):
         gameboard.create_oval(205, 105, 295, 195, outline="Blue")
         playerTurn = (playerTurn + 2)
         square8 = (square8 + 1)
         Oc = (Oc + 1)
         Ob1 = (Ob1 + 1) 
        
         
         #O position right 3 
    elif playerTurn == (1) and playerMove.x > 200 and playerMove.x < 300 and playerMove.y < 300 and playerMove.y > 200 and square9 == (0):
         gameboard.create_oval(205, 205, 295, 295,outline="Blue")
         playerTurn = (playerTurn + 2)
         square9 = (square9 + 1)
         Oc = (Oc + 1)
         Oc1 = (Oc1 + 1)
         Oa2 = (Oa2 + 1)
         
    
    # Xmoves
    #X position left 1
    elif  playerTurn == (2) and playerMove.x < 100 and playerMove.y < 100 and square1 == (0):
        gameboard.create_line(100, 0, 0, 100, fill="Red")
        gameboard.create_line(0, 0, 100, 100, fill="Red")
        playerTurn = (playerTurn - 1)
        square1 = (square1 + 1)
        Xa = (Xa + 1)
        Xa1 = (Xa1 + 1)
        Xa2 = (Xa2 + 1)

        
        #X position left 2
    elif playerTurn == (2) and playerMove.x < 100 and playerMove.y > 100 and playerMove.y < 200 and square2 == (0):
         playerTurn = (playerTurn - 1)
         gameboard.create_line(100, 100, 0, 200, fill="Red")
         gameboard.create_line(0, 100, 100, 200, fill="Red")
         square2 = (square2 + 1)
         Xa = (Xa + 1)
         Xb1 = (Xb1 + 1)
 
         
         #X position left 3
    elif playerTurn == (2) and playerMove.x < 100 and playerMove.y > 200 and playerMove.y < 300 and square3 == (0):
         playerTurn = (playerTurn - 1)
         gameboard.create_line(100, 200, 0, 300, fill="Red")
         gameboard.create_line(0, 200, 100, 300, fill="Red")
         square3 = (square3 + 1)
         Xa = (Xa + 1)
         Xc1 = (Xc1 + 1)
         Xb2 = (Xb2 + 1)
       
        
        #X position middle 1
    elif playerTurn == 2 and playerMove.x > 100 and playerMove.x < 200 and playerMove.y < 100 and square4 == (0):
         playerTurn = (playerTurn - 1)
         gameboard.create_line(100, 0, 200, 100, fill="Red")
         gameboard.create_line(100, 100, 200, 0, fill="Red")
         square4  = (square4 + 1)
         Xb = (Xb + 1)
         Xa1 = (Xa1 + 1)
        
        #X position middle 2
    elif playerTurn == 2 and playerMove.x > 100 and playerMove.x < 200 and playerMove.y > 100 and playerMove.y < 200 and square5 == (0):
        gameboard.create_line(100, 100, 200, 200, fill="Red")
        gameboard.create_line(100, 200, 200, 100, fill="Red")
        playerTurn = (playerTurn - 1)
        square5  = (square5 + 1)
        Xb = (Xb + 1)
        Xb1 = (Xb1 + 1)
        Xa2 = (Xa2 + 1)
        Xb2 = (Xb2 + 1)
       
        
        #X position middle 3
    elif playerTurn == 2 and playerMove.x > 100 and playerMove.x < 200 and playerMove.y > 200 and playerMove.y < 300 and square6 == (0):
         gameboard.create_line(100, 200, 200, 300, fill="Red")
         gameboard.create_line(100, 300, 200, 200, fill="Red")
         playerTurn = (playerTurn - 1)
         square6  = (square6 + 1)
         Xb = (Xb + 1)
         Xc1 = (Xc1 + 1)
      

         
        #X position right 1        
    elif playerTurn == 2 and playerMove.x > 200 and playerMove.x < 300 and playerMove.y < 100 and playerMove.y > 0 and square7 == (0):
         gameboard.create_line(200, 0, 300, 100, fill="Red")
         gameboard.create_line(200, 100, 300, 0, fill="Red")
         playerTurn = (playerTurn - 1)
         square7 = (square7 + 1)
         Xc = (Xc + 1)
         Xa1 = (Xa1 + 1)
         Xb2 = (Xb2 + 1)
        

        #X position right 2
    elif playerTurn == 2 and playerMove.x > 200 and playerMove.x < 300 and playerMove.y < 200 and playerMove.y > 100 and square8 == (0):
         gameboard.create_line(200, 100, 300, 200, fill="Red")
         gameboard.create_line(200, 200, 300, 100, fill="Red")
         playerTurn = (playerTurn - 1)
         square8  = (square8 + 1)
         Xc = (Xc + 1)
         Xb1 = (Xb1 + 1)
         
         
         
        #X position right 3  
    elif playerTurn == 2 and playerMove.x > 200 and playerMove.x < 300 and playerMove.y < 300 and playerMove.y > 200 and square9 == (0):
         gameboard.create_line(200, 200, 300, 300, fill="Red")
         gameboard.create_line(200, 300, 300, 200, fill="Red")
         playerTurn = (playerTurn - 1)
         square9 = (square9 + 1)
         Xc = (Xc + 1)
         Xc1 = (Xc1 + 1)
         Xa2 = (Xa2 + 1)

    #Printing the TicTacToe line if you get three in a row with X's
    if Xa == 3:
        gameboard.create_line(50, 0, 50, 300, width="2")
       
        
    if Xb == 3:
        gameboard.create_line(150, 0, 150, 300, width="2")
    
    if Xc == 3:
        gameboard.create_line(250, 0, 250, 300, width="2")
        
    if Xa1 == 3:
        gameboard.create_line(0, 50, 300, 50, width="2")
    
    if Xb1 == 3:
        gameboard.create_line(0, 150, 300, 150, width="2")
        
    if Xc1 == 3:
        gameboard.create_line(0, 250, 300, 250, width="2")
        
    if Xa2 == 3:
        gameboard.create_line(0, 0, 300, 300, width="2")

    if Xb2 == 3:
        gameboard.create_line(0, 300, 300, 0, width="2")

    #Printing the TicTacToe line if you get three in a row with O's
    if Oa == 3:
        gameboard.create_line(50, 0, 50, 300, width="2")
        
    if Ob == 3:
        gameboard.create_line(150, 0, 150, 300, width="2")
    
    if Oc == 3:
        gameboard.create_line(250, 0, 250, 300, width="2")
        
    if Oa1 == 3:
        gameboard.create_line(0, 50, 300, 50, width="2")
    
    if Ob1 == 3:
        gameboard.create_line(0, 150, 300, 150, width="2")
        
    if Oc1 == 3:
        gameboard.create_line(0, 250, 300, 250, width="2")
        
    if Oa2 == 3:
        gameboard.create_line(0, 0, 300, 300, width="2")

    if Ob2 == 3:
        gameboard.create_line(0, 300, 300, 0, width="2")
        





    

gameboard.bind("<Button-1>", oxMoves)             
mainloop()
