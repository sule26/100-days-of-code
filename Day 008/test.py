from art import logo

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def encrypt(text, shift):
    encrypt_text = ""
    for letter in text:
        position = alphabet.index(letter)
        if letter in alphabet:
            if position + shift > 26:
                position -= 26
            encrypt_text += alphabet[position + shift]
        else:
            encrypt_text += letter
    print(f"The encoded text is {encrypt_text}")


def decrypt(text, shift):
    decrypt_text = ""
    for letter in text:
        position = alphabet.index(letter)
        if letter in alphabet:
            if position - shift < 0:
                position -= 26
            decrypt_text += alphabet[position - shift]
        else:
            decrypt_text += letter
    print(f"The decoded text is {decrypt_text}")


def caesar(text, shift, direction):
    caesar_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            caesar_text += alphabet[new_position]
        else:
            caesar_text += char
    print(f"The {direction}d text is {caesar_text}")


print(logo)

answer = ''
while answer != 'no':
    direction = input("\nType 'encode' to encrypt, type 'decode'to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    caesar(text, shift, direction)
    answer = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()

print("Good bye!")
