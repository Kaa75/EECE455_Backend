def mod_inverse(a, mod):
    """
    Find the modular inverse of 'a' under modulo 'mod'.
    Raises ValueError if 'a' has no inverse under modulo 'mod'.

    Parameters:
    - a: int, the integer to find the modular inverse of.
    - mod: int, the modulus.

    Returns:
    - int, the modular inverse of 'a' under modulo 'mod'.
    """
    for x in range(1, mod):
        if (a * x) % mod == 1:
            return x
    raise ValueError(f"No modular inverse for a={a} under modulo {mod}.")

def process_text(text, alphabet):
    """
    Process the text to retain only characters from the alphabet and convert them to uppercase.

    Parameters:
    - text: str, the text to process.
    - alphabet: str, the custom alphabet to filter against.

    Returns:
    - str, the processed text containing only characters from the alphabet.
    """
    return ''.join([char for char in text.upper() if char in alphabet])

def affine_encrypt_char(char, a, b, alphabet, mod):
    """
    Encrypt a single character using the Affine cipher formula.

    Parameters:
    - char: str, the character to encrypt.
    - a: int, the multiplier in the Affine cipher.
    - b: int, the shift in the Affine cipher.
    - alphabet: str, the custom alphabet to use.
    - mod: int, the length of the alphabet.

    Returns:
    - str, the encrypted character.
    """
    index = alphabet.index(char)
    return alphabet[(a * index + b) % mod]

def affine_decrypt_char(char, a, b, alphabet, mod):
    """
    Decrypt a single character using the Affine cipher formula.

    Parameters:
    - char: str, the character to decrypt.
    - a: int, the multiplier in the Affine cipher.
    - b: int, the shift in the Affine cipher.
    - alphabet: str, the custom alphabet to use.
    - mod: int, the length of the alphabet.

    Returns:
    - str, the decrypted character.
    """
    index = alphabet.index(char)
    a_inv = mod_inverse(a, mod)
    return alphabet[(a_inv * (index - b)) % mod]

def encrypt_text(text, a, b, alphabet):
    """
    Encrypt the entire text using the Affine cipher, preserving non-alphabet characters.

    Parameters:
    - text: str, the plaintext to encrypt.
    - a: int, the multiplier in the Affine cipher.
    - b: int, the shift in the Affine cipher.
    - alphabet: str, the custom alphabet to use.

    Returns:
    - str, the encrypted text with non-alphabet characters retained.
    """
    mod = len(alphabet)
    # Validate 'a' is coprime with mod
    try:
        mod_inverse (a, mod)
    except ValueError:
        raise ValueError ( f"Invalid 'a' value: {a} must be coprime with the length of the alphabet ({mod})." )
    processed_text = process_text(text, alphabet)
    encrypted_text = ''.join(affine_encrypt_char(char, a, b, alphabet, mod) for char in processed_text)

    full_result = []
    j = 0
    for char in text:
        if char.upper() in alphabet:
            full_result.append(encrypted_text[j])
            j += 1
        else:
            full_result.append(char)
    return ''.join(full_result).strip()

def decrypt_text(text, a, b, alphabet):
    """
    Decrypt the entire text using the Affine cipher, preserving non-alphabet characters.

    Parameters:
    - text: str, the ciphertext to decrypt.
    - a: int, the multiplier in the Affine cipher.
    - b: int, the shift in the Affine cipher.
    - alphabet: str, the custom alphabet to use.

    Returns:
    - str, the decrypted text with non-alphabet characters retained.
    """
    mod = len(alphabet)
    # Validate 'a' is coprime with mod
    try:
        mod_inverse ( a, mod )
    except ValueError:
        raise ValueError ( f"Invalid 'a' value: {a} must be coprime with the length of the alphabet ({mod})." )
    processed_text = process_text(text, alphabet)
    decrypted_text = ''.join(affine_decrypt_char(char, a, b, alphabet, mod) for char in processed_text)

    full_result = []
    j = 0
    for char in text:
        if char.upper() in alphabet:
            full_result.append(decrypted_text[j])
            j += 1
        else:
            full_result.append(char)
    return ''.join(full_result).strip()


def crack_text(freq1, freq2, alphabet):
    """
    Determine 'a' and 'b' for the Affine cipher by using the two most frequent letters in the ciphertext,
    mapped to the two most common letters in the plaintext ('E' and 'T').

    Parameters:
    - freq1: str, the most frequent letter in the ciphertext (mapped to 'E').
    - freq2: str, the second most frequent letter in the ciphertext (mapped to 'T').
    - alphabet: str, the custom alphabet to use.

    Returns:
    - tuple: (a, b) if cracking is successful; raises ValueError otherwise.
    """
    mod = len (alphabet)
    alphabet_dict = {char: idx for idx, char in enumerate (alphabet)}

    try:
        X1, X2 = alphabet_dict['E'], alphabet_dict['T']  # Plaintext letters
        Y1, Y2 = alphabet_dict[freq1.upper()], alphabet_dict[freq2.upper()]  # Ciphertext letters
    except KeyError:
        raise ValueError("One or more letters not found in the provided alphabet.")

    # Calculate 'a' by solving (Y2 - Y1) * a ≡ (X2 - X1) mod len(alphabet)
    delta_y = (Y2 - Y1) % mod
    delta_x = (X2 - X1) % mod

    try:
        a = (delta_y * mod_inverse ( delta_x, mod )) % mod
    except ValueError:
        raise ValueError ( "Unable to solve for 'a'. Ensure inputs and the alphabet are correct." )

    # Calculate 'b' using b ≡ Y1 - a * X1 mod len(alphabet)
    b = (Y1 - a * X1) % mod

    return a, b
