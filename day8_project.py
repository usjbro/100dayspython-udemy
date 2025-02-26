## Ceaser Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Pick encrypt or decrypt: ").lower()
text = input("Enter your message: ").lower()
shift = int(input("How many characters would you like the characters shifter? "))


# letter_position = []

def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:
            current_position = alphabet.index(letter)
            new_position = (current_position + shift) % len(alphabet)
            encrypted_text += alphabet[new_position]
            print(f"new position: {new_position}")
        else:
            encrypted_text += alphabet[new_position]
        return encrypted_text
        #new_position = position + shift
        #print(f"old position: {position} new position: {new_position}")
        


def decrypt(text, shift):
    decrypted_text = ""
    for letter in text:
        if letter in alphabet:
            current_position = alphabet.index(letter)
            new_position = (current_position - shift) % len(alphabet)
            decrypted_text += alphabet[new_position]
            print(f"new position: {new_position}")
        else:
            decrypted_text += letter
    return decrypted_text

if direction == "encrypt":
    result = encrypt(text, shift)
    print(f"Your encrypted message is {result}")
elif direction == "decrypt":
    result = decrypt(text, shift)
    print(f"Your decrypted message is {result}")

else:
    print("Unknow selection")