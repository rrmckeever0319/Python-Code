import random



amountInList = (26)
total = (0)
testActive = ("True")
answerEntered = ("False")
randomVariable = (0)

squares = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]



while testActive == ("True"):
    
    
    for i in range(26):
        randomVariable = (random.randrange(0,(amountInList)))

        squares[randomVariable]
        
        userAnswer = int(raw_input("What is " + str(squares[randomVariable]) + " " + "squared?" + " "))
                            
        if userAnswer == (squares[randomVariable]) * (squares[randomVariable]):
            print ("CORRECT!")
            print (" " )
            total += 1
            amountInList -= 1
            
            squares.pop(randomVariable)
          
            
        elif userAnswer != (squares[randomVariable]) * (squares[randomVariable]):
            print ("Incorrect, the correct answer is " + str((squares[randomVariable]) * (squares[randomVariable])))
            print (" " )
            amountInList -= 1
            squares.pop(randomVariable)

    print ("You got " + str(total) + (" correct") )

    
    # reseting the variables
    while answerEntered == ("False"):
        userAnswer = raw_input(("Again? yes/no" + " "))
        if userAnswer == ("yes") :
            testActive = ("True")
            answerEntered = ("True")
            total = (0)
            squares = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
            amountInList = (26)
            
        elif userAnswer == ("no") :
            testActive = ("False")
            answerEntered = ("True")
    
        elif userAnswer != ("yes") or ("no") :
            print ("yes or no")
            print (" ")
