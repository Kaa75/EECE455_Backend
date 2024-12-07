import string

# Constants and character mapping
ALPHABET = string.ascii_uppercase
ALPHABET_DICT = {char: idx for idx, char in enumerate(ALPHABET)}
REVERSE_ALPHABET_DICT = {idx: char for idx, char in enumerate(ALPHABET)}
MOD = 26  # Length of the alphabet

def mod_inverse(a, mod=MOD):
    """
    Find the modular inverse of 'a' under modulo 'mod'.
    Raises ValueError if 'a' has no inverse under modulo 'mod'.

    Parameters:
    - a: int, the integer to find the modular inverse of.
    - mod: int, the modulus (default is 26).

    Returns:
    - int, the modular inverse of 'a' under modulo 'mod'.
    """
    for x in range(1, mod):
        if (a * x) % mod == 1:
            return x
    raise ValueError(f"No modular inverse for a={a} under modulo {mod}.")

def process_text(text):
    """
    Process the text to retain only alphabetic characters and convert them to uppercase.

    Parameters:
    - text: str, the text to process.

    Returns:
    - str, the processed text containing only uppercase alphabetic characters.
    """
    return ''.join([char for char in text if char.isalpha()]).upper()

def affine_encrypt_char(char, a, b):
    """
    Encrypt a single character using the Affine cipher formula: E(x) = (a * x + b) % MOD.

    Parameters:
    - char: str, the character to encrypt.
    - a: int, the multiplier in the Affine cipher.
    - b: int, the shift in the Affine cipher.

    Returns:
    - str, the encrypted character.
    """
    x = ALPHABET_DICT[char]
    return REVERSE_ALPHABET_DICT[(a * x + b) % MOD]

def affine_decrypt_char(char, a, b):
    """
    Decrypt a single character using the Affine cipher formula: D(x) = a_inv * (x - b) % MOD.

    Parameters:
    - char: str, the character to decrypt.
    - a: int, the multiplier in the Affine cipher.
    - b: int, the shift in the Affine cipher.

    Returns:
    - str, the decrypted character.
    """
    x = ALPHABET_DICT[char]
    a_inv = mod_inverse(a, MOD)
    return REVERSE_ALPHABET_DICT[(a_inv * (x - b)) % MOD]

def encrypt_text(text, a, b):
    """
    Encrypt the entire text using the Affine cipher, preserving non-alphabet characters.

    Parameters:
    - text: str, the plaintext to encrypt.
    - a: int, the multiplier in the Affine cipher.
    - b: int, the shift in the Affine cipher.

    Returns:
    - str, the encrypted text with non-alphabet characters retained.
    """
    try:
        mod_inverse(a, MOD)
    except ValueError:
        raise ValueError("Invalid 'a' value. 'a' must be coprime with 26.")

    processed_text = process_text(text)
    encrypted_text = ''.join(affine_encrypt_char(char, a, b) for char in processed_text)

    # Reinsert non-alphabet characters at their original positions
    full_result = []
    j = 0
    for char in text:
        if char.upper() in ALPHABET:
            full_result.append(encrypted_text[j])
            j += 1
        else:
            full_result.append(char)
    return ''.join(full_result).strip()

def decrypt_text(text, a, b):
    """
    Decrypt the entire text using the Affine cipher, preserving non-alphabet characters.

    Parameters:
    - text: str, the ciphertext to decrypt.
    - a: int, the multiplier in the Affine cipher.
    - b: int, the shift in the Affine cipher.

    Returns:
    - str, the decrypted text with non-alphabet characters retained.
    """
    try:
        mod_inverse(a, MOD)
    except ValueError:
        raise ValueError("Invalid 'a' value. 'a' must be coprime with 26.")

    processed_text = process_text(text)
    decrypted_text = ''.join(affine_decrypt_char(char, a, b) for char in processed_text)

    # Reinsert non-alphabet characters at their original positions
    full_result = []
    j = 0
    for char in text:
        if char.upper() in ALPHABET:
            full_result.append(decrypted_text[j])
            j += 1
        else:
            full_result.append(char)
    return ''.join(full_result).strip()

def crack_text(freq1, freq2):
    """
    Determine 'a' and 'b' for the Affine cipher by using the two most frequent letters in the ciphertext,
    which correspond to 'E' and 'T' in plaintext.

    Parameters:
    - freq1: str, the most frequent letter in the ciphertext (mapped to 'E').
    - freq2: str, the second most frequent letter in the ciphertext (mapped to 'T').

    Returns:
    - tuple: (a, b) if cracking is successful; raises ValueError otherwise.
    """
    X1, X2 = ALPHABET_DICT['E'], ALPHABET_DICT['T']
    Y1, Y2 = ALPHABET_DICT[freq1.upper()], ALPHABET_DICT[freq2.upper()]

    # Calculate 'a' by solving (Y2 - Y1) * a ≡ (X2 - X1) mod 26
    delta_y = (Y2 - Y1) % MOD
    delta_x = (X2 - X1) % MOD

    try:
        a = (delta_y * mod_inverse(delta_x, MOD)) % MOD
    except ValueError:
        raise ValueError("Unable to solve for 'a' and 'b'. Ensure inputs are correct.")

    # Calculate 'b' using b ≡ Y1 - a * X1 mod 26
    b = (Y1 - a * X1) % MOD

    return a, b
