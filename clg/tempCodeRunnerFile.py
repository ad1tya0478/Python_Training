def caesar_cipher(text, key):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))

        elif char.islower():
            result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))

        else:
            result += char

    return result


# Input
student_name = input("Enter student name: ")
message = input("Enter message: ")
key = int(input("Enter key: "))

# Encryption
encrypted = caesar_cipher(message, key)

# Decryption
decrypted = caesar_cipher(encrypted, -key)

# Output
print("\nStudent Name:", student_name)
print("Original Message:", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)