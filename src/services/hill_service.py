import numpy as np


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
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int)  # Adjugate matrix
    return (det_inv * adjugate % mod).astype(int)

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

def hill_cipher(text, matrix, alphabet, mode='encrypt'):
    """
    Core function for the Hill cipher, encrypts or decrypts text based on the provided matrix.

    Parameters:
    - text: str, the text to encrypt or decrypt.
    - matrix: numpy.ndarray, the matrix used for transformation.
    - alphabet: str, the custom alphabet to use.
    - mode: str, 'encrypt' for encryption, 'decrypt' for decryption.

    Returns:
    - str: the resulting encrypted or decrypted text.
    """
    matrix_size = matrix.shape[0]
    mod = len(alphabet)

    # Create mappings for the alphabet
    ALPHABET_DICT = {char: idx for idx, char in enumerate(alphabet)}
    REVERSE_ALPHABET_DICT = {idx: char for idx, char in enumerate(alphabet)}

    def text_to_vector(block):
        return [ALPHABET_DICT[char] for char in block]

    def vector_to_text(vector):
        return ''.join(REVERSE_ALPHABET_DICT[num % mod] for num in vector)

    validate_text_length(text, matrix_size)
    processed_text = process_text(text)
    result_text = ''

    for i in range(0, len(processed_text), matrix_size):
        block = processed_text[i:i + matrix_size]
        vector = text_to_vector(block)

        # Perform matrix multiplication
        transformed_vector = np.dot(matrix, vector) % mod
        result_text += vector_to_text(transformed_vector.astype(int))

    # Reinsert non-alphabet characters
    full_result = ''
    j = 0
    for char in text:
        if char.upper() in alphabet:
            full_result += result_text[j]
            j += 1
        else:
            full_result += char
    return full_result

def encrypt_text(text, matrix, alphabet):
    """
    Encrypt text using the Hill cipher with the specified key matrix and alphabet.

    Parameters:
    - text: str, the text to encrypt.
    - matrix: numpy.ndarray, the key matrix used for encryption (2x2 or 3x3).
    - alphabet: str, the custom alphabet to use.

    Returns:
    - str: the encrypted text.

    Raises:
    - ValueError: if the matrix is not 2x2 or 3x3.
    """
    if matrix.shape[0] != matrix.shape[1] or matrix.shape[0] not in [2, 3]:
        raise ValueError("Matrix must be 2x2 or 3x3.")
    return hill_cipher(text, matrix, alphabet, mode='encrypt')

def decrypt_text(text, matrix, alphabet):
    """
    Decrypt text using the Hill cipher with the specified key matrix and alphabet.

    Parameters:
    - text: str, the text to decrypt.
    - matrix: numpy.ndarray, the key matrix used for decryption (2x2 or 3x3).
    - alphabet: str, the custom alphabet to use.

    Returns:
    - tuple:
        - str: the decrypted text.
        - list of list of int: the inverse matrix used for decryption.

    Raises:
    - ValueError: if the matrix is not 2x2 or 3x3 or if the inverse does not exist.
    """
    if matrix.shape[0] != matrix.shape[1] or matrix.shape[0] not in [2, 3]:
        raise ValueError("Matrix must be 2x2 or 3x3.")
    inverse_matrix = mod_inverse_matrix(matrix, mod=len(alphabet))
    decrypted_text = hill_cipher(text, inverse_matrix, alphabet, mode='decrypt')
    return decrypted_text, inverse_matrix.tolist()
