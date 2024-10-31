from fastapi import FastAPI
from controllers import (
    affine_controller,
    vigenere_controller,
    playfair_controller,
    hill_controller,
    mono_alphabetic_controller,
    euclid_controller,
)

app = FastAPI()


# Register routes



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)