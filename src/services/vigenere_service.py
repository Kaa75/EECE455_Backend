def encrypt_text(text, key):
    """
    Encrypts text using a Vigenère cipher.

    Parameters:
    - text (str): The input text to encrypt.
    - key (str): The keyword used to generate shifts for encryption.

    Returns:
    - str: The encrypted text, with each letter shifted according to the key.
    """
    encrypted_text = []
    key = key.lower()
    key_index = 0
    key_length = len(key)

    for char in text:
        if char.isalpha():  # Encrypt only alphabetic characters
            shift = ord(key[key_index % key_length]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1  
        else:
            encrypted_text.append(char)  # Non-alphabetic characters stay unchanged

    return ''.join(encrypted_text)


def decrypt_text(text, key):
    """
    Decrypts text encrypted using a Vigenère cipher.

    Parameters:
    - text (str): The input text to decrypt.
    - key (str): The keyword used to generate shifts for decryption.

    Returns:
    - str: The decrypted text, with each letter reverted based on the key.
    """
    decrypted_text = []
    key = key.lower()
    key_index = 0
    key_length = len(key)

    for char in text:
        if char.isalpha():  # Decrypt only alphabetic characters
            shift = ord(key[key_index % key_length]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            decrypted_text.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1  
        else:
            decrypted_text.append(char)  # Non-alphabetic characters stay unchanged

    return ''.join(decrypted_text)
