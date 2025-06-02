import random
choices =["r" , "p" , "s" ]

choice_meaning = {
    "r" : "rock",
    "p" : "paper",
    "s" : "scissor"
}
user_score = 0
ai_score = 0
while True:
    if user_score == 5 or ai_score == 5:
        break
    user_choice = input("select from  rock , paper , scissor  (r , p , s ) : ")
    ai_choice = random.choice(choices)
    if user_choice in choices:
        print(f'you chose {choice_meaning[user_choice]} , ai chose {choice_meaning[ai_choice]}')
        if user_choice == ai_choice :
            print("tie")
            # continue
        elif user_choice == "r" and ai_choice == "s":
            user_score += 1
            print("you + 1 ")
        elif user_choice == "p" and ai_choice == "r":
            user_score += 1
            print("you + 1 ")
        elif user_choice == "s" and ai_choice == "p":
            user_score += 1
            print("you + 1 ")
        else :
            ai_score += 1
    else :
        print("invalid input ")

    print(f"your score is {user_score} / ai score is {ai_score}")
    print("\n" , 15*"--" , "\n")

if user_score == 5:
    print("you win")
else:
    print("you lose")
