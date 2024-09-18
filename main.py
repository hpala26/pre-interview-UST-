from src.validate_passwords import validate_passwords

def main():
    input_passwords = "as@1,a15#,2w3E*,33Au@45"
    result = validate_passwords(input_passwords)
    print("Valid passwords:", result)

if __name__ == "__main__":
    main()
