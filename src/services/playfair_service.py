import string

alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # I and J are typically combined for Playfair

def create_playfair_key_matrix(key):
    # Remove duplicates and prepare the key matrix
    key = ''.join(sorted(set(key), key=key.index)).upper().replace('J', 'I')
    key_matrix = [c for c in key if c in alphabet]
    for letter in alphabet:
        if letter not in key_matrix:
            key_matrix.append(letter)
    return [key_matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(char, key_matrix):
    # Find position of a character in the key matrix
    for row in range(5):
        for col in range(5):
            if key_matrix[row][col] == char:
                return row, col
    return None

def playfair_encryption(plaintext, key):
    key_matrix = create_playfair_key_matrix(key)
    plaintext = plaintext.upper().replace('J', 'I')
    plaintext_pairs = []
    
    # Prepare plaintext pairs
    i = 0
    while i < len(plaintext):
        char1 = plaintext[i]
        char2 = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'
        
        # Handle duplicate letters in pair
        if char1 == char2:
            plaintext_pairs.append((char1, 'X'))
            i += 1
        else:
            plaintext_pairs.append((char1, char2))
            i += 2
    
    # Encrypt pairs
    encrypted_text = []
    for char1, char2 in plaintext_pairs:
        row1, col1 = find_position(char1, key_matrix)
        row2, col2 = find_position(char2, key_matrix)
        
        if row1 == row2:  # Same row
            encrypted_text.append(key_matrix[row1][(col1 + 1) % 5])
            encrypted_text.append(key_matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:  # Same column
            encrypted_text.append(key_matrix[(row1 + 1) % 5][col1])
            encrypted_text.append(key_matrix[(row2 + 1) % 5][col2])
        else:  # Rectangle swap
            encrypted_text.append(key_matrix[row1][col2])
            encrypted_text.append(key_matrix[row2][col1])
    
    return ''.join(encrypted_text)

def playfair_decryption(ciphertext, key):
    key_matrix = create_playfair_key_matrix(key)
    ciphertext = ciphertext.upper().replace('J', 'I')
    decrypted_text = []

    for i in range(0, len(ciphertext), 2):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1]
        row1, col1 = find_position(char1, key_matrix)
        row2, col2 = find_position(char2, key_matrix)
        
        if row1 == row2:  # Same row
            decrypted_text.append(key_matrix[row1][(col1 - 1) % 5])
            decrypted_text.append(key_matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:  # Same column
            decrypted_text.append(key_matrix[(row1 - 1) % 5][col1])
            decrypted_text.append(key_matrix[(row2 - 1) % 5][col2])
        else:  # Rectangle swap
            decrypted_text.append(key_matrix[row1][col2])
            decrypted_text.append(key_matrix[row2][col1])
    
    # Remove extra 'X's if they were added during encryption
    return ''.join(decrypted_text).replace('X', '')
