from flask import request, jsonify
from services.playfair_service import playfair_encryption, playfair_decryption, create_playfair_key_matrix

# Define a helper function to validate the key
def is_valid_key(key):
    # Check if key is a string and contains only alphabetic characters
    return isinstance(key, str) and key.isalpha()

def encrypt(request):
  '''Encrypts plaintext using Playfair cipher after getting the necessary input parameters from the user.
    parameters:
    text = plaintext obtained from the user
    key = key obtained from the user 
    '''
    text = request.get('inputText', '')
    key = request.get('keyString', '')
    cipher = request.get('cipher', '').lower()
    if cipher != 'playfair':
        return jsonify({'error': 'Invalid cipher type. Use "cipher=playfair".'}), 400
    if not is_valid_key(key):
     return jsonify({"error": "Invalid key. Key must be a string of alphabetic characters only."}), 400

    # Call the Playfair encryption function
    encrypted_text = playfair_encryption(text, key)
    return jsonify({"encrypted_text": encrypted_text})

def decrypt(request):
    '''Decrypts ciphertext using Playfair cipher after getting the necessary input parameters from the user.
    parameters:
    text = ciphertext obtained from the user
    key = key obtained from the user 
    '''
    text = request.get('inputText', '')
    key = request.get('keyString', '')
    cipher = request.get('cipher', '').lower()

    if cipher != 'playfair':
        return jsonify({'error': 'Invalid cipher type. Use "cipher=playfair".'}), 400
    # Validate the key
    if not is_valid_key(key):
        return jsonify({"error": "Invalid key. Key must be a string of alphabetic characters only."}), 400

    # Call the Playfair decryption function
    decrypted_text = playfair_decryption(text, key)
    return jsonify({'decrypted_text': decrypted_text})
  
