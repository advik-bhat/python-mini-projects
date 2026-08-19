import random

opt = ["rock", "paper", "scissors"]

print("\tRock Paper Scissors Game")
print("Rules: Whoever reaches 5 points first, wins!")

user = 0
computer = 0

while user < 5 and computer < 5:

    choice = input("Enter a choice: ").lower()

    if choice not in opt:
        print("Try Again")
        continue

    computer_choice = random.choice(opt)

    print(f"Computer chose: {computer_choice}")

    if choice == computer_choice:
        print("Tie!")

    elif (
        (choice == "rock" and computer_choice == "scissors") or
        (choice == "paper" and computer_choice == "rock") or
        (choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
        user += 1

    else:
        print("You lose!")
        computer += 1

    print(f"Score → You: {user} | Computer: {computer}")
    print()

if user == 5:
    print("Yay! You won :)")
else:
    print("You lost the match :(")