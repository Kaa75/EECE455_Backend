from flask import Flask
from controllers import (
    affine_controller,
    vigenere_controller,
    playfair_controller,
    hill_controller,
    mono_alphabetic_controller,
    euclid_controller,
)

app = Flask(__name__)


# Register routes
app.add_url_rule('/encrypt/affine', view_func=affine_controller.encrypt_route, methods=['GET'])
app.add_url_rule('/decrypt/affine', view_func=affine_controller.decrypt_route, methods=['GET'])
app.add_url_rule('/crack/affine', view_func=affine_controller.crack_route, methods=['GET'])




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)