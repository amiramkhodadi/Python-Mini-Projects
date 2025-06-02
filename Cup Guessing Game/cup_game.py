import random

number_cups = int(input("how many cups? "))
number_chance = int(input("how many chance? "))

right_answer = random.choice(range(1, number_cups+1))
is_win = False
for i in range(number_chance):
    print(f"{number_chance} chances left")
    user_answer = int(input(f"Guess [1-{number_cups} ] : "))
    if user_answer == right_answer:
        print("Correct! Guess ")
        is_win = True
        break
    else :
        print(f"Wrong! Guess  ")

    number_chance -= 1
    print("-" * 30, )

if is_win :
    print("You win!")
else :
    print(f"You lose! The right answer is {right_answer}")