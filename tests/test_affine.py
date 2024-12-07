import unittest
from src.services.affine_service import encrypt_text, decrypt_text, crack_text, mod_inverse

class TestAffineCipher(unittest.TestCase):
    """
    Unit tests for the Affine cipher encryption, decryption, and modular inverse functions.
    """

    def test_encrypt_text(self):
        """
        Test encryption with valid 'a' and 'b' values produces a
        valid encrypted text different from the original.
        """
        text = "HELLO"
        a, b = 5, 8
        encrypted_text = encrypt_text(text, a, b, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertIsInstance(encrypted_text, str)
        self.assertNotEqual(encrypted_text, text)

    def test_decrypt_text(self):
        """
        Test decryption with valid 'a' and 'b' values recovers
        the original plaintext from the encrypted text.
        """
        text = "HELLO"
        a, b = 5, 8
        encrypted_text = encrypt_text(text, a, b, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        decrypted_text = decrypt_text(encrypted_text, a, b, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(decrypted_text, text)

    def test_invalid_a_value(self):
        """
        Test encryption raises a ValueError when 'a' is not coprime
        with the length of the alphabet.
        """
        text = "HELLO"
        a, b = 13, 8  # 'a' = 13 has no modular inverse mod 26
        with self.assertRaises ( ValueError ) as context:
            encrypt_text ( text, a, b, "ABCDEFGHIJKLMNOPQRSTUVWXYZ" )
        self.assertIn ( f"Invalid 'a' value: {a} must be coprime with the length of the alphabet", str ( context.exception ) )

    def test_mod_inverse(self):
        """
        Test the modular inverse function with valid inputs and ensure
        it raises ValueError for invalid inputs.
        """
        self.assertEqual(mod_inverse(5, 26), 21)  # 5 * 21 % 26 == 1
        self.assertEqual(mod_inverse(7, 26), 15)  # 7 * 15 % 26 == 1

        with self.assertRaises(ValueError) as context:
            mod_inverse(13, 26)  # 13 has no modular inverse mod 26
        self.assertIn("No modular inverse", str(context.exception))

    def test_crack_text(self):
        """
        Test cracking the Affine cipher using two known frequency
        mappings and verify the calculated 'a' and 'b'.
        """
        freq1, freq2 = 'J', 'X'
        a, b = crack_text(freq1, freq2, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        expected_a, expected_b = 20, 7

        self.assertEqual(a, expected_a)
        self.assertEqual(b, expected_b)

if __name__ == "__main__":
    unittest.main()
