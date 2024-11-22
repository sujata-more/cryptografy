# Function to encrypt the plaintext using Rail Fence Cipher
def rail_fence_encrypt(plaintext, num_rails):
    rail = ['' for _ in range(num_rails)]
    direction = None  # To keep track of direction: down or up
    row = 0  # Current row

    # Iterate over each character in the plaintext
    for char in plaintext:
        rail[row] += char  # Place the character in the current rail

        # Change direction if at the top or bottom rail
        if row == 0:
            direction = 1  # Move down
        elif row == num_rails - 1:
            direction = -1  # Move up

        # Move to the next rail
        row += direction

    # Concatenate the rows to get the encrypted text
    encrypted_text = ''.join(rail)
    return encrypted_text

# Function to decrypt the ciphertext using Rail Fence Cipher
def rail_fence_decrypt(ciphertext, num_rails):
    rail = [['\n' for _ in range(len(ciphertext))] for _ in range(num_rails)]
    direction = None
    row, index = 0, 0

    # Mark the positions with '*'
    for char in ciphertext:
        rail[row][index] = '*'
        index += 1

        # Change direction if at the top or bottom rail
        if row == 0:
            direction = 1
        elif row == num_rails - 1:
            direction = -1

        # Move to the next rail
        row += direction

    # Replace '*' with actual characters in ciphertext
    index = 0
    for i in range(num_rails):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*' and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1

    # Read the characters in zigzag to decrypt
    decrypted_text = []
    row, direction = 0, 1
    for i in range(len(ciphertext)):
        decrypted_text.append(rail[row][i])

        # Change direction if at the top or bottom rail
        if row == 0:
            direction = 1
        elif row == num_rails - 1:
            direction = -1

        row += direction

    return ''.join(decrypted_text)

# Example usage
plaintext = input("Enter the plaintext: ")
num_rails = int(input("Enter the number of rails: "))

# Encrypt the plaintext
encrypted_text = rail_fence_encrypt(plaintext, num_rails)
print("Encrypted text:", encrypted_text)

# Decrypt the ciphertext
decrypted_text = rail_fence_decrypt(encrypted_text, num_rails)
print("Decrypted text:", decrypted_text)
