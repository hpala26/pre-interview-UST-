# Password Validator

This project contains a password validation utility that checks if provided passwords meet certain security criteria. 
The validation logic is implemented in Python and tested using **pytest**.

## Criteria for Valid Passwords

Passwords must meet the following criteria to be considered valid:
- At least one letter between `a-z`.
- At least one letter between `A-Z`.
- At least one digit between `0-9`.
- At least one character from `$#@`.
- Minimum length of 6 characters.
- Maximum length of 12 characters.

## Installation

1. **Pre-requisites**:
    1. Python3 
   2. Pytest 

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/hpala26/pre-interview-UST-.git
   cd pre-interview-UST-
   ```

## How to Run

### Run the Main Program:
You can run the password validation logic via the `main.py` file:

```bash
python main.py
```

The program reads from the `input/passwords.txt` file, validating the passwords listed within.

### Running Tests:
To run the unit tests, execute the following command to ensure everything is working as expected:

```bash
pytest tests/ -v
```

## How to Add Passwords

To add more passwords for validation:
1. Open the `input/passwords.txt` file.
2. Add new passwords on separate lines or provide them as comma-separated values in a single line.

## Example Passwords File

An example of what your `input/passwords.txt` file might look like:

```
as@1,a15#,2w3E*,33Au@45
Pa$$w0rd,short6A#1,12Aa@Bb34
Password#1,Valid1P@,TooLongPassword123@
N0Sp3cialChar,One1@A
abcABC123#,M1Nimum!@,validPass$9
```
