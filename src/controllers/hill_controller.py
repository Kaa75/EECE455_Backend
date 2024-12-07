from flask import request, jsonify
from services.hill_service import encrypt_text, decrypt_text, mod_inverse_matrix
import numpy as np

def format_matrix(matrix):
    """
    Format a matrix as a regular Python-style list without extra spaces or line breaks.

    Parameters:
    - matrix: numpy.ndarray or list, the matrix to be formatted as a string.

    Returns:
    - str: the matrix in a formatted string as a Python list.
    """
    if isinstance(matrix, np.ndarray):
        matrix = matrix.tolist()
    return str(matrix)

def encrypt_route():
    """
    Encrypts the given text using the Hill cipher with the provided key matrix.

    Parameters:
    - text: str, the text to encrypt, obtained from request arguments.
    - key: str, the key matrix in list format, obtained from request arguments.
    - cipher: str, the cipher type, expected to be 'hill', obtained from request arguments.

    Returns:
    - JSON response with:
        - matrix: str, the key matrix formatted as a string.
        - encrypted_text: str, the encrypted text.
      If there are errors, returns a JSON response with an error message and a 400 status code.
    """
    text = request.args.get('text', '')
    key = request.args.get('key', '')



    try:
        key_matrix = np.array(eval(key))  # Safe only with controlled input
    except:
        return jsonify({'error': 'Invalid key format. Provide a valid 2x2 or 3x3 matrix in list format.'}), 400

    if key_matrix.shape[0] != key_matrix.shape[1] or key_matrix.shape[0] not in [2, 3]:
        return jsonify({'error': 'Matrix must be 2x2 or 3x3.'}), 400

    try:
        encrypted_text = encrypt_text(text, key_matrix)
        return jsonify({
            'matrix': format_matrix(key_matrix),
            'encrypted_text': encrypted_text
        })
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

def decrypt_route():
    """
    Decrypts the given text using the Hill cipher with the provided key matrix and finds the inverse matrix.

    Parameters:
    - text: str, the text to decrypt, obtained from request arguments.
    - key: str, the key matrix in list format, obtained from request arguments.
    - cipher: str, the cipher type, expected to be 'hill', obtained from request arguments.

    Returns:
    - JSON response with:
        - matrix: str, the key matrix formatted as a string.
        - inverse_matrix: str, the inverse of the key matrix formatted as a string.
        - decrypted_text: str, the decrypted text.
      If there are errors, returns a JSON response with an error message and a 400 status code.
    """
    text = request.args.get('text', '')
    key = request.args.get('key', '')



    try:
        key_matrix = np.array(eval(key))  # Safe only with controlled input
    except:
        return jsonify({'error': 'Invalid key format. Provide a valid 2x2 or 3x3 matrix in list format.'}), 400

    if key_matrix.shape[0] != key_matrix.shape[1] or key_matrix.shape[0] not in [2, 3]:
        return jsonify({'error': 'Matrix must be 2x2 or 3x3.'}), 400

    try:
        decrypted_text, inverse_matrix = decrypt_text(text, key_matrix)
        return jsonify({
            'matrix': format_matrix(key_matrix),
            'inverse_matrix': format_matrix(inverse_matrix),
            'decrypted_text': decrypted_text
        })
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
