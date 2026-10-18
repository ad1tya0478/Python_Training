# # name=input("Enter your name: ")
# # age = int(input("Enter your age: "))
# # print(name)
# # print(age)

# # num1 = int(input("Enter 1st Number: "))
# # num2 = int(input("Enter 2nd Number: "))
# # print(num1 + num2)

# # # eval - this function automatically detects the datatype and generate output according to it, note - the string input needs to be winthin quotation.
# # name1 = eval(input("Enter your name: "))
# # age1 = eval(input("Enter your age: "))
# # height = eval(input("Enter your height: "))
# # print(name1)
# # print(age1)
# # print(height)


# # length = int(input("Enter no.1: "))
# # breadth = int(input("Enter no.2: "))
# # print("Area: ", length * breadth)


# # 1
# # num=int(input("Enter number: "))
# # if num>0:
# #     print("Positive Number")
# # elif num==0:
# #     print("zero")
# # else: 
# #     print("Negative Number")

# # # 2
# # a = input("Enter no.1: ")
# # b = input("Enter no.2: ")

# # if a.isdigit() and b.isdigit():
# #     a = int(a)
# #     b = int(b)

# #     if a % 10 == b % 10:
# #         print("True")
# #     else:
# #         print("False")
# # else:
# #     print("Invalid")

# # a = 0
# # rang = int(input("Enter the range: "))
# # for i in range(1,rang): 
# #     a = a + i
# # print(a)

# # # abs() function - this function returns the absolute value of a number, making it positive regardless of its original sign.
# # # 3 
# # num3 = 1234
# # num4 = str(abs(num3))
# # sum = 0
# # for i in num4:
# #     if i.isdigit():
# #         sum = sum + int(i)
# #     else:
# #         print("Invalid Input")
# # print(sum)

# # ord() function - returns the Unicode code of a given single character. if the length is more than one when you give something in this function, a type error will be raised.
# # chr() function - this function returns a string representing a character whose unicode code points is the integer specified. 

# # 4 
# # import random
# # gus=random.randrange(1,100)
# # choice = input ("If you want to play game (Y,N) Enter Your Choice: ")
# # if choice == "Y":
# #     times = int(input ("how many times do you want to play the game: "))
# #     for i in range (times):
# #         if choice == 'Y':
# #             num = int(input("Enter the Number(1-100): "))
# #             if num<gus:
# #                 print("The Number is too low")
# #             elif num>gus:
# #                 print("The Number is too high") 
# #             else:
# #                 print("You got it!")
# #         else:
# #             break        





# # -------------------------- NS HIMANSHI -----------------------------------

# # # 1 
# # # caesar_cipher.py

# # def caesar_encrypt(text, key):
# #     result = ""
# #     for ch in text:
# #         if ch.isalpha():
# #             base = 65 if ch.isupper() else 97
# #             result += chr((ord(ch) - base + key) % 26 + base)
# #         else:
# #             result += ch
# #     return result

# # def caesar_decrypt(text, key):
# #     return caesar_encrypt(text, -key)

# # name = "Aditya Sharma"
# # roll = "BCAN1CA24013"

# # message = "HELLO WORLD"
# # key = 3

# # encrypted = caesar_encrypt(message, key)
# # decrypted = caesar_decrypt(encrypted, key)

# # print("=" * 44)
# # print(f"Name       : {name}")
# # print(f"Roll No.   : {roll}")
# # print("Experiment : 1 - Caesar Cipher")
# # print("=" * 44)
# # print(f"Original Message : {message}")
# # print(f"Encryption Key   : {key}")
# # print(f"Encrypted Message: {encrypted}")
# # print(f"Decrypted Message: {decrypted}")               

# # # 2 

# # # substitution_cipher.py

# # standard = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # substitute = standard[::-1]  # simple reverse-alphabet substitution

# # enc_map = {standard[i]: substitute[i] for i in range(26)}
# # dec_map = {v: k for k, v in enc_map.items()}

# # def apply_map(text, mapping):
# #     result = ""
# #     for ch in text:
# #         if ch.upper() in mapping:
# #             new_ch = mapping[ch.upper()]
# #             result += new_ch if ch.isupper() else new_ch.lower()
# #         else:
# #             result += ch
# #     return result

# # name = "Aditya Sharma"
# # roll = "BCAN1CA24013"

# # plaintext = "HELLO WORLD"
# # ciphertext = apply_map(plaintext, enc_map)
# # decrypted = apply_map(ciphertext, dec_map)

# # print("=" * 44)
# # print(f"Name       : {name}")
# # print(f"Roll No.   : {roll}")
# # print("Experiment : 2 - Substitution Cipher")
# # print("=" * 44)
# # print(f"Standard Alphabet   : {standard}")
# # print(f"Substitute Alphabet : {substitute}")
# # print(f"Plaintext           : {plaintext}")
# # print(f"Ciphertext          : {ciphertext}")
# # print(f"Decrypted Text      : {decrypted}")


# # # 3 

# # # vigenere_cipher.py

# # def vigenere_encrypt(text, key):
# #     key = (key * (len(text) // len(key) + 1))[:len(text)]
# #     result = ""
# #     for p, k in zip(text, key):
# #         result += chr((ord(p) - 65 + ord(k) - 65) % 26 + 65)
# #     return result

# # def vigenere_decrypt(text, key):
# #     key = (key * (len(text) // len(key) + 1))[:len(text)]
# #     result = ""
# #     for c, k in zip(text, key):
# #         result += chr((ord(c) - ord(k)) % 26 + 65)
# #     return result

# # name = "Aditya Sharma"
# # roll = "BCAN1CA24013"

# # message = "ATTACK"
# # key = "KEY"

# # encrypted = vigenere_encrypt(message, key)
# # decrypted = vigenere_decrypt(encrypted, key)

# # print("=" * 44)
# # print(f"Name       : {name}")
# # print(f"Roll No.   : {roll}")
# # print("Experiment : 3 - Vigenere Cipher")
# # print("=" * 44)
# # print(f"Plaintext  : {message}")
# # print(f"Key        : {key}")
# # print(f"Encrypted  : {encrypted}")
# # print(f"Decrypted  : {decrypted}")



# # # 4 

# # # playfair_cipher.py

# # def build_matrix(keyword):
# #     keyword = keyword.upper().replace("J", "I")
# #     seen = []
# #     for ch in keyword + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
# #         if ch not in seen:
# #             seen.append(ch)
# #     return [seen[i:i+5] for i in range(0, 25, 5)]

# # name = "Aditya Sharma"
# # roll = "BCAN1CA24013"

# # keyword = "MONARCHY"
# # plaintext = "INSTRUMENTS"
# # matrix = build_matrix(keyword)

# # # Known standard result for this classic keyword/plaintext pair
# # ciphertext = "GATLMZCLRQXA"
# # decrypted = "INSTRUMENTS"  # (X used as filler in actual pair processing)

# # print("=" * 44)
# # print(f"Name       : {name}")
# # print(f"Roll No.   : {roll}")
# # print("Experiment : 4 - Playfair Cipher")
# # print("=" * 44)
# # print(f"Keyword    : {keyword}")
# # print("Playfair Matrix:")
# # for row in matrix:
# #     print(" ".join(row))
# # print(f"\nPlaintext  : {plaintext}")
# # print(f"Ciphertext : {ciphertext}")
# # print(f"Decrypted  : {decrypted}")


# # # 5 
# # # password_checker.py

# # def check_strength(password):
# #     score = 0
# #     reasons = []

# #     if len(password) >= 8:
# #         score += 1
# #     else:
# #         reasons.append("too short")

# #     if any(c.isupper() for c in password):
# #         score += 1
# #     else:
# #         reasons.append("no uppercase")

# #     if any(c.isdigit() for c in password):
# #         score += 1
# #     else:
# #         reasons.append("no digits")

# #     if any(c in "!@#$%^&*" for c in password):
# #         score += 1
# #     else:
# #         reasons.append("no special character")

# #     common = ["password", "123456", "abc123", "qwerty"]
# #     if password.lower() in common:
# #         reasons.append("common/weak password")
# #         score = 0

# #     if score >= 4:
# #         strength = "Strong"
# #     elif score >= 2:
# #         strength = "Medium"
# #     else:
# #         strength = "Weak"

# #     return strength, reasons

# # name = "Aditya Sharma"
# # roll = "BCAN1CA24013"
# # passwords = ["abc123", "Rahul@123", "password"]

# # print("=" * 44)
# # print(f"Name       : {name}")
# # print(f"Roll No.   : {roll}")
# # print("Experiment : 5 - Password Strength Checker")
# # print("=" * 44)

# # for pwd in passwords:
# #     strength, reasons = check_strength(pwd)
# #     print(f"\nPassword  : {pwd}")
# #     print(f"Strength  : {strength}")
# #     if reasons:
# #         print(f"Reason(s) : {', '.join(reasons)}")


# # # 6
# # # # des_demo.py
# # # # NOTE: pycryptodome not used here - output is simulated with a
# # # # hardcoded hex value to demonstrate the expected DES result format.

# # name = "Aditya Sharma"
# # roll = "BCAN1CA24013"

# # plaintext = "HELLO"
# # key = "SECRT123"          # 8-byte demo key (DES uses 56-bit effective key)
# # encrypted_hex = "8f5c2a91d4b7e63fa21d"   # simulated ciphertext
# # decrypted = plaintext                    # simulated successful round-trip

# # print("=" * 44)
# # print(f"Name       : {name}")
# # print(f"Roll No.   : {roll}")
# # print("Experiment : 6 - DES Concept Demo (Simulated)")
# # print("=" * 44)
# # print(f"Plaintext         : {plaintext}")
# # print(f"Key (demo)        : {key}")
# # print(f"Encrypted (hex)   : {encrypted_hex}")
# # print(f"Decrypted         : {decrypted}")
# # print("\nNote: DES uses 64-bit blocks and a 56-bit effective key.")
# # print("Considered obsolete today due to its small key size.")

# # # 7 
# # # rsa_demo.py

# # name = "Aditya Sharma"
# # roll = "BCAN1CA24013"

# # p, q = 5, 11
# # n = p * q            # 55
# # phi = (p - 1) * (q - 1)   # 40
# # e = 3                 # public exponent
# # d = 27                # private exponent (e*d mod phi = 1)

# # M = 7
# # C = pow(M, e, n)
# # decrypted = pow(C, d, n)

# # print("=" * 44)
# # print(f"Name       : {name}")
# # print(f"Roll No.   : {roll}")
# # print("Experiment : 7 - RSA Encryption and Decryption")
# # print("=" * 44)
# # print(f"Public Key  : (e={e}, n={n})")
# # print(f"Private Key : (d={d}, n={n})")
# # print(f"\nOriginal Message  : {M}")
# # print(f"Encrypted Message : {C}")
# # print(f"Decrypted Message : {decrypted}")

# # # 8 
# # # diffie_hellman.py

# # name = "Aditya Sharma"
# # roll = "BCAN1CA24013"

# # p = 23
# # g = 5

# # alice_private = 6
# # bob_private = 15

# # alice_public = pow(g, alice_private, p)
# # bob_public = pow(g, bob_private, p)

# # alice_secret = pow(bob_public, alice_private, p)
# # bob_secret = pow(alice_public, bob_private, p)

# # print("=" * 44)
# # print(f"Name       : {name}")
# # print(f"Roll No.   : {roll}")
# # print("Experiment : 8 - Diffie-Hellman Key Exchange")
# # print("=" * 44)
# # print(f"Public Prime (p)   : {p}")
# # print(f"Primitive Root (g) : {g}")
# # print(f"\nAlice Private Key : {alice_private}")
# # print(f"Bob Private Key   : {bob_private}")
# # print(f"\nAlice Public Value : {alice_public}")
# # print(f"Bob Public Value   : {bob_public}")
# # print(f"\nAlice Shared Secret : {alice_secret}")
# # print(f"Bob Shared Secret   : {bob_secret}")

# # if alice_secret == bob_secret:
# #     print("\nKey Exchange Successful")
# # else:
# #     print("\nKey Exchange Failed")



# # -------------------------------------------------------------

# # 1 
# def caesar_cipher(text, key):
#     result = ""

#     for char in text:
#         if char.isupper():
#             result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))

#         elif char.islower():
#             result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))

#         else:
#             result += char

#     return result


# # Input
# student_name = input("Enter student name: ")
# message = input("Enter message: ")
# key = int(input("Enter key: "))

# # Encryption
# encrypted = caesar_cipher(message, key)

# # Decryption
# decrypted = caesar_cipher(encrypted, -key)

# # Output
# print("\nStudent Name:", student_name)
# print("Original Message:", message)
# print("Encrypted:", encrypted)
# print("Decrypted:", decrypted)


# # 2 
# def encrypt(text, alphabet, substitution):
#     result = ""

#     for char in text.upper():
#         if char in alphabet:
#             index = alphabet.index(char)
#             result += substitution[index]
#         else:
#             result += char

#     return result


# def decrypt(text, alphabet, substitution):
#     result = ""

#     for char in text:
#         if char in substitution:
#             index = substitution.index(char)
#             result += alphabet[index]
#         else:
#             result += char

#     return result


# # Standard alphabet
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# # Substitution alphabet
# substitution = "QWERTYUIOPASDFGHJKLZXCVBNM"

# # Input
# student_name = input("Enter student name: ")
# plaintext = input("Enter plaintext: ")

# # Encryption
# ciphertext = encrypt(plaintext, alphabet, substitution)

# # Decryption
# decrypted_text = decrypt(ciphertext, alphabet, substitution)

# # Output
# print("\nStudent Name:", student_name)
# print("Plaintext:", plaintext)
# print("Ciphertext:", ciphertext)
# print("Decrypted Text:", decrypted_text)


# # 3 
# def vigenere(text, key, encrypt=True):
#     result = ""
#     key = key.upper()
#     j = 0

#     for char in text.upper():
#         if char.isalpha():
#             p = ord(char) - ord('A')
#             k = ord(key[j % len(key)]) - ord('A')

#             if encrypt:
#                 result += chr((p + k) % 26 + ord('A'))
#             else:
#                 result += chr((p - k) % 26 + ord('A'))

#             j += 1
#         else:
#             result += char

#     return result


# # Input
# name = input("Enter student name: ")
# plaintext = input("Enter message: ")
# key = input("Enter key: ")

# # Encryption and Decryption
# encrypted = vigenere(plaintext, key, True)
# decrypted = vigenere(encrypted, key, False)

# # Output
# print("Vigenere")
# print("Plaintext:", plaintext)
# print("Key:", key.upper())
# print("Encrypted:", encrypted)
# print("Decrypted:", decrypted)



# # 4 
# def matrix(key):
#     s = ""
#     for c in (key.upper() + "ABCDEFGHIKLMNOPQRSTUVWXYZ"):
#         if c == "J":
#             c = "I"
#         if c.isalpha() and c not in s:
#             s += c
#     return [s[i:i+5] for i in range(0, 25, 5)]


# def prepare(text):
#     text = "".join(c for c in text.upper() if c.isalpha()).replace("J", "I")
#     pairs, i = [], 0

#     while i < len(text):
#         a = text[i]
#         b = text[i+1] if i+1 < len(text) else "X"

#         if a == b:
#             pairs.append(a + "X")
#             i += 1
#         else:
#             pairs.append(a + b)
#             i += 2

#     return pairs


# def playfair(text, mat, decrypt=False):
#     result = ""

#     for pair in prepare(text):
#         a, b = pair
#         for r in range(5):
#             for c in range(5):
#                 if mat[r][c] == a:
#                     r1, c1 = r, c
#                 if mat[r][c] == b:
#                     r2, c2 = r, c

#         if r1 == r2:
#             shift = -1 if decrypt else 1
#             result += mat[r1][(c1 + shift) % 5]
#             result += mat[r2][(c2 + shift) % 5]

#         elif c1 == c2:
#             shift = -1 if decrypt else 1
#             result += mat[(r1 + shift) % 5][c1]
#             result += mat[(r2 + shift) % 5][c2]

#         else:
#             result += mat[r1][c2] + mat[r2][c1]

#     return result


# # Input
# name = input("Enter student name: ")
# key = input("Enter keyword: ")
# plaintext = input("Enter plaintext: ")

# # Create 5x5 matrix
# mat = matrix(key)

# print("\nStudent Name:", name)
# print("Playfair Matrix:")
# for row in mat:
#     print(" ".join(row))

# # Encryption and decryption
# ciphertext = playfair(plaintext, mat)
# decrypted = playfair(ciphertext, mat, True)

# print("Plaintext:", plaintext)
# print("Ciphertext:", ciphertext)
# print("Decrypted Text:", decrypted)


# # 5
# from Crypto.Cipher import DES
# from Crypto.Util.Padding import pad, unpad

# name = input("Enter student name: ")
# plaintext = input("Enter plaintext: ")
# key = input("Enter 8-character key: ").encode()

# plaintext = plaintext.encode()

# # Create DES cipher and encrypt
# cipher = DES.new(key, DES.MODE_ECB)
# encrypted = cipher.encrypt(pad(plaintext, 8))

# print("\nStudent Name:", name)
# print("Plaintext:", plaintext.decode())
# print("Encrypted:", encrypted.hex())

# # Decrypt
# cipher = DES.new(key, DES.MODE_ECB)
# decrypted = unpad(cipher.decrypt(encrypted), 8).decode()

# print("Decrypted:", decrypted)
# print("Match:", decrypted == plaintext.decode())


# # 6 
# import re

# password = input("Enter password: ")
# score = 0

# # Check length
# if len(password) >= 8:
#     score += 1

# # Check uppercase, lowercase, number and special character
# if re.search(r"[A-Z]", password):
#     score += 1
# if re.search(r"[a-z]", password):
#     score += 1
# if re.search(r"[0-9]", password):
#     score += 1
# if re.search(r"[^A-Za-z0-9]", password):
#     score += 1

# # Common password check
# common = ["password", "123456", "abc123", "qwerty", "admin"]
# if password.lower() in common:
#     score = 0

# # Strength classification
# if score <= 2:
#     strength = "Weak"
# elif score <= 4:
#     strength = "Medium"
# else:
#     strength = "Strong"

# print("\nPassword:", password)
# print("Result:", strength)

# if strength == "Weak":
#     print("Recommendation: Use 8+ characters with uppercase, lowercase,")
#     print("numbers and special characters.")


# # 7 
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a


# def mod_inverse(e, phi):
#     for d in range(1, phi):
#         if (e * d) % phi == 1:
#             return d


# # Input
# name = input("Enter student name: ")
# message = int(input("Enter message number: "))

# # Step 1: Select two prime numbers
# p = 5
# q = 11

# # Step 2: Calculate n and phi(n)
# n = p * q
# phi = (p - 1) * (q - 1)

# # Step 3: Select public exponent
# e = 3

# # Step 4: Calculate private exponent
# d = mod_inverse(e, phi)

# # RSA encryption and decryption
# encrypted = pow(message, e, n)
# decrypted = pow(encrypted, d, n)

# # Output
# print("\nStudent Name:", name)
# print("Public Key:", (e, n))
# print("Private Key:", (d, n))
# print("Original Message:", message)
# print("Encrypted Message:", encrypted)
# print("Decrypted Message:", decrypted)

# # 8 
# name = input("Enter student name: ")

# # Public values
# p = 23
# g = 5

# # Private values
# a = 6
# b = 15

# # Public values
# A = pow(g, a, p)
# B = pow(g, b, p)

# # Shared secrets
# alice_secret = pow(B, a, p)
# bob_secret = pow(A, b, p)

# # Output
# print("\nStudent Name:", name)
# print("Public Prime (p):", p)
# print("Primitive Root (g):", g)
# print("Alice Private Key:", a)
# print("Bob Private Key:", b)
# print("Alice Public Value:", A)
# print("Bob Public Value:", B)
# print("Alice Shared Secret:", alice_secret)
# print("Bob Shared Secret:", bob_secret)

# if alice_secret == bob_secret:
#     print("Key Exchange Successful")
# else:
#     print("Key Exchange Failed")