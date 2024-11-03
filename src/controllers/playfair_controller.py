from flask import request, jsonify
from src.services.hill_service import playfair_encryption, playfair_decryption, create_playfair_key_matrix

# Define a helper function to validate the key
def is_valid_key(key):
    # Check if key is a string and contains only alphabetic characters
    return isinstance(key, str) and key.isalpha()

def encrypt_route():
  '''Encrypts plaintext using Playfair cipher after getting the necessary input parameters from the user.
    parameters:
    text = plaintext obtained from the user
    key = key obtained from the user 
    '''
   text = request.args.get('text', '')
   key = request.args.get('key', '')
   if not is_valid_key(key):
        return jsonify({"error": "Invalid key. Key must be a string of alphabetic characters only."}), 400

    # Call the Playfair encryption function
    encrypted_text = playfair_encryption(text, key)
    return jsonify({"ciphertext": encrypted_text})

def playfair_decrypt():
    '''Decrypts ciphertext using Playfair cipher after getting the necessary input parameters from the user.
    parameters:
    text = ciphertext obtained from the user
    key = key obtained from the user 
    '''
    data = request.get_json()
    ciphertext = data.get('ciphertext', '')
    key = data.get('key', '')

    # Validate the key
    if not is_valid_key(key):
        return jsonify({"error": "Invalid key. Key must be a string of alphabetic characters only."}), 400

    # Call the Playfair decryption function
    decrypted_text = playfair_decryption(ciphertext, key)
    return jsonify({"plaintext": decrypted_text})
  
