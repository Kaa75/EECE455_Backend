from flask import Flask, request, jsonify
from flask_cors import CORS
from controllers import (
    affine_controller,
    vigenere_controller,
    playfair_controller,
    hill_controller,
    mono_alphabetic_controller,
    euclid_controller,
)

app = Flask(__name__)

CORS(app)

cipher_controllers = {
    'affine': affine_controller,
    'vigenere': vigenere_controller,
    'playfair': playfair_controller,
    'hill': hill_controller,
    'mono_alphabetic': mono_alphabetic_controller,
    'euclid': euclid_controller,
}

# Encryption route
@app.route('/encrypt/<cipher>', methods=['POST'])
def encrypt_route(cipher):
    data = request.get_json()
    controller = cipher_controllers.get(cipher)
    
    if controller is None or not hasattr(controller, 'encrypt'):
        return jsonify({'error': f'Encryption method for {cipher} not found.'}), 400
    
    try:
        result = controller.encrypt(data)
        return result
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Decryption route
@app.route('/decrypt/<cipher>', methods=['POST'])
def decrypt_route(cipher):
    data = request.get_json()
    controller = cipher_controllers.get(cipher)
    
    if controller is None or not hasattr(controller, 'decrypt'):
        return jsonify({'error': f'Decryption method for {cipher} not found.'}), 400
    
    try:
        result = controller.decrypt(data)
        return result
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Brute-force decryption route
@app.route('/bruteforce/<cipher>', methods=['POST'])
def bruteforce_route(cipher):
    data = request.get_json()
    controller = cipher_controllers.get(cipher)
    
    if controller is None or not hasattr(controller, 'bruteforce'):
        return jsonify({'error': f'Brute-force method for {cipher} not found.'}), 400
    
    try:
        result = controller.bruteforce(data)
        return jsonify({'bruteforce_results': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
