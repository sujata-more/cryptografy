import math
# Function to encrypt the plaintext using Columnar Transposition Cipher
def columnar_transposition_encrypt(plaintext, key):
    # Remove spaces from plaintext and calculate the number of columns
    plaintext = plaintext.replace(" ", "")
    num_columns = len(key)
    num_rows = math.ceil(len(plaintext) / num_columns)

    # Fill the grid with characters of plaintext row-wise
    grid = ['' for _ in range(num_columns)]
    for i, char in enumerate(plaintext):
        col = i % num_columns
        grid[col] += char

    # Sort columns according to the key and create the encrypted text
    sorted_key = sorted(enumerate(key), key=lambda x: x[1])
    encrypted_text = ''.join(grid[col] for col, _ in sorted_key)
    
    return encrypted_text

# Function to decrypt the ciphertext using Columnar Transposition Cipher
def columnar_transposition_decrypt(ciphertext, key):
    # Calculate the number of columns and rows
    num_columns = len(key)
    num_rows = math.ceil(len(ciphertext) / num_columns)
    
    # Determine the order of columns based on the sorted key
    sorted_key = sorted(enumerate(key), key=lambda x: x[1])
    
    # Fill the grid with characters column-wise from ciphertext
    grid = ['' for _ in range(num_columns)]
    index = 0
    for col, _ in sorted_key:
        col_length = num_rows - (1 if col >= len(ciphertext) % num_columns and len(ciphertext) % num_columns != 0 else 0)
        grid[col] = ciphertext[index:index + col_length]
        index += col_length

    # Read the characters row by row to get the decrypted text
    decrypted_text = ''.join(grid[col][row] for row in range(num_rows) for col in range(num_columns) if row < len(grid[col]))
    
    return decrypted_text

# Example usage
plaintext = input("Enter the plaintext: ")
key = input("Enter the key (string without repeating characters): ")

# Encrypt the plaintext
encrypted_text = columnar_transposition_encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)

# Decrypt the ciphertext
decrypted_text = columnar_transposition_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
