alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

action = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
text = input("Enter your message:\n").lower()
shift = int(input("Enter shift number:\n"))


def decrypt(original_text, shift_amount):
    output_text = ""
    for char in original_text:
        shifted_index = alphabet.index(char) - shift_amount
        shifted_index = shifted_index % len(alphabet)
        output_text += alphabet[shifted_index]
    print(f"Decrypted message: {output_text}")


decrypt(text, shift)
