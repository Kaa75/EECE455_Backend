import unittest
from src.services.hill_service import encrypt_text, decrypt_text, mod_inverse_matrix
from src.controllers.hill_controller import format_matrix
import numpy as np

class TestHillCipher(unittest.TestCase):
    """
    Unit tests for the Hill cipher functions including encryption, decryption, matrix inversion,
    and formatting utilities. Tests cover both 2x2 and 3x3 matrices, input validation, and error handling.
    """

    def test_encrypt_text(self):
        """
        Test encryption with a 2x2 matrix and a text length compatible with the matrix size.

        Validates that:
        - The encrypted result is a string.
        - The encrypted result is different from the original text.
        """
        matrix = np.array([[3, 3], [2, 5]])
        text = "HELLOX"  # Length 6 is divisible by 2 for a 2x2 matrix
        encrypted = encrypt_text(text, matrix)

        self.assertIsInstance(encrypted, str)
        self.assertNotEqual(encrypted, text)

    def test_decrypt_text(self):
        """
        Test decryption with a 2x2 matrix and verify inverse matrix formatting.

        Validates that:
        - Decrypted text matches the original up to padding length.
        - The inverse matrix is formatted correctly as a string.
        """
        matrix = np.array([[3, 3], [2, 5]])
        text = "HELLOX"  # Padded text for proper length
        encrypted = encrypt_text(text, matrix)
        decrypted, inverse_matrix = decrypt_text(encrypted, matrix)

        self.assertEqual(decrypted[:len(text)], text)

        formatted_inverse = format_matrix(np.array(inverse_matrix))
        self.assertEqual(formatted_inverse, "[[15, 17], [20, 9]]")

    def test_invalid_text_length(self):
        """
        Test that an invalid text length raises a ValueError.

        Validates that:
        - A `ValueError` is raised when the text length is not divisible by the matrix size.
        - The exception message includes the correct information about text length divisibility.
        """
        matrix = np.array([[3, 3], [2, 5]])
        text = "HELLO"  # Length 5 is not divisible by 2 (for 2x2 matrix)

        with self.assertRaises(ValueError) as context:
            encrypt_text(text, matrix)

        self.assertIn("Text length must be divisible", str(context.exception))

    def test_non_invertible_matrix(self):
        """
        Test that a non-invertible matrix raises a ValueError during decryption.

        Validates that:
        - A `ValueError` is raised when attempting to decrypt with a non-invertible matrix.
        - The exception message indicates that the matrix determinant is zero.
        """
        non_invertible_matrix = np.array([[2, 4], [2, 4]])

        with self.assertRaises(ValueError) as context:
            decrypt_text("HELLO", non_invertible_matrix)

        self.assertIn("Matrix determinant is zero", str(context.exception))


    def test_3x3_matrix_encryption(self):
        """
        Test encryption and decryption with a 3x3 matrix and a compatible text length.

        Validates that:
        - Encrypted text is different from the original text.
        - Decrypted text matches the original.
        - The inverse matrix is formatted as a standard Python list string.
        """
        matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
        text = "ACTNOW"  # Length divisible by 3 for 3x3 matrix
        encrypted = encrypt_text(text, matrix)
        decrypted, inverse_matrix = decrypt_text(encrypted, matrix)

        self.assertNotEqual(encrypted, text)
        self.assertEqual(decrypted[:len(text)], text)

        formatted_inverse = format_matrix(np.array(inverse_matrix))
        self.assertIsInstance(formatted_inverse, str)

if __name__ == "__main__":
    unittest.main()
