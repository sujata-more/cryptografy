import math

# Function to encrypt the message using Advanced Columnar Transposition
def encrypt_message(message, key):
    # Calculate the number of columns based on the key length
    num_cols = len(key)
    
    # Calculate the number of rows required to fit the message
    num_rows = math.ceil(len(message) / num_cols)
    
    # Pad the message with spaces if necessary
    padding_length = (num_rows * num_cols) - len(message)
    message += ' ' * padding_length
    
    # Create the matrix
    matrix = [message[i:i + num_cols] for i in range(0, len(message), num_cols)]
    
    # Sort the key to determine column order for transposition
    key_order = sorted(list(key))
    
    # Encrypt the message by reading columns in the key order
    encrypted_message = ''
    for k in key_order:
        col_idx = key.index(k)
        for row in matrix:
            encrypted_message += row[col_idx]
    
    return encrypted_message


# Function to decrypt the message using Advanced Columnar Transposition
def decrypt_message(encrypted_message, key):
    # Calculate the number of columns based on the key length
    num_cols = len(key)
    
    # Calculate the number of rows required
    num_rows = math.ceil(len(encrypted_message) / num_cols)
    
    # Create an empty matrix with the same number of rows and columns
    matrix = [''] * num_cols
    
    # Sort the key to determine column order for decryption
    key_order = sorted(list(key))
    
    # Fill the matrix with encrypted message in column order
    idx = 0
    for k in key_order:
        col_idx = key.index(k)
        for i in range(num_rows):
            if idx < len(encrypted_message):
                matrix[col_idx] += encrypted_message[idx]
                idx += 1
    
    # Decrypt the message by reading rows
    decrypted_message = ''
    for i in range(num_rows):
        for j in range(num_cols):
            decrypted_message += matrix[j][i] if i < len(matrix[j]) else ''
    
    return decrypted_message.strip()


# Main program with user input
if __name__ == "__main__":
    # Take input from the user
    message = input("Enter the message to encrypt: ")
    key = input("Enter the encryption key: ")
    
    # Encrypt the message
    encrypted = encrypt_message(message, key)
    print(f"Encrypted Message: {encrypted}")
    
    # Decrypt the message
    decrypted = decrypt_message(encrypted, key)
    print(f"Decrypted Message: {decrypted}")
