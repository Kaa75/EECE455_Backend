import numpy as np
import string

# Constants and dictionaries for character mapping
ALPHABET = string.ascii_uppercase
ALPHABET_DICT = {char: idx for idx, char in enumerate(ALPHABET)}
REVERSE_ALPHABET_DICT = {idx: char for idx, char in enumerate(ALPHABET)}

def mod_inverse_matrix(matrix, mod=26):
    """
    Calculate the modular inverse of a matrix under a specified modulus.

    Parameters:
    - matrix: numpy.ndarray, the matrix to invert.
    - mod: int, the modulus for the inversion operation, default is 26.

    Returns:
    - numpy.ndarray: the modular inverse of the input matrix under the specified modulus.

    Raises:
    - ValueError: if the matrix is non-invertible under the given modulus.
    """
    det = int(round(np.linalg.det(matrix)))
    if det == 0:
        raise ValueError("Matrix determinant is zero, inverse does not exist.")

    det_inv = pow(det % mod, -1, mod)  # Modular inverse of the determinant
    matrix_mod_inv = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % mod) % mod
    return matrix_mod_inv.astype(int)

def validate_text_length(text, matrix_size):
    """
    Validate if the length of the text is divisible by the matrix size for encryption or decryption.

    Parameters:
    - text: str, the input text to validate.
    - matrix_size: int, the size of the matrix (e.g., 2 for 2x2 matrix).

    Raises:
    - ValueError: if the length of filtered text is not divisible by the matrix size.
    """
    filtered_text = ''.join([char for char in text if char.isalpha()])
    if len(filtered_text) % matrix_size != 0:
        raise ValueError(f"Text length must be divisible by {matrix_size} for the given matrix size.")

def process_text(text):
    """
    Process the text to retain only alphabetic characters and convert them to uppercase.

    Parameters:
    - text: str, the input text to process.

    Returns:
    - str: processed text containing only uppercase alphabetic characters.
    """
    return ''.join([char for char in text if char.isalpha()]).upper()

def text_to_vector(block):
    """
    Convert a block of text into a vector of numbers based on alphabetical positions.

    Parameters:
    - block: str, a block of text.

    Returns:
    - list of int: a list of numbers representing each character in the block.
    """
    return [ALPHABET_DICT[char] for char in block]

def vector_to_text(vector):
    """
    Convert a vector of numbers back to text based on alphabetical positions.

    Parameters:
    - vector: list of int, the vector to convert.

    Returns:
    - str: the text corresponding to the input vector.
    """
    return ''.join(REVERSE_ALPHABET_DICT[num % 26] for num in vector)

def hill_cipher(text, matrix, mode='encrypt'):
    """
    Core function for the Hill cipher, encrypts or decrypts text based on the provided matrix.

    Parameters:
    - text: str, the text to encrypt or decrypt.
    - matrix: numpy.ndarray, the matrix used for transformation.
    - mode: str, 'encrypt' for encryption, 'decrypt' for decryption.

    Returns:
    - str: the resulting encrypted or decrypted text.
    """
    matrix_size = matrix.shape[0]
    validate_text_length(text, matrix_size)

    processed_text = process_text(text)
    result_text = ''
    for i in range(0, len(processed_text), matrix_size):
        block = processed_text[i:i + matrix_size]
        vector = text_to_vector(block)

        # Encrypt or decrypt
        transformed_vector = np.dot(matrix, vector) % 26
        result_text += vector_to_text(transformed_vector.astype(int))

    # Reinsert non-alphabet characters
    full_result = ''
    j = 0
    for char in text:
        if char.upper() in ALPHABET:
            full_result += result_text[j]
            j += 1
        else:
            full_result += char
    return full_result

def encrypt_text(text, matrix):
    """
    Encrypt text using the Hill cipher with the specified key matrix.

    Parameters:
    - text: str, the text to encrypt.
    - matrix: numpy.ndarray, the key matrix used for encryption (2x2 or 3x3).

    Returns:
    - str: the encrypted text.

    Raises:
    - ValueError: if the matrix is not 2x2 or 3x3.
    """
    if matrix.shape[0] != matrix.shape[1] or matrix.shape[0] not in [2, 3]:
        raise ValueError("Matrix must be 2x2 or 3x3.")
    return hill_cipher(text, matrix, mode='encrypt')

def decrypt_text(text, matrix):
    """
    Decrypt text using the Hill cipher with the specified key matrix.

    Parameters:
    - text: str, the text to decrypt.
    - matrix: numpy.ndarray, the key matrix used for decryption (2x2 or 3x3).

    Returns:
    - tuple:
        - str: the decrypted text.
        - list of list of int: the inverse matrix used for decryption.

    Raises:
    - ValueError: if the matrix is not 2x2 or 3x3 or if the inverse does not exist.
    """
    if matrix.shape[0] != matrix.shape[1] or matrix.shape[0] not in [2, 3]:
        raise ValueError("Matrix must be 2x2 or 3x3.")
    inverse_matrix = mod_inverse_matrix(matrix)
    decrypted_text = hill_cipher(text, inverse_matrix, mode='decrypt')
    return decrypted_text, inverse_matrix.tolist()  # Return inverse matrix for API response
