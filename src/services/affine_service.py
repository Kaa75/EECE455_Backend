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
    """
    for x in range(1, mod):
        if (a * x) % mod == 1:
            return x
    raise ValueError(f"No modular inverse for a={a} under modulo {mod}.")

def process_text(text):
    """
    Process the text to retain only alphabetic characters and convert them to uppercase.
    """
    return ''.join([char for char in text if char.isalpha()]).upper()

def affine_encrypt_char(char, a, b):
    """
    Encrypt a single character using the Affine cipher formula: E(x) = (a * x + b) % MOD
    """
    x = ALPHABET_DICT[char]
    return REVERSE_ALPHABET_DICT[(a * x + b) % MOD]

def affine_decrypt_char(char, a, b):
    """
    Decrypt a single character using the Affine cipher formula: D(x) = a_inv * (x - b) % MOD
    """
    x = ALPHABET_DICT[char]
    a_inv = mod_inverse(a, MOD)
    return REVERSE_ALPHABET_DICT[(a_inv * (x - b)) % MOD]

def encrypt_text(text, a, b):
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


