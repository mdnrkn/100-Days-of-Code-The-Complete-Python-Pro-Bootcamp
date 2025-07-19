alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Encode(message, shift):
    cipher_text = ""

    for letter in message:

        if letter not in alphabet:
            cipher_text += letter

        shifted_position = alphabet.index(letter) + shift 
        shifted_position %= len(alphabet) 
        cipher_text += alphabet[shifted_position]

    print(f"The encrypted message is: {cipher_text}")