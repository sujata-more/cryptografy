# S-DES Program in Python

# Function to perform permutation
def permute(bits, table):
    return [bits[i] for i in table]

# Function to perform left circular shift
def left_shift(bits, n):
    return bits[n:] + bits[:n]

# Function to XOR two bit sequences
def xor(bits1, bits2):
    return [str(int(b1) ^ int(b2)) for b1, b2 in zip(bits1, bits2)]

# S-Boxes
S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

# Initial Permutation (IP)
IP = [1, 5, 2, 0, 3, 7, 4, 6]

# Inverse Initial Permutation (IP^-1)
IP_inv = [3, 0, 2, 4, 6, 1, 7, 5]

# Expansion/Permutation (EP)
EP = [3, 0, 1, 2, 1, 2, 3, 0]

# P4 permutation
P4 = [1, 3, 2, 0]

# P10 permutation
P10 = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]

# P8 permutation
P8 = [5, 2, 6, 3, 7, 4, 9, 8]

# Function to generate keys K1 and K2
def key_generation(key):
    # Perform P10 permutation
    key = permute(key, P10)
    
    # Split the key into two halves
    left, right = key[:5], key[5:]
    
    # Perform left shifts and generate K1
    left, right = left_shift(left, 1), left_shift(right, 1)
    K1 = permute(left + right, P8)
    
    # Perform left shifts again and generate K2
    left, right = left_shift(left, 2), left_shift(right, 2)
    K2 = permute(left + right, P8)
    
    return K1, K2

# Function to perform the S-box lookup
def sbox(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return format(sbox[row][col], '02b')

# Function for fK (round function)
def fk(bits, key):
    left, right = bits[:4], bits[4:]
    
    # Perform expansion/permutation on right half
    right_expanded = permute(right, EP)
    
    # XOR with key
    temp = xor(right_expanded, key)
    
    # Split and apply S-boxes
    left_sbox = sbox(temp[:4], S0)
    right_sbox = sbox(temp[4:], S1)
    
    # Apply P4 permutation
    sbox_output = permute(left_sbox + right_sbox, P4)
    
    # XOR with left half
    result = xor(left, sbox_output)
    
    return result + right

# Function to perform the encryption
def encrypt(plaintext, key):
    # Perform initial permutation (IP)
    plaintext = permute(plaintext, IP)
    
    # Generate keys K1 and K2
    K1, K2 = key_generation(key)
    
    # Apply the first round with K1
    temp = fk(plaintext, K1)
    
    # Swap the two halves
    temp = temp[4:] + temp[:4]
    
    # Apply the second round with K2
    temp = fk(temp, K2)
    
    # Perform inverse initial permutation (IP^-1)
    ciphertext = permute(temp, IP_inv)
    
    return ''.join(ciphertext)

# Function to perform the decryption
def decrypt(ciphertext, key):
    # Perform initial permutation (IP)
    ciphertext = permute(ciphertext, IP)
    
    # Generate keys K1 and K2
    K1, K2 = key_generation(key)
    
    # Apply the first round with K2 (inverse order)
    temp = fk(ciphertext, K2)
    
    # Swap the two halves
    temp = temp[4:] + temp[:4]
    
    # Apply the second round with K1
    temp = fk(temp, K1)
    
    # Perform inverse initial permutation (IP^-1)
    plaintext = permute(temp, IP_inv)
    
    return ''.join(plaintext)

# Main program with input/output
if __name__ == "__main__":
    # Input key and plaintext from user
    key = input("Enter a 10-bit key: ")
    plaintext = input("Enter an 8-bit plaintext: ")
    
    # Encrypt the plaintext
    ciphertext = encrypt(list(plaintext), list(key))
    print(f"Encrypted Ciphertext: {ciphertext}")
    
    # Decrypt the ciphertext
    decrypted_text = decrypt(list(ciphertext), list(key))
    print(f"Decrypted Plaintext: {decrypted_text}")
