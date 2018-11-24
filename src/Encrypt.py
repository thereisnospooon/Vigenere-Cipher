import sys
import os

# ********************** Constants *******************
UPPER_CYCLE = 65
LOWER_CYCLE = 97


def verify_args():
    """
    Verifies that the args are path to a program and a valid key
    :return: Void. Does nothing if the args are valid. If not, prints a usage message and exits.
    """
    # Todo: verify key is only letters
    if len(sys.argv) != 3:
        print("Usage: python3 encrypt.py <input file> <key>")
        exit(1)
    elif not os.path.exists(sys.argv[1]):
        print("path is not valid")
        exit(1)
    elif not isinstance(sys.argv[1], str) or not isinstance(sys.argv[2], str):
        print("path and key should be strings")
        exit(1)


def encrypt_letter(char: str, encrypt_var: str):
    """
    Given a letter from the text input and a char from the key, this function returns the letter after
    encryption
    :param char: Char from input text file
    :param encrypt_var: corresponding char from key
    :return: A char after encryption
    """
    if char is " ":
        return char
    if char.isalpha():
        if encrypt_var.isupper():
            val = (ord(char) + (ord(encrypt_var) - UPPER_CYCLE))
            if char.isupper() and val > ord("Z"):
                return chr(val - ord("Z"))
            elif char.islower() and val > ord("z"):
                return chr(val - ord("z"))
            else:
                return chr(val)
        else:
            val = (ord(char) + (ord(encrypt_var) - LOWER_CYCLE))
            if char.isupper() and val > ord("Z"):
                return chr(val - ord("Z"))
            elif char.islower() and val > ord("z"):
                return chr(val - ord("z"))
            else:
                return chr(val)
    else:
        return char


def encrypt(path: str, key: str):
    """
    Opens the file specified by path and encrypts the text in it using vigenere cipher and
    key.
    :param path: path to the text file to encrypt.
    :param key: key of the encryption
    :return: lines of encrypted text
    """
    encrypted_lines = []
    counter = 0
    with open(path, "r") as input_file:
        for line in input_file.readlines():
            cur_line = ""
            for char in line:
                cur_line += encrypt_letter(char, key[counter % len(key)])
                counter += 1
            encrypted_lines.append(cur_line)
    return encrypted_lines


def write_encrypted(encrypted_lines: list, output_path: str):
    """
    Given a list of encrypted lines, this function writes them to Outputs directory
    :param encrypted_lines:
    :return:
    """
    with open(output_path, "w") as target:
        for line in encrypted_lines:
            target.write(line)


def get_output_path(path: str):
    """
    Given a path, this function extracts the name of the file and appends "_encrypted"
    :param path: path to file to encrypt
    :return: a string containing the name of the output file
    """
    if not os.path.exists("../Outputs"):
        os.makedirs("../Outputs")
    return "../Outputs/" + os.path.basename(path) + "_encrypted"


def main():
    verify_args()
    path = sys.argv[1]
    key = sys.argv[2]
    encrypted_lines = encrypt(path, key)
    output_path = get_output_path(path)
    write_encrypted(encrypted_lines, output_path)


if __name__ == '__main__':
    main()
