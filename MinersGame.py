import random
hearts = 3
emeralds = 0
def miner_sam_request():
    global hearts
    global emeralds
    global total
    global loopcount
    total=5
    print("Please enter your name:")
    name = input()
    print("hearts = ",hearts)
    print("Miner Sam: 'Help! there is an monumental earthquake happening above!'")
    print("Miner Tom: 'But what about our abundance of emeralds we miners collected'")
    print("Captain: 'We sure cannot leave them behind but our safety is much more important than that'")
    print("Police: 'Radio...is...not working properly...everyone must be in safety...")
    print("General: 'Miner Sam how many emeralds have you searched?\n'")
    samemerald = random.randint(10,25)
    print("Miner Sam: 'I have searched",samemerald,"emeralds'")
    print("General: 'Miner Tom how many emeralds have you searched?'")
    tomemerald = random.randint(20,30)
    print("Miner Tom: 'I have searched",tomemerald,"emeralds\n'")
    totalemeralds =int(input("General: 'Help me to find the total emeralds miner Sam and miner Tom has collected:\n"))
    totale = samemerald + tomemerald    
    if totalemeralds == totale:
        print("Clever! I will give you two emeralds from our collection!")
        emeralds = emeralds + 2
        loopcount =1
        emerald_hunt()        
    else:
        print("According to my calculator, it says that the answer to the calculation is",totale,"and that means you were wrong")
        emerald_hunt()
        
def check():
    global total
    global loopcount
    if loopcount == total:
        print("Mission accomplished!")
    else:
        emerald_hunt()
        
def emerald_hunt():
    global total
    global hearts
    global emeralds
    global loopcount
    loopcount+=1
    numvalue = random.randint(20,40)
    numvalue = random.randint(24,47)
    print("Calculate",numvalue,"+",numvalue)
    answer = int(input())
    if answer == numvalue + numvalue:
        emeralds += 5
        print("Correct! you have got  5 emeralds and the total is",emeralds,"emeralds")
        check()
    else:
        print("Incorrect, you have lost a life")
        hearts = hearts - 1
        print("Hearts remaining:",hearts)
        if hearts == 0:
            print("You have lost all your hearts. Rest in peace, you will be remembered forever")
        else:
            check()
            
miner_sam_request()
