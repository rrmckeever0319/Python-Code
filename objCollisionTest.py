from Tkinter import *
master = Tk()

import time


frame = Canvas(master, width=1000, height=600, bg="black")



frame.create_rectangle(50, 50, 950, 500, outline="white")
frame.create_line(500, 50, 500, 500, fill="white", dash=(2,4))

paddle1positionY1 = (325)
paddle1positionYn = (275)

paddle2positionY1 = (325)
paddle2positionYn = (275)




#game Objects
def player1paddle (x1, y1, xn, yn):
    frame.create_rectangle(x1, y1, xn, yn, fill="white", tag="paddle1")

def player2paddle (x1, y1, xn, yn):
    frame.create_rectangle(x1, y1, xn, yn, fill="white", tag="paddle2")


#creating starting position of objects

player1paddle(100, paddle1positionY1, 115, paddle1positionYn)
player2paddle(900, paddle2positionY1, 885, paddle2positionYn)

frame.focus_set()


def mouseClick(click):
	pass


paddle1and2Speed = (7) # How fast both paddle move up and down in pixels

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
	
	
def player2upKey(Up):
	global paddle1and2Speed
	global paddle2positionY1 
	global paddle2positionYn

	if paddle1positionY1 > 53 :
		paddle2positionY1 = (paddle2positionY1 - (paddle1and2Speed))
		paddle2positionYn = (paddle2positionYn - (paddle1and2Speed))

	frame.delete("paddle2")
	player2paddle(900, paddle2positionY1, 885, paddle2positionYn)
	


def player2downKey(Down):
	global paddle1and2Speed
	global paddle2positionY1 
	global paddle2positionYn

	if paddle1positionY1 < 497:
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
