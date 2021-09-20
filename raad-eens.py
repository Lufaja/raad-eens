import random
winAmount = 0
lossAmount= 0
roundNum = 1
continueG = "y"
while continueG == "y" and roundNum <= 20:
    secret = random.randint(1, 1000)
    answer = 0
    tryNum = 1
    print("Round " + str(roundNum))
    
    while int(answer) != secret and tryNum <= 10:
        print("Try " + str(tryNum))
        answer = (input("{ "))
        digit = answer.isdigit()
        if digit == False:
            print("Only use numbers!")
            answer = 0
            tryNum -= 1
        elif digit == True and int(answer) > 1000:
            print("Answer from 1 to 1000")
            digit = False
            answer = 0
            tryNum -= 1
        answer = int(answer)
        difference = secret - answer
        if digit == False:
            pass
        elif answer == secret:
            print("You guessed the right number!!")
            winAmount += 1
        elif tryNum == 10:
            print("You couldn't guess the right number.")
            lossAmount += 1
        elif difference <= 20 and difference >= -20:
            print("Very hot!") 
            if answer < secret:
                print("Higher")
            elif answer > secret:
                print("Lower")
        elif difference <= 50 and difference >= -50:
            print("Getting warmer!")
            if answer < secret:
                print("Higher")
            elif answer > secret:
                print("Lower")
        elif answer < secret:
            print("Higher")
        elif answer > secret:
            print("Lower")
        tryNum += 1
    if roundNum == 20:
        break
    print("You have " + str(winAmount) + " point(s).")
    continueG = " "
    while continueG != "y" and continueG != "n":
        continueG = input("Want to go another round? Y/N: ").lower()
    if continueG == "n":
        break
    else:
        roundNum += 1

print("-----------------------------------------------")
print("You played " + str(roundNum) + " round(s), won " + str(winAmount) + " time(s) and lost " + str(lossAmount) + " time(s).")
input("Press enter to exit the game.")