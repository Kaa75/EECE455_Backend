import sqlite3
import os
from flask import request, jsonify
from services.playfair_service import playfair_encryption, playfair_decryption, create_playfair_key_matrix

# Define a helper function to validate the key
def is_valid_key(key):
    # Check if key is a string and contains only alphabetic characters
    return isinstance(key, str) and key.isalpha()

# Helper function to log Playfair operations
def log_playfair_operation(operation, input_text, key, result_text):
    try:
        # Connect to SQLite database
        current_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(current_dir, '../..', 'encryption_log.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Insert log into playfair_log table
        cursor.execute('''
            INSERT INTO playfair_log (operation, input_text, key, output_text)
            VALUES (?, ?, ?, ?)
        ''', (operation, input_text, key, result_text))

        # Commit and close connection
        conn.commit()
        conn.close()

    except Exception as e:
        print(f"Error logging Playfair operation: {e}")

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

    log_playfair_operation('encrypt', text, key, encrypted_text)

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

    log_playfair_operation('decrypt', text, key, decrypted_text)

    return jsonify({'decrypted_text': decrypted_text})
  
