import sqlite3
import os
from flask import jsonify
from services.vigenere_service import encrypt_text, decrypt_text

# Helper function to log Vigenère operations
def log_vigenere_operation(operation, input_text, key, result_text, alphabet):
    try:
        # Connect to SQLite database
        current_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(current_dir, '../..', 'encryption_log.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Insert log into vigenere_log table
        cursor.execute('''
            INSERT INTO vigenere_log (operation, input_text, key, output_text, alphabet)
            VALUES (?, ?, ?, ?, ?)
        ''', (operation, input_text, key, result_text, alphabet))

        # Commit and close connection
        conn.commit()
        conn.close()

    except Exception as e:
        print(f"Error logging Vigenère operation: {e}")

def encrypt(request):
    """
    Encrypts text using a Vigenère cipher.

    Parameters:
    - text (str): Text to encrypt, provided in the request arguments.
    - key (str): Keyword for encryption, provided in the request arguments.
    - cipher (str): Cipher type, expected to be 'vigenere', provided in the request arguments.
    - alphabet (str): Custom alphabet (optional), provided in the request arguments.

    Returns:
    - JSON response containing:
        - 'encrypted_text' (str): The encrypted version of the input text.
      In case of errors, returns a JSON response with an error message and status code 400.
    """
    text = request.get('inputText', '')
    key = request.get('keyString', '')
    cipher = request.get('cipher', '').lower()
    alphabet = request.get('alphabet', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')  # Default alphabet

    if cipher != 'vigenere':
        return jsonify({'error': 'Invalid cipher type. Use "cipher=vigenere".'}), 400

    if not key.isalpha():
        return jsonify({'error': 'Key must be an alphabetic string.'}), 400

    if len(alphabet) != 26 or len(set(alphabet)) != 26:
        return jsonify({'error': 'Alphabet must be a permutation of 26 unique characters.'}), 400

    encrypted_text = encrypt_text(text, key, alphabet)

    log_vigenere_operation('encrypt', text, key, encrypted_text, alphabet)

    return jsonify({'encrypted_text': encrypted_text})

def decrypt(request):
    """
    Decrypts text encrypted with a Vigenère cipher.

    Parameters:
    - text (str): Encrypted text to decrypt, provided in the request arguments.
    - key (str): Keyword for decryption, provided in the request arguments.
    - cipher (str): Cipher type, expected to be 'vigenere', provided in the request arguments.
    - alphabet (str): Custom alphabet (optional), provided in the request arguments.

    Returns:
    - JSON response containing:
        - 'decrypted_text' (str): The decrypted version of the input text.
      In case of errors, returns a JSON response with an error message and status code 400.
    """
    text = request.get('inputText', '')
    key = request.get('keyString', '')
    cipher = request.get('cipher', '').lower()
    alphabet = request.get('alphabet', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')  # Default alphabet

    if cipher != 'vigenere':
        return jsonify({'error': 'Invalid cipher type. Use "cipher=vigenere".'}), 400

    if not key.isalpha():
        return jsonify({'error': 'Key must be an alphabetic string.'}), 400

    if len(alphabet) != 26 or len(set(alphabet)) != 26:
        return jsonify({'error': 'Alphabet must be a permutation of 26 unique characters.'}), 400
    
    decrypted_text = decrypt_text(text, key, alphabet)

    log_vigenere_operation('decrypt', text, key, decrypted_text, alphabet)

    return jsonify({'decrypted_text': decrypted_text})
