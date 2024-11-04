from flask import jsonify
from services.mono_alphabetic_service import encrypt_text, decrypt_text

def encrypt(request):
    """
    Encrypts text using a mono-alphabetic cipher.

    Parameters:
    - text (str): Text to encrypt, provided in the request arguments.
    - key (str): 26-character substitution key for encryption, provided in the request arguments.
    - cipher (str): Cipher type, expected to be 'mono_alphabetic', provided in the request arguments.

    Returns:
    - JSON response containing:
        - 'encrypted_text' (str): The encrypted version of the input text.
      In case of errors, returns a JSON response with an error message and status code 400.
    """
    text = request.get('inputText', '')
    key = request.get('keyString', '')
    cipher = request.get('cipher', '').lower()


    if cipher != 'mono_alphabetic':
        return jsonify({'error': 'Invalid cipher type. Use "cipher=mono_alphabetic".'}), 400

    if len(key) != 26 or not key.isalpha():
        return jsonify({'error': 'Key must be a 26-character alphabetic string.'}), 400

    encrypted_text = encrypt_text(text, key)
    return jsonify({'encrypted_text': encrypted_text})

def decrypt(request):
    """
    Decrypts text encrypted with a mono-alphabetic cipher.

    Parameters:
    - text (str): Encrypted text to decrypt, provided in the request arguments.
    - key (str): 26-character substitution key for decryption, provided in the request arguments.
    - cipher (str): Cipher type, expected to be 'mono_alphabetic', provided in the request arguments.

    Returns:
    - JSON response containing:
        - 'decrypted_text' (str): The decrypted version of the input text.
      In case of errors, returns a JSON response with an error message and status code 400.
    """
    text = request.get('inputText', '')
    key = request.get('keyString', '')
    cipher = request.get('cipher', '').lower()

    if cipher != 'mono_alphabetic':
        return jsonify({'error': 'Invalid cipher type. Use "cipher=mono_alphabetic".'}), 400

    if len(key) != 26 or not key.isalpha():
        return jsonify({'error': 'Key must be a 26-character alphabetic string.'}), 400

    decrypted_text = decrypt_text(text, key)
    return jsonify({'decrypted_text': decrypted_text})