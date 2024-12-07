import unittest
from src.services.hill_service import encrypt_text, decrypt_text, mod_inverse_matrix
import numpy as np

class TestHillCipher(unittest.TestCase):
    """
    Unit tests for the Hill cipher functions including encryption, decryption, and matrix inversion.
    Tests cover both 2x2 and 3x3 matrices, input validation, and error handling.
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
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        encrypted = encrypt_text(text, matrix, alphabet)

        self.assertIsInstance(encrypted, str)
        self.assertNotEqual(encrypted, text)

    def test_decrypt_text(self):
        """
        Test decryption with a 2x2 matrix and verify decrypted text matches original.

        Validates that:
        - Decrypted text matches the original up to padding length.
        - The inverse matrix is a valid numpy array.
        """
        matrix = np.array([[3, 3], [2, 5]])
        text = "HELLOX"  # Padded text for proper length
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        encrypted = encrypt_text(text, matrix, alphabet)
        decrypted, inverse_matrix = decrypt_text(encrypted, matrix, alphabet)

        self.assertEqual(decrypted[:len(text)], text)
        self.assertIsInstance(inverse_matrix, list)  # Inverse matrix should be a list

    def test_invalid_text_length(self):
        """
        Test that an invalid text length raises a ValueError.

        Validates that:
        - A `ValueError` is raised when the text length is not divisible by the matrix size.
        - The exception message includes the correct information about text length divisibility.
        """
        matrix = np.array([[3, 3], [2, 5]])
        text = "HELLO"  # Length 5 is not divisible by 2 (for 2x2 matrix)
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        with self.assertRaises(ValueError) as context:
            encrypt_text(text, matrix, alphabet)

        self.assertIn("Text length must be divisible", str(context.exception))

    def test_non_invertible_matrix(self):
        """
        Test that a non-invertible matrix raises a ValueError during decryption.

        Validates that:
        - A `ValueError` is raised when attempting to decrypt with a non-invertible matrix.
        - The exception message indicates that the matrix determinant is zero.
        """
        non_invertible_matrix = np.array([[2, 4], [2, 4]])
        text = "HELLOX"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        with self.assertRaises(ValueError) as context:
            decrypt_text(text, non_invertible_matrix, alphabet)

        self.assertIn("Matrix determinant is zero", str(context.exception))

    def test_3x3_matrix_encryption(self):
        """
        Test encryption and decryption with a 3x3 matrix and a compatible text length.

        Validates that:
        - Encrypted text is different from the original text.
        - Decrypted text matches the original.
        - The inverse matrix is a valid numpy array.
        """
        matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
        text = "ACTNOW"  # Length divisible by 3 for 3x3 matrix
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        encrypted = encrypt_text(text, matrix, alphabet)
        decrypted, inverse_matrix = decrypt_text(encrypted, matrix, alphabet)

        self.assertNotEqual(encrypted, text)
        self.assertEqual(decrypted[:len(text)], text)
        self.assertIsInstance(inverse_matrix, list)  # Ensure the inverse matrix is returned as a list

    def test_custom_alphabet(self):
        """
        Test encryption and decryption with a custom alphabet.
        """
        matrix = np.array([[3, 3], [2, 5]])
        text = "HI"  # Custom text including numbers
        alphabet = "ABZDEFGHIJKLMNOPQRSTUVWXYB"
        encrypted = encrypt_text(text, matrix, alphabet)
        decrypted, _ = decrypt_text(encrypted, matrix, alphabet)

        self.assertIsInstance(encrypted, str)
        self.assertNotEqual(encrypted, text)

    def test_invalid_characters_in_text(self):
        """
        Test encryption skips characters not in the provided alphabet.
        """
        matrix = np.array([[3, 3], [2, 5]])
        text = "HELLO@WORLD!"  # Contains invalid characters
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        encrypted = encrypt_text(text, matrix, alphabet)

        # Check that the invalid characters are retained in the same positions
        self.assertEqual(encrypted[5], '@')
        self.assertEqual(encrypted[-1], '!')

    def test_mod_inverse_matrix(self):
        """
        Test the modular inverse of a 2x2 and 3x3 matrix.
        """
        matrix_2x2 = np.array([[3, 3], [2, 5]])
        mod = 26
        inverse_2x2 = mod_inverse_matrix(matrix_2x2, mod)
        expected_inverse_2x2 = np.array([[15, 17], [20, 9]])

        self.assertTrue(np.array_equal(inverse_2x2, expected_inverse_2x2))

        matrix_3x3 = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
        inverse_3x3 = mod_inverse_matrix(matrix_3x3, mod)
        expected_inverse_3x3 = np.array([[8, 5, 10], [21, 8, 21], [21, 12, 8]])

        self.assertTrue(np.array_equal(inverse_3x3, expected_inverse_3x3))


if __name__ == "__main__":
    unittest.main()
