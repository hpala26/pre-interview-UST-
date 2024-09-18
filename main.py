from src.validate_passwords import validate_passwords

def main():
    input_file_path = 'src/input/passwords.txt'

    with open(input_file_path, 'r') as file:
        password_lines = file.readlines()

    for idx, passwords in enumerate(password_lines):
        passwords = passwords.strip()
        if passwords:
            result = validate_passwords(passwords)
            print(f"Valid passwords from line {idx + 1}: {result}")


if __name__ == "__main__":
    main()
