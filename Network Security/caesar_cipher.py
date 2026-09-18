

def caesar_cipher(text, key):
    result = " "

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            result += char

    return result


plaintext = input("Enter the PlainText: ")
key = int(input("Enter The encryption key: "))

ciphertext = caesar_cipher(plaintext, key)
print("Encrypted Text: ", ciphertext)

decrypted_text = caesar_cipher(ciphertext, -key)
print("Decrypted Text: ", decrypted_text)
