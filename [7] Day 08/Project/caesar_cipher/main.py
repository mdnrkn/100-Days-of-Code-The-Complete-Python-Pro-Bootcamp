from encode import Encode
from decode import Decode

print("Welcome to the Caesar Cipher!")
should_continue = True

while should_continue:
    operation = input("Type 'encode' to Encrypt, or 'decode' to Decrypt:\n")
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    if operation == "encode":
        Encode(message, shift)
    elif operation == "decode":
        Decode(message, shift)
    else:
        print("Invalid operation.")

    restart = input("Do you want to restart the program? Type 'yes' or 'no':\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")