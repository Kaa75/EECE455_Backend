def encrypt_text(text, key, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """
    Encrypts text using a Vigenère cipher.

    Parameters:
    - text (str): The input text to encrypt.
    - key (str): The keyword used to generate shifts for encryption.
    - alphabet (str): The custom alphabet to use for encryption (default is "ABCDEFGHIJKLMNOPQRSTUVWXYZ").
    
    Returns:
    - str: The encrypted text, with each letter shifted according to the key.
    """
    if len(alphabet) != 26 or len(set(alphabet)) != 26:
        raise ValueError("Alphabet must be a permutation of 26 unique characters.")
    
    encrypted_text = []
    key = key.lower()
    key_index = 0
    key_length = len(key)
    alphabet = alphabet.upper()

    for char in text:
        if char.upper() in alphabet:  # Encrypt only characters in the alphabet
            shift = alphabet.index(key[key_index % key_length].upper())
            index = (alphabet.index(char.upper()) + shift) % len(alphabet)
            encrypted_char = alphabet[index]
            encrypted_text.append(encrypted_char if char.isupper() else encrypted_char.lower())
            key_index += 1
        else:
            encrypted_text.append(char)  # Non-alphabetic characters stay unchanged

    return ''.join(encrypted_text)


def decrypt_text(text, key,  alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """
    Decrypts text encrypted using a Vigenère cipher.

    Parameters:
    - text (str): The input text to decrypt.
    - key (str): The keyword used to generate shifts for decryption.

    Returns:
    - str: The decrypted text, with each letter reverted based on the key.
    """
    if len(alphabet) != 26 or len(set(alphabet)) != 26:
        raise ValueError("Alphabet must be a permutation of 26 unique characters.")

    decrypted_text = []
    key = key.lower()
    key_index = 0
    key_length = len(key)
    alphabet = alphabet.upper()

    for char in text:
        if char.upper() in alphabet:  # Decrypt only characters in the alphabet
            shift = alphabet.index(key[key_index % key_length].upper())
            index = (alphabet.index(char.upper()) - shift) % len(alphabet)
            decrypted_char = alphabet[index]
            decrypted_text.append(decrypted_char if char.isupper() else decrypted_char.lower())
            key_index += 1
        else:
            decrypted_text.append(char)  # Non-alphabetic characters stay unchanged

    return ''.join(decrypted_text)
