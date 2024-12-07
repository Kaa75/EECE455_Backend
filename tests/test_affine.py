import unittest
from src.services.affine_service import encrypt_text, decrypt_text, crack_text, mod_inverse

class TestAffineCipher(unittest.TestCase):
    """
    Unit tests for the Affine cipher encryption, decryption, and modular inverse functions.
    """

    def test_encrypt_text(self):
        """
        Test that encryption with valid 'a' and 'b' values produces a
        different result from the original text.
        """
        text = "HELLO"
        a, b = 5, 8
        encrypted_text = encrypt_text(text, a, b)
        self.assertIsInstance(encrypted_text, str)
        self.assertNotEqual(encrypted_text, text)

    def test_decrypt_text(self):
        """
        Test that decryption with valid 'a' and 'b' values recovers
        the original plaintext from the encrypted text.
        """
        text = "HELLO"
        a, b = 5, 8
        encrypted_text = encrypt_text(text, a, b)
        decrypted_text = decrypt_text(encrypted_text, a, b)
        self.assertEqual(decrypted_text, text)

    def test_invalid_a_value(self):
        """
        Test that encryption raises a ValueError when 'a' is not coprime
        with 26 (e.g., a = 13), which makes it invalid.
        """
        text = "HELLO"
        a, b = 13, 8  # 'a' = 13 has no modular inverse mod 26
        with self.assertRaises(ValueError) as context:
            encrypt_text(text, a, b)
        self.assertIn("must be coprime with 26", str(context.exception))

    def test_mod_inverse(self):
        """
        Test that the modular inverse function returns correct results
        for valid inputs and raises a ValueError for invalid ones.
        """
        self.assertEqual(mod_inverse(5), 21)  # 5 * 21 % 26 == 1
        self.assertEqual(mod_inverse(7), 15)  # 7 * 15 % 26 == 1

        # Test modular inverse error for an invalid 'a'
        with self.assertRaises(ValueError) as context:
            mod_inverse(13)  # 13 has no modular inverse mod 26
        self.assertIn("No modular inverse", str(context.exception))

    def test_crack_text(self):
        """
        Test that cracking the Affine cipher using two known frequency
        mappings to 'E' and 'T' correctly determines 'a' and 'b'.
        """
        # For this test, assume the mappings E -> J and T -> X
        freq1, freq2 = 'J', 'X'

        # Calculate 'a' and 'b' using crack_text
        a, b = crack_text(freq1, freq2)

        expected_a, expected_b = 20,7

        # Verify the values of 'a' and 'b'
        self.assertEqual(a, expected_a)
        self.assertEqual(b, expected_b)

if __name__ == "__main__":
    unittest.main()
