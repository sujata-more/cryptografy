import numpy as np

# Function to convert text to numbers (A=0, B=1, ..., Z=25)
def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text]

# Function to convert numbers to text
def numbers_to_text(numbers):
    return ''.join(chr(num + ord('A')) for num in numbers)

# Function to encrypt the plaintext
def hill_encrypt(plaintext, key_matrix):
    plaintext = plaintext.upper().replace(" ", "")
    
    if len(plaintext) % 2 != 0:  # Pad with an extra 'X' if not even length
        plaintext += 'X'

    plaintext_numbers = text_to_numbers(plaintext)
    encrypted_text = ''

    # Encrypt in blocks of 2 (for 2x2 key matrix)
    for i in range(0, len(plaintext_numbers), 2):
        block = np.array(plaintext_numbers[i:i+2])
        encrypted_block = np.dot(key_matrix, block) % 26
        encrypted_text += numbers_to_text(encrypted_block)

    return encrypted_text

# Function to find the modular inverse of a 2x2 matrix in mod 26
def matrix_mod_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))  # Calculate determinant
    det_inv = pow(det, -1, modulus)  # Modular inverse of determinant
    
    # Inverse of a 2x2 matrix formula
    inv_matrix = det_inv * np.array([[matrix[1][1], -matrix[0][1]],
                                     [-matrix[1][0], matrix[0][0]]])
    return inv_matrix % modulus

# Function to decrypt the ciphertext
def hill_decrypt(ciphertext, key_matrix):
    ciphertext = ciphertext.upper().replace(" ", "")
    ciphertext_numbers = text_to_numbers(ciphertext)
    decrypted_text = ''

    # Find inverse key matrix
    inv_key_matrix = matrix_mod_inv(key_matrix, 26)

    # Decrypt in blocks of 2
    for i in range(0, len(ciphertext_numbers), 2):
        block = np.array(ciphertext_numbers[i:i+2])
        decrypted_block = np.dot(inv_key_matrix, block) % 26
        decrypted_text += numbers_to_text(np.round(decrypted_block).astype(int))

    return decrypted_text

# Example usage
key_matrix = np.array([[3, 3], [2, 5]])  # 2x2 key matrix for Hill Cipher
plaintext = input("Enter the plaintext: ").upper()

# Encrypt the plaintext
encrypted_text = hill_encrypt(plaintext, key_matrix)
print("Encrypted text:", encrypted_text)

# Decrypt the encrypted text
decrypted_text = hill_decrypt(encrypted_text, key_matrix)
print("Decrypted text:", decrypted_text)
