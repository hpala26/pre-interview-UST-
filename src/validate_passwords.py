import re

def validate_passwords(passwords):
    password_list = passwords.split(',')

    valid_passwords = []

    lower_case = re.compile(r'[a-z]')
    upper_case = re.compile(r'[A-Z]')
    digit = re.compile(r'[0-9]')
    special_char = re.compile(r'[$#@]')

    for password in password_list:
        if (6 <= len(password) <= 12 and
            lower_case.search(password) and
            upper_case.search(password) and
            digit.search(password) and
            special_char.search(password)):
            valid_passwords.append(password)

    return ','.join(valid_passwords) if valid_passwords else "No valid passwords found."
