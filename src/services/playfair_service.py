import string

alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # I and J are combined when performing Playfair

def create_playfair_key_matrix(key):
    key = ''.join(sorted(set(key), key=key.index)).upper().replace('J', 'I')
    key_matrix = [c for c in key if c in alphabet]
    for letter in alphabet:
        if letter not in key_matrix:
            key_matrix.append(letter)
    return [key_matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(char, key_matrix):
    for row in range(5):
        for col in range(5):
            if key_matrix[row][col] == char:
                return row, col
    return None

def playfair_encryption(plaintext, key):
    key_matrix = create_playfair_key_matrix(key)
    plaintext = plaintext.upper().replace('J', 'I')
    plaintext_pairs = []
    
    i = 0
    while i < len(plaintext):
        char1 = plaintext[i]
        if not char1.isalpha():
            plaintext_pairs.append((char1,))
            i += 1
            continue

        char2 = plaintext[i + 1] if i + 1 < len(plaintext) and plaintext[i + 1].isalpha() else 'X'
        
        if char1 == char2:
            plaintext_pairs.append((char1, 'X'))
            i += 1
        else:
            plaintext_pairs.append((char1, char2))
            i += 2

    encrypted_text = []
    for pair in plaintext_pairs:
        if len(pair) == 1:
            encrypted_text.append(pair[0])
            continue
        
        char1, char2 = pair
        row1, col1 = find_position(char1, key_matrix)
        row2, col2 = find_position(char2, key_matrix)
        
        if row1 == row2:
            encrypted_text.append(key_matrix[row1][(col1 + 1) % 5])
            encrypted_text.append(key_matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:
            encrypted_text.append(key_matrix[(row1 + 1) % 5][col1])
            encrypted_text.append(key_matrix[(row2 + 1) % 5][col2])
        else:
            encrypted_text.append(key_matrix[row1][col2])
            encrypted_text.append(key_matrix[row2][col1])
    
    return ''.join(encrypted_text)

def playfair_decryption(ciphertext, key):
    key_matrix = create_playfair_key_matrix(key)
    ciphertext = ciphertext.upper().replace('J', 'I')
    decrypted_text = []

    i = 0
    while i < len(ciphertext):
        char1 = ciphertext[i]
        if not char1.isalpha():
            decrypted_text.append(char1)
            i += 1
            continue
        
        char2 = ciphertext[i + 1] if i + 1 < len(ciphertext) and ciphertext[i + 1].isalpha() else 'X'
        
        row1, col1 = find_position(char1, key_matrix)
        row2, col2 = find_position(char2, key_matrix)

        if row1 == row2:
            decrypted_text.append(key_matrix[row1][(col1 - 1) % 5])
            decrypted_text.append(key_matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:
            decrypted_text.append(key_matrix[(row1 - 1) % 5][col1])
            decrypted_text.append(key_matrix[(row2 - 1) % 5][col2])
        else:
            decrypted_text.append(key_matrix[row1][col2])
            decrypted_text.append(key_matrix[row2][col1])
        
        i += 2

    # Remove padding 'X' characters
    cleaned_text = []
    for i, char in enumerate(decrypted_text):
        if i < len(decrypted_text) - 1 and char == 'X' and decrypted_text[i - 1] == decrypted_text[i + 1]:
            continue  # Skip padding 'X'
        if i == len(decrypted_text) - 1 and char == 'X':
            continue  # Skip trailing 'X'
        cleaned_text.append(char)

    return ''.join(cleaned_text)
