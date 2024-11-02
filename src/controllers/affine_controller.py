from flask import request, jsonify
from src.services.affine_service import encrypt_text, decrypt_text

def encrypt_route():
    """
    Encrypts the given text using the Affine cipher with the provided 'a' and 'b' values.

    Parameters:
    - text: str, the text to encrypt.
    - key: str, the key in the format "[a,b]", obtained from request arguments.
    - cipher: str, should be 'affine' for Affine cipher, obtained from request arguments.

    Returns:
    - JSON response with the encrypted text or an error message with a 400 status code.
    """
    text = request.args.get('text', '')
    key = request.args.get('key', '')
    cipher = request.args.get('cipher', '').lower()

    if cipher != 'affine':
        return jsonify({'error': 'Invalid cipher type. Use "cipher=affine".'}), 400

    try:
        # Parse 'key' as [a, b] for Affine cipher
        a, b = eval(key)
        encrypted_text = encrypt_text(text, a, b)
        return jsonify({'encrypted_text': encrypted_text})
    except (ValueError, SyntaxError) as e:
        return jsonify({'error': f'Invalid input: {str(e)}'}), 400

def decrypt_route():
    """
    Decrypts the given text using the Affine cipher with the provided 'a' and 'b' values.

    Parameters:
    - text: str, the text to decrypt.
    - key: str, the key in the format "[a,b]", obtained from request arguments.
    - cipher: str, should be 'affine' for Affine cipher, obtained from request arguments.

    Returns:
    - JSON response with the decrypted text or an error message with a 400 status code.
    """
    text = request.args.get('text', '')
    key = request.args.get('key', '')
    cipher = request.args.get('cipher', '').lower()

    if cipher != 'affine':
        return jsonify({'error': 'Invalid cipher type. Use "cipher=affine".'}), 400

    try:
        # Parse 'key' as [a, b] for Affine cipher
        a, b = eval(key)
        decrypted_text = decrypt_text(text, a, b)
        return jsonify({'decrypted_text': decrypted_text})
    except (ValueError, SyntaxError) as e:
        return jsonify({'error': f'Invalid input: {str(e)}'}), 400
