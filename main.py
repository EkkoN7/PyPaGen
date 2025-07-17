import random

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


def get_length(user_input, name_count):
    random_num = random.randint(0, user_input - 1)
    try:
        result = user_input // random_num
    except ZeroDivisionError:
        return 1
    return name_count + result


def get_random(name_count, character):
    for i in range(1, name_count + 1):
        random_chars = random.choice(character)
        password_list.append(random_chars)

print(f"{acii_art}\nTo create a safer cyber environment.")

is_insecure = True
while is_insecure:
    user_input = input("Welcome. How long would you like your new password to be? (Minimum: 16 characters)\nUser: ").strip()
    user_input_isdigit = user_input.isdigit()
    if user_input_isdigit == True:
        user_input_len = int(user_input)
        if user_input_len >= 16:

            user_input_upper = input("Include uppercase letters? (y/n)\nUser: ").strip().lower()
            user_input_upper_isalpha = user_input_upper.isalpha()
            if user_input_upper_isalpha == True:
                if user_input_upper == "y" or user_input_upper == "n":
                    user_input_numbers = input("Include numbers? (y/n)\nUser: ").strip().lower()
                    user_input_numbers_isalpha = user_input_numbers.isalpha()
                    if  user_input_numbers_isalpha == True:
                        if user_input_numbers == "y" or user_input_numbers == "n":
                            user_input_symbols = input("Include special characters? (y/n)\nUser: ").strip().lower()
                            user_input_symbols_isalpha = user_input_symbols.isalpha()
                            if user_input_symbols_isalpha == True:
                                if user_input_symbols == "y" or user_input_symbols == "n":

                                    upper_count = 0
                                    num_count = 0
                                    sym_count = 0

                                    password_list = []

                                    if user_input_upper == "y":
                                        get_upper = get_length(user_input_len, upper_count)
                                        upper_count += get_upper
                                        if upper_count == 0:
                                            get_random(1, upper_letters)
                                        else:
                                            get_random(upper_count, upper_letters)
                                    if user_input_numbers == "y" and len(password_list) != user_input_len:
                                        num_length = user_input_len - len(password_list)
                                        get_num = get_length(num_length, num_count)
                                        num_count += get_num
                                        if num_count == 0:
                                            get_random(1, numbers)
                                        else:
                                            get_random(num_count, numbers)
                                    if user_input_symbols == "y" and len(password_list) != user_input_len:
                                        sym_length = user_input_len - len(password_list)
                                        get_sym = get_length(sym_length, sym_count)
                                        sym_count += get_sym
                                        if sym_count == 0:
                                            get_random(1, symbols)
                                        else:
                                            get_random(sym_count, symbols)
                                    if len(password_list) != user_input_len:
                                        low_length = user_input_len - len(password_list)
                                        get_random(low_length, lower_letters)

                                    random.shuffle(password_list)
                                    password = "".join(password_list)
                                    print(password)
                                    is_insecure = False
                                else:
                                    print("Your input appears to be incorrect.")
                                    continue
                            else:
                                print("Your input appears to be incorrect.")
                                continue
                        else:
                            print("Your input appears to be incorrect.")
                            continue
                    else:
                        print("Your input appears to be incorrect.")
                        continue
                else:
                    print("Your input appears to be incorrect.")
                    continue
            else:
                print("Your input appears to be incorrect.")
                continue
        else:
            print("Your password is below the recommended length of 16 characters.")
            continue
    else:
        print("Your input appears to be incorrect.")
        continue