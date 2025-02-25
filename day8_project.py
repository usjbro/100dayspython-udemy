## Ceaser Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Pick encrypt or decrypt: ").lower()
text = input("Enter your message: ").lower()
shift = int(input("How many characters would you like the characters shifter? "))

encrypted_text = ""
decrypted_text = ""
# letter_position = []

def encrypt(text, shift, encrypted_text):
    for letter in text:
        current_position = alphabet.index(letter)
        if current_position + shift > 25:
            new_position = current_position + shift - 25
            print(f"new position: {new_position}")
            encrypted_text += alphabet[new_position]
        else:
            new_position = alphabet.index(letter) + shift
            print(f"new position: {new_position}")
            encrypted_text += alphabet[new_position]

        print(f"Your encrypted message is {encrypted_text}")
        #new_position = position + shift
        #print(f"old position: {position} new position: {new_position}")
        


def decrypt(text = text, shift = shift, decrypted_text = decrypted_text):
    for letter in text:
        new_position = alphabet.index(letter) - shift
        #new_position = position + shift
        #print(f"old position: {position} new position: {new_position}")
        print(f"new position: {new_position}")
        encrypted_text += alphabet[new_position]
        print(f"Your encrypted message is {encrypted_text}")

if direction == "encrypt":
    encrypt(text, shift, encrypted_text)
elif direction == "decrypt":
    decrypt(text, shift, decrypted_text)
else:
    print("Unknow selection")