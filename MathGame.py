import random
print("Welcome to a mathematics game")
number = int(input("Please type a number between 1 and 5"))
if number == 1:
    print("Welcome to level 1")
    num1= random.randint(1,10)
    num2=random.randint(1,10)
    print("calculate",num1,"+",num2,"and enter your answer below")
    answer = int(input())
    if answer == num1+num2:
        print("You completed level 1.Hooray!")
        print("Welcome to level 2")
        num3=random.randint(25,50)
        num4=random.randint(25,50)
        print("calculate",num3,"+",num4,"and enter your answer below")
        answer = int(input())
        if answer == num3+num4:
            print("You completed the level.Yippee!")
            print("Other Levels are coming soon!")
        else:
            print("Incorrect.Try again later.")
    else:
        print("Incorrect.Try again later.")
        
if number == 2:
    print("Welcome to level 2")
    num3=random.randint(25,50)
    num4=random.randint(25,50)
    print("calculate",num3,"+",num4,"and enter your answer below")
    answer = int(input())
    if answer == num3+num4:
        print("You completed the level.Yippee!")
        print("Other Levels are coming soon!")
    else:
        print("Incorrect.Try again later.")
        
if number > 2 and number <= 5:
    print("Levels coming soon!")
if number >5:
    print("We asked you to pick a number between 1 and 5")

    
    









    
    
    



