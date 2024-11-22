def caesar_cipher(text, shift):
    result = ""

    # Loop through each character in the text
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # For non-alphabetical characters, leave as is
        else:
            result += char

    return result

# Input the text to be encrypted and the shift key
text = input("Enter the text to encrypt: ")
shift = int(input("Enter shift key: "))

# Encrypt the text
encrypted_text = caesar_cipher(text, shift)
print("Encrypted text:", encrypted_text)
