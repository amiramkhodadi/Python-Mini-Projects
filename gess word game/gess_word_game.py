import random

words = ['hello' , ' tree' , 'amir' , 'university' , 'son' , 'movie' , 'developer' , 'god' , 'real madrid' , 'blue' ]
# right_answer = random.choice(words)
right_answer = words[2]

def get_input() :
    user_input = input("Enter a word from list of up: ")
    if user_input.isalpha():
        return user_input.lower()
    else :
        print("-------------Please enter a valid word.---------------")
        print()
        get_input()

def play_game(words):
        i = 0
        while i<5:
            user_input = get_input()
            if user_input in words:
                if user_input == right_answer:
                    print('-' * 40)
                    return f"you are win ;  {right_answer} is answer"
                    print('-' * 40)
                else :
                    print( "your  answer is  wrong please try again"  )
                    print(f"you have {4- i} chanse")
                    print('-' * 40)
                    i += 1
            else :
                print( "your  answer is  not in list  please try again" )
        return f"you are lose ; the righ answer is {right_answer}"

def print_game_intro(words):
    print('-'*40)
    print("hi , welcome to guess game")
    print("you have 5 guesses from list of words to win the game")
    print("list of words : " , words)
    game_start = input(" * Are You Ready ? (yes , no) ==>  " ).lower()
    print('-' * 40)
    if game_start == 'yes':
         print(play_game(words))
    elif game_start == 'no':
       print("byyyyyyyyyyyyyyyyyyyyyyyy")
    else :
        print_game_intro()

print_game_intro(words)



















