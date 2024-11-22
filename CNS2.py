# Function to generate the full repeating keyword for encryption/decryption
def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

# Function to encrypt the plaintext
def polyalphabetic_encrypt(plaintext, keyword):
    plaintext = plaintext.upper().replace(" ", "")
    keyword = generate_key(plaintext, keyword).upper()
    encrypted_text = []

    for i in range(len(plaintext)):
        # Shift character based on keyword
        shift = (ord(plaintext[i]) + ord(keyword[i])) % 26
        encrypted_text.append(chr(shift + ord('A')))
    
    return "".join(encrypted_text)

# Function to decrypt the ciphertext
def polyalphabetic_decrypt(ciphertext, keyword):
    ciphertext = ciphertext.upper().replace(" ", "")
    keyword = generate_key(ciphertext, keyword).upper()
    decrypted_text = []

    for i in range(len(ciphertext)):
        # Reverse the shift
        shift = (ord(ciphertext[i]) - ord(keyword[i]) + 26) % 26
        decrypted_text.append(chr(shift + ord('A')))
    
    return "".join(decrypted_text)

# Example usage
plaintext = input("Enter the plaintext: ").upper()
keyword = input("Enter the keyword: ").upper()

# Encrypt the plaintext
encrypted_text = polyalphabetic_encrypt(plaintext, keyword)
print("Encrypted text:", encrypted_text)

# Decrypt the encrypted text
decrypted_text = polyalphabetic_decrypt(encrypted_text, keyword)
print("Decrypted text:", decrypted_text)
