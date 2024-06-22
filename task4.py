import random

def game_winner(computer, me):
    if computer == me:
        return None
    elif computer == 'R':
        if me == 'P':
            return True
        elif me  == 'S':
            return False
        
    elif computer == 'P':
        if me == 'S':
            return True
        elif me == 'R':
            return False
        
    elif computer == 'S':
        if me == 'R':
            return True
        elif me == 'P':
            return False

while True:
    print("Computer Turn: Rock(R) Paper(P) or Scissors(S):-")
    random_num = random.randint(1, 3)
    if(random_num==1):
        computer='R'
    elif(random_num==2):
        computer='P'
    else:
        computer='S'
    
    me = input("My turn: Rock(R) Paper(P) or Scissors(S) (or 'quit' to end the game): ").upper()
    if me == 'QUIT':
        print("Thanks for playing")
        break
    
    if me not in ['R', 'P', 'S']:
        print("Invalid choice ans Please try again.")
        continue
    
    result = game_winner(computer, me)

    print(f"Computer chose {computer}")
    print(f"My chose {me}")

    if result is None:
        print("The game is a tie.")
    elif result:
        print("You win.")
    else:
        print("You lose.")

    print("\nStarting a new game.\n")
