import random
number = random.randint(1000,9999)
print("type the code",number," to play this game")
rep = int(input())

if rep == number:
    print("What is your name?")
    rep2 =input()
    print("What is your surname?")
    rep3 = input()
    print()
    print("*****************************")
    print("*                                      *")
    print("* ",rep2+"  "+rep3,"!  *")
    print("* Wish you a Happy          *")
    print("*                        Birthday!!*")
    print("*                                      *")
    print("*****************************")
    print()
    
    print("Now answer the question and let's see if we can calculate your age")
    print("What year are you born in?")
    rep4 = int(input())
    yearnow = 2021
    age=2021 - rep4
    print("\nWOW! you are",age,"years old\n")
    if age>20 and age<=30:
        print("Early Adulthood (Ages 20-35): – You are a young adult to accomplish your many responsibilities, including finding a home and mate, establishing a family or circle of friends, and/or getting a good job.")
    elif age>30 and age<=40:
        print(" You Should Make these After 30:  Create a Budget., Exercise Regularly., Get Serious About Paying Off Debt., Consider Buying Instead of Renting., Do More Cooking at Home.,Stop Your Bad Habits., Get to Know Yourself Again.")
    elif age>40 and age<=50:
        print("The phrase 'Life begins at 40' means that:\n When one reaches the age of forty, Life becomes better, maybe because one has the skills, experiences and means necessary for an enjoyable life.\n10 fab things about being 40''s:\nUnderstanding yourself better.\nHaving the confidence to dress for YOU.\nDeveloping a great relationships with your kids & partner.\nEnjoying time on your own.\nDoing more of what makes you happy.\nLearning to say NO.\nKnowing your tribe.\nCaring less about what others think of you.")
    else:
        print("You're less fearful.\nYou're not afraid to have opinions.\nYou know yourself.\nYou have a greater appreciation of life.\nIt's easier to laugh at yourself.\nIt's easier to laugh at others.\nIt's easier to take life less seriously.\nYou stop caring what other people think.\nYou stop sweating the small stuff.\nYou have a lifetime of wisdom to help you make decisions.\nYou are more at peace. ")
    
    print()
    print("Here's a riddle for you: what has a head and a tail but no legs?")
    ans = input()
    if ans == "a coin" or ans=="coin":
        print("Well done! I thought it was very hard for you... but anyways here is another riddle for you: what has a face and two hands but no arms or legs")
        ans2 = input()
        if ans2 == "a clock" or ans2== "clock":
            print("Bravo! you are AMAZING! do you want to play a birthday game(type yes or no)")
            yesno = input()
            if yesno == "yes":
                print("You have to guess a number between 1 and 10")
                num = random.randint(1,10)
                guess = int(input())
                if guess == num:
                    print("WOW! you are rocking in your birthday! and that's the end :( but you can play again in your next birthday!")
                    print("*****************************")
                    print()
                    print("* ",rep2+"  "+rep3,"!********")
                    print("* Wish you a Happy ********")
                    print("*                            Birthday!!")
                    print()
                    print("*****************************")
                    print("            THE END              " )
                    quit()
                else:
                    print("Unlucky, but you can play the game again")
                   
                    quit()
            elif yesno == "no":
                print("Okay! Enjoy the rest of your birthday",rep2,"!")
            else:
                print("You have to type yes or no")
        else:
            print("Oops! the answer is 'a clock' or 'clock'!")
    else:
        print("Oops! the answer is 'a coin' or 'coin'")
else:
    print("INCORRECT CODE")
          
    
    
    
          

    
      
      
      
