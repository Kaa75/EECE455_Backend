def encrypt_text(text, key):
    """
    Encrypts text using a mono-alphabetic substitution cipher.

    Parameters:
    - text (str): The input text to encrypt.
    - key (str): A 26-character string representing the substitution key.

    Returns:
    - str: The encrypted text, with each letter substituted according to the key.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_map = {alphabet[i]: key[i].lower() for i in range(26)}
    return ''.join(key_map.get(char, char) for char in text.lower())

def decrypt_text(text, key):
    """
    Decrypts text encrypted using a mono-alphabetic substitution cipher.

    Parameters:
    - text (str): The input text to decrypt.
    - key (str): A 26-character string representing the substitution key.

    Returns:
    - str: The decrypted text, with each letter reverted to its original form based on the key.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_map = {key[i].lower(): alphabet[i] for i in range(26)}
    return ''.join(key_map.get(char, char) for char in text.lower())
