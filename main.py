# def greet():
#     print("Hello World")
#     print("Hello again")
#     print("I'm a module")
# greet()
# import math
# def number_of_cans(height1, width1, coverage1):
#     print(f"you will need {math.ceil(height1 * width1 / coverage1)} cans of paint")
# height = int(input("Enter height: "))
# width = int(input("Enter weight: "))
# coverage = 5
# number_of_cans(height, width, coverage)
# #prime number checker
# def prime_checker (number):
#     prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             prime = False
#             break
#     if prime:
#         print("It is a prime number.")
#     else:
#         print("It is not a prime number.")
# n = int(input("Enter a number: "))
# prime_checker(number = n)
#Ceaser Cipher Project
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(directing, texting, shifting):
    code = list(texting)
    for i in range(len(code)):
        if code[i] in alphabet:
            if directing == 'encode':
                letter = alphabet.index(code[i]) + shifting
                if letter > 25:
                    letter = letter % 26
                    code[i] = alphabet[letter]
                else:
                    code[i] = alphabet[letter]
            elif directing == 'decode':
                letter = alphabet.index(code[i]) - shifting
                if letter <- 26:
                    letter =  (letter % 26)
                    code[i] = alphabet[letter]
                else:
                     code[i] = alphabet[letter]
        else:
            code[i]= code[i]
    print(f"The {directing}d message is '{''.join(code)}'")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    result = input("Type 'yes' to continue. Type 'no' to exit the program:\n").lower()
    if result == 'no':
        print("Goodbye!")
        break
