'''
You need to write regex that will validate a password to make sure it meets the following
criteria:
At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a number
Valid passwords will only be alphanumeric characters.
'''


import re


def regex_password():
    print("задача 2_85:")
    passw = "123Qwer"
    regex = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])[A-Za-z0-9]{6,}$'
    result = re.match(regex, passw)
    if result:
        print("Пароль прошел проверку")
    else:
        print("Пароль  не прошел проверку")
