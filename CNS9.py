# S-box for SubBytes step
SBOX = [
    0x9, 0x4, 0xA, 0xB,
    0xD, 0x1, 0x8, 0x5,
    0x6, 0x2, 0x0, 0x3,
    0xC, 0xE, 0xF, 0x7
]

# Inverse S-box for InvSubBytes step
INV_SBOX = [
    0xA, 0x5, 0x9, 0xB,
    0x1, 0x7, 0x8, 0xF,
    0x6, 0x0, 0x2, 0x3,
    0xC, 0x4, 0xD, 0xE
]

# Round constants for key expansion
RCON = [0x80, 0x30]

# Function to substitute nibbles using S-box
def sub_nibble(nibble):
    # Ensure nibble is in the range 0 to 15
    nibble = nibble & 0xF
    return (SBOX[nibble >> 4] << 4) | SBOX[nibble & 0xF]

# Function to inverse substitute nibbles using inverse S-box
def inv_sub_nibble(nibble):
    # Ensure nibble is in the range 0 to 15
    nibble = nibble & 0xF
    return (INV_SBOX[nibble >> 4] << 4) | INV_SBOX[nibble & 0xF]

# Function to perform nibble substitution for 2-byte values
def sub_word(word):
    return (SBOX[word >> 4] << 4) | SBOX[word & 0xF]

# Function to generate round keys
def key_expansion(key):
    # Initial round key (w0 and w1)
    w = [key >> 8, key & 0xFF]

    for i in range(2):
        # Apply key schedule core
        temp = sub_word(w[i + 1]) ^ RCON[i]
        w.append(w[i] ^ temp)

    return w

# Function to perform the ShiftRow step
def shift_row(nibble):
    return ((nibble & 0xF0) | ((nibble & 0x0F) >> 1) | ((nibble & 0x01) << 3))

# Function to mix columns in the MixColumn step
def mix_column(nibble):
    return (nibble << 1) & 0xFF

# Function to add round keys (AddRoundKey)
def add_round_key(state, key):
    return state ^ key

# Function to encrypt plaintext using S-AES
def encrypt(plaintext, key):
    # Key expansion
    keys = key_expansion(key)

    # Initial AddRoundKey
    state = add_round_key(plaintext, keys[0])

    # First round
    state = sub_nibble(state)
    state = shift_row(state)
    state = mix_column(state)
    state = add_round_key(state, keys[1])

    # Second (Final) round
    state = sub_nibble(state)
    state = shift_row(state)
    state = add_round_key(state, keys[2])

    return state

# Function to decrypt ciphertext using S-AES
def decrypt(ciphertext, key):
    # Key expansion
    keys = key_expansion(key)

    # Initial AddRoundKey (inverse final round)
    state = add_round_key(ciphertext, keys[2])

    # Inverse final round
    state = shift_row(state)  # ShiftRow is its own inverse
    state = inv_sub_nibble(state)
    state = add_round_key(state, keys[1])

    # Inverse first round
    state = mix_column(state)  # Inverse MixColumn step (identity in simplified AES)
    state = shift_row(state)  # ShiftRow is its own inverse
    state = inv_sub_nibble(state)
    state = add_round_key(state, keys[0])

    return state

# Main program with input/output
if __name__ == "__main__":
    # Take 16-bit key and plaintext input from the user
    plaintext = int(input("Enter the 16-bit plaintext (in hex, e.g., 0x1234): "), 16)
    key = int(input("Enter the 16-bit key (in hex, e.g., 0x5678): "), 16)

    # Encrypt the plaintext
    ciphertext = encrypt(plaintext, key)
    print(f"Encrypted Ciphertext: {hex(ciphertext)}")

    # Decrypt the ciphertext
    decrypted_plaintext = decrypt(ciphertext, key)
    print(f"Decrypted Plaintext: {hex(decrypted_plaintext)}")
