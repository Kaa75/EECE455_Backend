import sqlite3
import os
from flask import jsonify
from services.mono_alphabetic_service import encrypt_text, decrypt_text


# Helper function to log data into the database
def log_mono_alphabetic_operation(operation, input_text, key, result_text):
    try:
        # Connect to SQLite database
        current_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(current_dir, '../..', 'encryption_log.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Insert log into mono_alphabetic_log table
        cursor.execute('''
            INSERT INTO mono_alphabetic_log (operation, input_text, key, output_text)
            VALUES (?, ?, ?, ?)
        ''', (operation, input_text, key, result_text))

        # Commit and close connection
        conn.commit()
        conn.close()

    except Exception as e:
        print(f"Error logging Mono-Alphabetic operation: {e}")

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

    log_mono_alphabetic_operation('encrypt', text, key, encrypted_text)

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

    log_mono_alphabetic_operation('decrypt', text, key, decrypted_text)

    return jsonify({'decrypted_text': decrypted_text})