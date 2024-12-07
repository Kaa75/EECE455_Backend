from flask import jsonify
from services.vigenere_service import encrypt_text, decrypt_text

def encrypt(request):
    """
    Encrypts text using a Vigenère cipher.

    Parameters:
    - text (str): Text to encrypt, provided in the request arguments.
    - key (str): Keyword for encryption, provided in the request arguments.
    - cipher (str): Cipher type, expected to be 'vigenere', provided in the request arguments.

    Returns:
    - JSON response containing:
        - 'encrypted_text' (str): The encrypted version of the input text.
      In case of errors, returns a JSON response with an error message and status code 400.
    """
    text = request.get('inputText', '')
    key = request.get('keyString', '')
    cipher = request.get('cipher', '').lower()

    if cipher != 'vigenere':
        return jsonify({'error': 'Invalid cipher type. Use "cipher=vigenere".'}), 400

    if not key.isalpha():
        return jsonify({'error': 'Key must be an alphabetic string.'}), 400

    encrypted_text = encrypt_text(text, key)
    return jsonify({'encrypted_text': encrypted_text})

def decrypt(request):
    """
    Decrypts text encrypted with a Vigenère cipher.

    Parameters:
    - text (str): Encrypted text to decrypt, provided in the request arguments.
    - key (str): Keyword for decryption, provided in the request arguments.
    - cipher (str): Cipher type, expected to be 'vigenere', provided in the request arguments.

    Returns:
    - JSON response containing:
        - 'decrypted_text' (str): The decrypted version of the input text.
      In case of errors, returns a JSON response with an error message and status code 400.
    """
    text = request.get('inputText', '')
    key = request.get('keyString', '')
    cipher = request.get('cipher', '').lower()

    if cipher != 'vigenere':
        return jsonify({'error': 'Invalid cipher type. Use "cipher=vigenere".'}), 400

    if not key.isalpha():
        return jsonify({'error': 'Key must be an alphabetic string.'}), 400

    decrypted_text = decrypt_text(text, key)
    return jsonify({'decrypted_text': decrypted_text})
