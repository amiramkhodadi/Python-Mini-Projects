import os
import random
import string
def clear_screen():
    os.system('cls')

default_setting = {
        'upper' : True,
        'lower' : True,
    'number' : True,
    'punctuation' : True,
    'space' : False ,
    'password_len' : 8
}
def get_user_pass_len(option,default):
    while True:
        user_pass_len = input(f"enter password length more than 4 : (default is {default}) ")
        if user_pass_len == "":
            return default
        if user_pass_len.isdigit() :
            if 30 >= int(user_pass_len) >= 4 :
                return int(user_pass_len)
            else :
                print("your password should between 4 and 30 characters")
        else :
            print("invalid input you should enter number ")
        print("please try again")

def get_yes_or_no_from_user(option,default):
    while True:
        user_choice = input(f'include {option} ?(default is {default} y : yes , n : no) ').lower()
        if user_choice == '':
            return default
        if user_choice in ['y','n']:
            return user_choice == 'y'
        print('Invalid Input please try again !!!')

def get_setting_from_user(setting):
    for option,default in setting.items():
        if option != 'password_len':
            setting[option] = get_yes_or_no_from_user(option,default)
        else :
            setting[option] = get_user_pass_len(option,default)



def password_generator(setting) :
    password_len = setting['password_len']
    final_password = ""
    user_choice = list(filter(lambda x : setting[x] == True ,['upper','lower','number','punctuation','space']))
    for i in range(password_len):
        random_type = random.choice(user_choice)
        if random_type == 'upper':
                final_password += random.choice(string.ascii_uppercase)
        elif random_type == 'lower':
                final_password += random.choice(string.ascii_lowercase)
        elif random_type == 'number':
                final_password += str(random.randint(0, 9))
        elif random_type == 'punctuation':
                final_password += random.choice(string.punctuation)
        elif  random_type == 'space':
                final_password += ' '
        else :
            print("invalid password please try again")

    return final_password
def password_generator_loop():
    while True:
        print('-' * 40)
        print(f'Generated Password : {password_generator(default_setting)}')

        while True :
            wanted_another_pass = input("Do you want to generate another password? (y/n) : ").lower()
            if wanted_another_pass in ['y','n','']:
                if wanted_another_pass == 'n':
                    return
                break
            else :
                print("invalid input please try again")


def run_app():
    clear_screen()
    get_setting_from_user(default_setting)
    password_generator_loop()
    print("Thank you for using this program")

run_app()
