from flask import request, jsonify
from src.services.euclid_service import modular_inverse, format_table

def encrypt_route():
    """
    Calculates the modular inverse of a given number using the Euclidean algorithm.

    Parameters:
    - a (int): The number to find the inverse of, provided in the request arguments.
    - mod (int): The modulus under which to calculate the inverse, provided in the request arguments.
    - cipher (str): Cipher type, expected to be 'euclid', provided in the request arguments.

    Returns:
    - JSON response containing:
        - 'inverse' (int): The modular inverse if it exists.
        - 'table' (str): A formatted string representing each step in the Euclidean algorithm.
      If an inverse does not exist, returns an error message and status code 400.
    """
    a = request.args.get('a', type=int)
    mod = request.args.get('mod', type=int)
    cipher = request.args.get('cipher', '').lower()

    if cipher != 'euclid':
        return jsonify({'error': 'Invalid cipher type. Use "cipher=euclid".'}), 400

    inverse, table = modular_inverse(a, mod)
    if inverse is None:
        return jsonify({'error': f'No modular inverse for {a} mod {mod}', 'table': format_table(table)}), 400

    return jsonify({'inverse': inverse, 'table': format_table(table)})

def decrypt_route():
    """
    Returns an error response indicating that decryption is unsupported for the Euclidean cipher.

    Parameters:
    - None

    Returns:
    - JSON response with an error message and status code 400.
    """
    # Euclidean does not support direct decryption
    return jsonify({'error': 'Decrypt not supported for Euclidean cipher.'}), 400
