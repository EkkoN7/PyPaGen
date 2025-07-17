import random
import os

acii_art = r'''
  ____        ____        ____            
 |  _ \ _   _|  _ \ __ _ / ___| ___ _ __  
 | |_) | | | | |_) / _` | |  _ / _ \ '_ \ 
 |  __/| |_| |  __/ (_| | |_| |  __/ | | |
 |_|    \__, |_|   \__,_|\____|\___|_| |_|
        |___/                             
'''

lower_letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

upper_letters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

numbers = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
    "[", "]", "{", "}", "|", "\\", ";", ":", "'", "\"", ",", ".", "<",
    ">", "/", "?"
]

character_pool = [lower_letters, upper_letters, numbers, symbols]


print(f"{acii_art}\nTo create a safer cyber environment.")

# Input
user_input_len = input("Welcome. How long would you like your new password to be? (Minimum: 16 characters)\nUser: ").strip()
user_input_upper = input("Include uppercase letters? (y/n)\nUser: ").lower().strip()
user_input_numbers = input("Include numbers? (y/n)\nUser: ").lower().strip()
user_input_symbols = input("Include special characters? (y/n)\nUser: ").lower().strip()

result = user_input_len //random.choice(character_pool)


# Input validation
user_input_len_isdigit = user_input_len.isdigit()
user_input_upper_isalpha = user_input_upper.isalpha()
user_input_numbers_isalpha = user_input_numbers.isalpha()
user_input_symbols_isalpha = user_input_symbols.isalpha()

# Calculation
lower_count = 0
upper_count = 0
num_count = 0
sym_count = 0

def get_length(user_input, name_count):
    random_num = random.randint(0, user_input - 1)
    try:
        result = user_input // random_num
    except ZeroDivisionError:
        result = 0
    return name_count += result


if user_input_len_isdigit == True and \
        user_input_upper_isalpha == True and \
        user_input_numbers_isalpha == True and \
        user_input_symbols_isalpha == True:
    password_list = []
    get_low = get_length(user_input_len, lower_count)
    for num in range(1, get_low + 1):
        low_letters = random.choice(lower_letters)
        password_list.append(low_letters)
    if upper_letters == "y":
        

    for characters in range(1, int(user_input_len) + 1):

    password = "".join(password_list)
    print (password)

