import random

# set our variables
player_score = 0
pc_score = 0
count = 3
# create a function - moves() 
def moves():
    global player_score
    global pc_score
    moves = ["rock", "paper", "scissors", "exit"]
    pc_selection_move = ["rock", "paper", "scissors"]           
    while (player_score <count) and (pc_score < count):            
        player_move = input("Choose rock, paper, scissors or exit\n")
        pc_move = random.choice(pc_selection_move)
        if player_move not in moves:
            print("Type rock, paper, scissors or exit\n")
            reset()
        elif player_move == moves[3]:
            print("\n\n\n")
            exit()
        else:
            print("You chose:",player_move.upper(),"and the computer chose:",pc_move.upper())
            if player_move == pc_move:
                print("Tie match!")
            else:
                if  pc_move == moves[0]:
                    if player_move == moves[1]: 
                        print("Paper covers rock so YOU WIN!")
                        player_score = player_score + 1
                        print()
                        print("Your score is:",player_score,"\nThe computer score is:",pc_score)
                    elif player_move == moves[2]:
                        print("Rock smashes the scissors so COMPUTER WINS!")
                        pc_score=pc_score+1
                        print()
                        print("Your score is:",player_score,"\nThe computer score:",pc_score)
                elif pc_move == moves[1]:
                    if player_move == moves[2]:
                        print("Scissor cuts the paper so YOU WIN!")
                        player_score = player_score + 1
                        print()
                        print("Your score is:",player_score,"/nThe computer score:",pc_score)
                    elif player_move == moves[0]:
                        print("Paper covers rock  so COMPUTER WINS!")
                        pc_score=pc_score+1
                        print()
                        print("Your score is:",player_score,"\nThe computer score:",pc_score)
                else:
                    if player_move == moves[0]:
                        print("Rock smashes the scissors so YOU WIN!")
                        player_score = player_score + 1
                        print()
                        print("Your score is:",player_score,"\nThe computer score:",pc_score)
                    elif player_move == moves[1]:
                        print("Scissor cuts the paper so COMPUTER WINS!")
                        pc_score=pc_score+1
                        print()
                        print("Your score is:",player_score,"\nThe computer score:",pc_score)
      
    if player_score >pc_score:
        print("You are the champion!")
    elif pc_score == player_score:
        print("A Tie match")
    else:
        print("The computer is the champion")       
                    
# create another function - reset() 
def reset():
    moves()
moves()


          
        
    

    
