alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Decode(message, shift):
    output_text = ""

    for letter in message:

        if letter not in alphabet:
            output_text += letter

        shifted_position = alphabet.index(letter) - shift 
        shifted_position %= len(alphabet) 
        output_text += alphabet[shifted_position]

    print(f"The decrypted message is: {output_text}")