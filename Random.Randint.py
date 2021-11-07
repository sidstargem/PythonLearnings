import random


def addition(num1,num2):
    return num1+num2
def Subraction(num1,num2):
    return num1-num2

def level1():
    print("You are in LEVEL 1")
    number1=random.randint(1,10)
    number2=random.randint(1,10)
    print("Calculate",number1,"+",number2,"and enter your answer below")
    answer = int(input())
    if answer == addition(number1 , number2):
        print("Hooray!You completed LEVEL 1!")
        print("*********************************************")
        level2()
    else:
        print("Your answer is incorrect, the correct answer is(",addition(number1 , number2),") but you can always try again")

def level2():
    print("You are in LEVEL 2")
    number1=random.randint(25,50)
    number2=random.randint(30,60)
    print("Calculate",number1,"+",number2,"and enter your answer below")
    answer = int(input())
    if answer == addition(number1 , number2):
        print("Hooray!You completed level 2!")
        print("**********************************************")
        level3()
    else:
        print("Your answer is incorrect, the correct answer is(",addition(number1 , number2),") but you can always try again")

def level3():
    print("You are in LEVEL 3")
    number1=random.randint(100,150)
    number2=random.randint(-30,60)
    print("Calculate",number1,"-",number2,"and enter your answer below")
    answer = int(input())
    if answer == Subraction(number1,number2):
        print("Hooray!You completed level 3!")
        print("***************************************************")
        level4()
    else:
        print("Your answer is incorrect, the correct answer is(",number1 - number2,") but you can always try again")

def level4():
    print("You are in LEVEL 4")
    number1=random.randint(100,150)
    number2=random.randint(-30,60)
    number3=random.randint(8,10)
    print("Calculate",number1,"-",number2,"*",number3," and enter your answer below")
    answer = int(input())
    if answer == number1 - number2 * number3:
        print("Hooray!You completed level 4!")
        print("****************************")
    else:
        print("Your answer is incorrect, the correct answer is(",number1 - number2 * number3,") but you can always try again")


print("\033[1m"+" Welcome to my mathematics game"+"\033[0m")
level1()
print("***************************************************")
print("Thank you for playing my mathematics game, more levels are coming soon!")
print("It is created by Siddharth Sureshkannan")



    
