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
        if letter in alphabet:
            current_position = alphabet.index(letter)
            new_position = (current_position + shift) % len(alphabet)
            encrypted_text += alphabet[new_position]
            print(f"new position: {new_position}")
        else:
            new_position = alphabet.index(letter) + shift
            print(f"new position: {new_position}")
            encrypted_text += alphabet[new_position]

        print(f"Your encrypted message is {encrypted_text}")
        #new_position = position + shift
        #print(f"old position: {position} new position: {new_position}")
        


def decrypt(text, shift, decrypted_text):
    for letter in text:
        if letter in alphabet:
            current_position = alphabet.index(letter)
            new_position = (current_position - shift) % len(alphabet)
            decrypted_text += alphabet[new_position]
            print(f"new position: {new_position}")
        else:
            decrypted_text += letter

        print(f"Your decrypted message is {encrypted_text}")

if direction == "encrypt":
    encrypt(text, shift, encrypted_text)
elif direction == "decrypt":
    decrypt(text, shift, decrypted_text)
else:
    print("Unknow selection")