import random




total = (0)
testActive = ("True")
answerEntered = ("False")

while testActive == ("True"):
    
    
    for i in range(26):
        randomVariable = (random.randrange(0,25))
        
        userAnswer = int(raw_input("What is " + str(i) + " " + "squared?" + " "))
        print randomVariable                       
        if userAnswer == (i) * (i):
            print ("CORRECT!")
            print (" " )
            total += 1
        
        elif userAnswer != (i) * (i):
            print ("Incorrect, the correct answer is " + str((i) * (i)))
            print (" " )
        

    print ("You got " + str(total) + (" correct") )

    

    while answerEntered == ("False"):
        userAnswer = raw_input(("Again? yes/no" + " "))
        if userAnswer == ("yes") :
            testActive = ("True")
            answerEntered = ("True")
            total = (0)
            
        elif userAnswer == ("no") :
            testActive = ("False")
            answerEntered = ("True")
    
        elif userAnswer != ("yes") or ("no") :
            print ("yes or no")
            print (" ")

