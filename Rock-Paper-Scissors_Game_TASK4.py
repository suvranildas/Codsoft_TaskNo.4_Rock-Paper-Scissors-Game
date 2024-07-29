import random
def user():
    user = input("Enter rock, paper, or scissors: ")
    while user not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter between rock, paper, or scissors.")
        user = input("Enter rock, paper, or scissors: ")
    return user
def computer():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
def winner(user, computer):
    if user == computer:
        return "draw"
    elif ((user == 'rock' and computer == 'scissors') | (user == 'scissors' and computer == 'paper') | (user == 'paper' and computer == 'rock')):
        return "user"
    else:
        return "computer"

def choices(user, computer):
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")

def result(winner):
    if winner == "draw":
        print("It's a draw!")
    elif winner == "user":
        print("Congratulations! You win!")
    else:
        print("Computer wins!")

def play_again():
    play_again = input("Do you want to play again? (yes/no): ")
    return play_again == 'yes'

def rock_paper_scissors():

    print("Welcome to Rock-Paper-Scissors Game!")
    user_score = 0
    computer_score = 0
    while True:
        you = user()
        machine = computer()
        choices(you, machine)
        champion = winner(you, machine)
        result(champion)
        if champion == "user":
            user_score +=1
        elif champion == "computer":
            computer_score += 1

        print(f"Score - You: {user_score}  Computer: {computer_score}")

        if not play_again():
            print("Thanks for playing!")
            break
rock_paper_scissors()
