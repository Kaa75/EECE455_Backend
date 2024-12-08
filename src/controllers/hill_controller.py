import sqlite3
import os
from flask import jsonify
from services.hill_service import encrypt_text, decrypt_text
import numpy as np


# Helper function to log data into the database
def log_hill_operation(operation, input_text, key_string, alphabet, result_text):
    try:
        # Connect to SQLite database
        current_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(current_dir, '../..', 'encryption_log.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Insert log into hill_log table
        cursor.execute('''
            INSERT INTO hill_log (operation, input_text, matrix, alphabet, output_text)
            VALUES (?, ?, ?, ?, ?)
        ''', (operation, input_text, key_string, alphabet, result_text))

        # Commit and close connection
        conn.commit()
        conn.close()

    except Exception as e:
        print(f"Error logging Hill operation: {e}")

def parse_key_string(key_string):
    """
    Converts a comma-separated key string into a numpy matrix.

    Parameters:
    - key_string: str, the key string in the format "1,2,3,4" for a 2x2 or 3x3 matrix.

    Returns:
    - numpy.ndarray: the parsed matrix.
    """
    try:
        key_values = list ( map ( int, key_string.split ( ',' ) ) )
        matrix_size = int ( len ( key_values ) ** 0.5 )
        if matrix_size ** 2 != len ( key_values ):
            raise ValueError ( "Key string must represent a square matrix." )
        return np.array ( key_values ).reshape ( matrix_size, matrix_size )
    except ValueError as e:
        raise ValueError ( f"Invalid key string format: {str ( e )}" )


def encrypt(data):
    """
    Encrypts the given text using the Hill cipher with the provided key matrix.

    Parameters (JSON payload):
    - inputText: str, the text to encrypt.
    - keyString: str, the key string in the format "1,2,3,4".
    - alphabet: str, the alphabet to use for encryption.
    - cipher: str, the cipher type, expected to be 'hill'.

    Returns:
    - JSON response with:
        - encrypted_text: str, the encrypted text.
    """
    input_text = data.get ( 'inputText', '' )
    key_string = data.get ( 'keyString', '' )
    alphabet = data.get ( 'alphabet', '' )
    cipher = data.get ( 'cipher', '' ).lower ()

    try:
        if cipher != 'hill':
            raise ValueError ( "Invalid cipher type. Only 'hill' is supported." )
        if not alphabet:
            raise ValueError ( "Alphabet cannot be empty." )

        # Parse the key string into a matrix
        key_matrix = parse_key_string ( key_string )
        encrypted_text = encrypt_text ( input_text, key_matrix, alphabet )

        log_hill_operation('encrypt', input_text, key_string, alphabet, encrypted_text)

        return jsonify ( {'encrypted_text': encrypted_text} )
    except ValueError as e:
        return jsonify ( {'error': str ( e )} ), 400


def decrypt(data):
    """
    Decrypts the given text using the Hill cipher with the provided key matrix.

    Parameters (JSON payload):
    - inputText: str, the text to decrypt.
    - keyString: str, the key string in the format "1,2,3,4".
    - alphabet: str, the alphabet to use for decryption.
    - cipher: str, the cipher type, expected to be 'hill'.

    Returns:
    - JSON response with:
        - decrypted_text: str, the decrypted text.
    """
    input_text = data.get ( 'inputText', '' )
    key_string = data.get ( 'keyString', '' )
    alphabet = data.get ( 'alphabet', '' )
    cipher = data.get ( 'cipher', '' ).lower ()

    try:
        if cipher != 'hill':
            raise ValueError ( "Invalid cipher type. Only 'hill' is supported." )
        if not alphabet:
            raise ValueError ( "Alphabet cannot be empty." )

        # Parse the key string into a matrix
        key_matrix = parse_key_string ( key_string )
        decrypted_text, _ = decrypt_text ( input_text, key_matrix, alphabet )

        log_hill_operation('decrypt', input_text, key_string, alphabet, decrypted_text)

        return jsonify ( {'decrypted_text': decrypted_text} )
    except ValueError as e:
        return jsonify ( {'error': str ( e )} ), 400
