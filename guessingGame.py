def guessingGame():
    userNumber = "Unknown"
    midpoint = 50
    temp_mid = 50
    tries = 0
    while (userNumber != midpoint):
        HLE = input(f"Higher, lower, or equal to {midpoint} [H/L/E] ")
        if HLE == "H": 
            temp_mid = round(temp_mid / 2)
            midpoint = midpoint + temp_mid
            tries = tries + 1
            if midpoint == 99 and temp_mid == 0: 
                midpoint = 100
        elif HLE == "L": 
            temp_mid = round(temp_mid / 2)
            midpoint = midpoint - temp_mid 
            tries = tries + 1
            if midpoint == 1 and temp_mid == 0: 
                midpoint = 0
        elif HLE == "E":
            tries = tries + 1 
            print(f"It took {tries} tries and your number is: {midpoint}")
            userNumber = midpoint
        



def Main():
    guessingGame()
Main()
