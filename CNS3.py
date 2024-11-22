def generate_key(text, keyword):
    key = list(keyword)
    if len(text) == len(key):
        return "".join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_encrypt(text, keyword):
    key = generate_key(text, keyword)
    encrypted_text = []
    
    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key[i]) - ord('A') if text[i].isupper() else ord(key[i]) - ord('a')
            base = ord('A') if text[i].isupper() else ord('a')
            encrypted_char = chr((ord(text[i]) + shift - base) % 26 + base)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(text[i])  # Non-alphabet characters are not encrypted

    return "".join(encrypted_text)

def vigenere_decrypt(encrypted_text, keyword):
    key = generate_key(encrypted_text, keyword)
    decrypted_text = []

    for i in range(len(encrypted_text)):
        if encrypted_text[i].isalpha():
            shift = ord(key[i]) - ord('A') if encrypted_text[i].isupper() else ord(key[i]) - ord('a')
            base = ord('A') if encrypted_text[i].isupper() else ord('a')
            decrypted_char = chr((ord(encrypted_text[i]) - shift - base) % 26 + base)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(encrypted_text[i])

    return "".join(decrypted_text)

# Get user input
text = input("Enter text to encrypt: ")
keyword = input("Enter the keyword: ")

# Encrypt and display the result
encrypted_text = vigenere_encrypt(text, keyword)
print("Encrypted text:", encrypted_text)

# Decrypt and display the result
decrypted_text = vigenere_decrypt(encrypted_text, keyword)
print("Decrypted text:", decrypted_text)
