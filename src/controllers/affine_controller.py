from flask import jsonify
from src.services.affine_service import encrypt_text, decrypt_text, crack_text

def encrypt(data):
    """
    Encrypts the given text using the Affine cipher with the provided parameters.

    Parameters (JSON payload):
    - inputText: str, the text to encrypt.
    - keyString: str, the key in the format "a,b".
    - alphabet: str, the alphabet to use for encryption.
    - cipher: str, should be 'affine' for Affine cipher.

    Returns:
    - JSON response with the encrypted text or an error message with a 400 status code.
    """
    input_text = data.get('inputText', '')
    key_string = data.get('keyString', '')
    alphabet = data.get('alphabet', '')
    cipher = data.get('cipher', '').lower()

    try:
        # Validate the cipher type
        if cipher != 'affine':
            raise ValueError("Invalid cipher type. Only 'affine' is supported.")
        if not alphabet:
            raise ValueError("Alphabet cannot be empty.")

        # Parse the key string
        a, b = map(int, key_string.split(','))
        encrypted_text = encrypt_text(input_text, a, b, alphabet)
        return jsonify({'encrypted_text': encrypted_text})
    except (ValueError, SyntaxError) as e:
        return jsonify({'error': f'Invalid input: {str(e)}'}), 400

def decrypt(data):
    """
    Decrypts the given text using the Affine cipher with the provided parameters.

    Parameters (JSON payload):
    - inputText: str, the text to decrypt.
    - keyString: str, the key in the format "a,b".
    - alphabet: str, the alphabet to use for decryption.
    - cipher: str, should be 'affine' for Affine cipher.

    Returns:
    - JSON response with the decrypted text or an error message with a 400 status code.
    """
    input_text = data.get('inputText', '')
    key_string = data.get('keyString', '')
    alphabet = data.get('alphabet', '')
    cipher = data.get('cipher', '').lower()

    try:
        # Validate the cipher type
        if cipher != 'affine':
            raise ValueError("Invalid cipher type. Only 'affine' is supported.")
        if not alphabet:
            raise ValueError("Alphabet cannot be empty.")

        # Parse the key string
        a, b = map(int, key_string.split(','))
        decrypted_text = decrypt_text(input_text, a, b, alphabet)
        return jsonify({'decrypted_text': decrypted_text})
    except (ValueError, SyntaxError) as e:
        return jsonify({'error': f'Invalid input: {str(e)}'}), 400


def crack(data):
    """
    Determines 'a' and 'b' values based on the two most frequent letters
    in the ciphertext, mapped to 'E' and 'T' in plaintext.

    Parameters (JSON payload):
    - inputText: str, the ciphertext (not directly used in this function).
    - keyString: str, the two most frequent letters in the ciphertext (e.g., "J,X").
    - alphabet: str, the custom alphabet to use.
    - cipher: str, should be 'affine'.

    Returns:
    - A string in the format "a=..., b=..." or an error message.
    """
    input_text = data.get('inputText', '')
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #alphabet = data.get('alphabet', '')

    if not input_text or not alphabet:
        return "Error: Missing required parameters: inputText or alphabet.", 400

    try:
        # Extract freq1 and freq2 from keyString
        freq1, freq2 = input_text.split(',')

        # Call the crack_text function
        a, b = crack_text(freq1, freq2, alphabet)

        # Return the result in the format expected by the frontend
        return jsonify({"encrypted_text": f"a={a}, b={b}"})
    except ValueError as e:
        return str(e), 400
    except Exception as e:
        return "An unexpected error occurred.", 500
