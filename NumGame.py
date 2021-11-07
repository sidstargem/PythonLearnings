import random

def Addlevel1():
    global hearts
    global coins
    coins=0
    hearts=0
    number1 = random.randint(1,10)
    number2 = random.randint(1,5)
    print("Calculate",number1,"+",number2,"enter your answer")
    answer = int(input())
    if answer == number1 + number2:
        coins = coins + 20
        hearts = hearts + 1
        print("Hooray! You completed Addition level 1 with",coins," points")
        Addlevel2()    
        
    else:
        print("Your answer is incorrect, but you can always play again!")
        
def Addlevel2():
    global hearts
    global coins
    number3 = random.randint(10,50)
    number4 = random.randint(5,10)
    print("Calculate",number3,"+",number4,"enter your answer")
    answer = int(input())
    if answer == number3 + number4:
        coins = coins + 40
        hearts = hearts + 1
        print("Hooray! You completed Addition level 2 with",coins," points")
        Addlevel3()
            
    else:
        print("Your answer is incorrect, but you can always play again!")
        Addlevel1()
        
def Addlevel3():
    global hearts
    global coins
    number5 = random.randint(50,100)
    number6 = random.randint(10,50)
    print("Calculate",number5,"+",number6,"enter your answer")
    answer = int(input())
    if answer == number5 + number6:
        coins = coins + 60
        hearts = hearts + 1
        print("Hooray! You completed Addition level 3 with",coins," points")
        Challenge1()            
    else:
        print("Your answer is incorrect, but you can always play again!")
        Addlevel2()
        
def Challenge1():
    global hearts
    global coins
    number7 = random.randint(100,200)
    number8 = random.randint(150,200)
    number9 = random.randint(200,250)
    print("Calculate",number7,"+",number8,"+",number9,"enter your answer")
    answer = int(input())
    if answer == number7 + number8 + number9:
        coins = coins + 50
        hearts = hearts + 2
        print("Hooray! You completed Challenge level 1! Why not you play again in a new topic? with",coins," points")
    else:
        print("Your answer is incorrect, You will have to start from Addition level 1 again")
        Addlevel1()
        
def Sublevel1():
    global hearts
    global coins
    number10 = random.randint(1,10)
    number11 = random.randint(1,5)
    print("Calculate",number10,"-",number11,"enter your answer")
    answer = int(input())
    if answer == number10 - number11:
        coins = coins + 20
        hearts = hearts + 1
        print("Hooray! You completed Subtraction level 1")
    else:
        print("Your answer is incorrect, but you can always play again!")

choice = int(input("Choose 1 for Addition, 2 for Subtraction, 3 for Multiplication or 4 for Division"))
if choice == 1:      
    Addlevel1()
elif choice == 2:
    Sublevel1()
elif choice == 3:
    Addlevel1()
elif choice == 4:
    Addlevel1()
else:
    print("You didn't choose the given options, play again!")
      

    


    
        
    
    
    
    
    
