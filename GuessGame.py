import random
hearts = 5
coins = 0
autoclick = False
def guess():
    global hearts
    global coins
    print("Press A for shop or B for instructions or number 1 to get to the actual game")
    ans = int(input())
    if ans = "A".upper:
        shop = ["autoclick","1 heart"]
        print("You can buy an autoclick for $20 or 1 heart for $10")
        print("Press C to buy an autoclick or D for 1 heart")
        rep = int(input())
        if rep = "C".upper:
            print("Do you want to buy an autoclick for $20(type yes or no)")
            yesno = int(input())
            if yesno = "yes":
                if coins >= 20:
                    coins = coins - 20
                    autoclick = True
                if coins < 20:
                    print("You don't have $20, you can get them by playing games")
            if yesno = "no":
                print("Play again!")
            else:
                print("You have to type yes or no")
        if rep = "D".upper:
            print("Do you want to buy 1 heart for $10(type yes or no)")
            yesno2 = int(input())
            if yesno2 = "yes":
                if coins >= 10:
                    coins = coins - 10
                    if hearts = 5:
                        print("You already have 5 hearts and thats the limit")
                        coins = coins + 10
                    else:
                        hearts = hearts + 1
                if coins < 10:
                    print("You don't have $10, you can get them by playing games")
            if yesno2 = "no":
                print("Play again!")
            else:
                print("You have to type yes or no")
        else:
            print("You have to type C or D")
    if ans = "B".upper:
        print("These are the instructions for the guessing game")
        print()
        print("You have to guess a number between the two numbers given and if you get the number right, you get a reward of coins")
        print("Good luck!")
    else:
        print("You have to type A or B or 1")
def game():
    pass

    
                
                
                    

                    
        
