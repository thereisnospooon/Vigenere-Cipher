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
        print("Usage: python3 Decrypt.py <input file> <key>")
        exit(1)
    elif not os.path.exists(sys.argv[1]):
        print("path is not valid")
        exit(1)
    elif not isinstance(sys.argv[1], str) or not isinstance(sys.argv[2], str):
        print("path and key should be strings")
        exit(1)


def decrypt_letter(char: str, decrypt_var: str):
    """
    Given a letter from the text input and a char from the key, this function returns the letter after
    decryption
    :param char: Char from input text file
    :param decrypt_var: corresponding char from key
    :return: A char after decryption
    """
    if char is " ":
        return char
    if char.isalpha():
        if decrypt_var.isupper():
            val = (ord(char) - (ord(decrypt_var) - UPPER_CYCLE))
            if char.isupper() and val < ord("A"):
                return chr(val + ord("A"))
            elif char.islower() and val < ord("a"):
                return chr(val + ord("a"))
            else:
                return chr(val)
        else:
            val = (ord(char) - (ord(decrypt_var) - LOWER_CYCLE))
            if char.isupper() and val < ord("A"):
                return chr(val + ord("A"))
            elif char.islower() and val < ord("a"):
                return chr(val + ord("a"))
            else:
                return chr(val)
    else:
        return char


def decrypt(path: str, key: str):
    """
    Opens the file specified by path and encrypts the text in it using vigenere cipher and
    key.
    :param path: path to the text file to encrypt.
    :param key: key of the encryption
    :return: lines of encrypted text
    """
    decrypted_lines = []
    counter = 0
    with open(path, "r") as input_file:
        for line in input_file.readlines():
            cur_line = ""
            for char in line:
                cur_line += decrypt_letter(char, key[counter % len(key)])
                counter += 1
            decrypted_lines.append(cur_line)
    return decrypted_lines


def write_encrypted(decrypted_lines: list, output_path: str):
    """
    Given a list of encrypted lines, this function writes them to Outputs directory
    :param output_path: Path of output file
    :param decrypted_lines:
    :return:
    """
    with open(output_path, "w") as target:
        for line in decrypted_lines:
            target.write(line)


def get_output_path(path: str):
    """
    Given a path, this function extracts the name of the file and appends "_encrypted"
    :param path: path to file to encrypt
    :return: a string containing the name of the output file
    """
    if not os.path.exists("../Outputs"):
        os.makedirs("../Outputs")
    return "../Outputs/" + os.path.basename(path) + "_decrypted"


def main():
    verify_args()
    path = sys.argv[1]
    key = sys.argv[2]
    decrypted_lines = decrypt(path, key)
    output_path = get_output_path(path)
    write_encrypted(decrypted_lines, output_path)


if __name__ == '__main__':
    main()
