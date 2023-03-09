# Mingyu Li
debug = True
password = None
# set two variables for the main function

# this is the change I make for the rubric
def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3))
        encoded_password += encoded_digit
    return encoded_password


while debug:
    # print the menu
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3.Quit')
    option = int(input('Please enter an option:'))
    if option == 1:
        password = input('Please enter your password to encode:')
        print('Your password has been encoded and stored! ')
    elif option == 2:
        print('The encoded password is', end=' ')
        # plug in the encoder function
        print(encode(password), end='')
        print(f', and the original password is {password}')
    elif option == 3:
        debug = False
