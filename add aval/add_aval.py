while True :
    is_prime = True
    user_number = input("Enter a number: ")
    if user_number == "quit":
        break
    for i in range(2, int(user_number)) :
        if int(user_number) % i == 0 :
            is_prime = False
            print(f"{user_number}is a multiple of {i} so it's not Prime" )
            break
    if is_prime :
        print(f"{user_number} is  a  Prime")
    else :
        print(f"{user_number} is not a  Prime" )

