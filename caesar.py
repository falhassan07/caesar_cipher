from art import logo 

print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

action = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
text = input("Enter your message:\n").lower()
shift = int(input("Enter shift number:\n"))


def caesar(original_text, shift_amount, encode_decode):
    output_text = ""

    if encode_decode == 'decode':
        shift_amount *= -1

    for char in original_text:
        shifted_index = alphabet.index(char) + shift_amount
        shifted_index = shifted_index % len(alphabet)
        output_text += alphabet[shifted_index]
    print(f"{encode_decode}d message: {output_text}")


caesar(text, shift, action)