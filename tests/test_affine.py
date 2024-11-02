# affine_tests.py
import unittest
from src.services.affine_service import encrypt_text, decrypt_text, mod_inverse


class TestAffineCipher ( unittest.TestCase ):
    def test_encrypt_text(self):
        # Test encryption with valid a, b values
        text = "HELLO"
        a, b = 5, 8
        encrypted_text = encrypt_text ( text, a, b )
        self.assertIsInstance ( encrypted_text, str )
        self.assertNotEqual ( encrypted_text, text )  # Should be different from the original text

    def test_decrypt_text(self):
        # Test decryption with valid a, b values
        text = "HELLO"
        a, b = 5, 8
        encrypted_text = encrypt_text ( text, a, b )
        decrypted_text = decrypt_text ( encrypted_text, a, b )
        self.assertEqual ( decrypted_text, text )  # Decryption should return the original text

    def test_invalid_a_value(self):
        # Test error handling for invalid a (not coprime with 26)
        text = "HELLO"
        a, b = 13, 8  # a = 13 has no modular inverse mod 26
        with self.assertRaises ( ValueError ) as context:
            encrypt_text ( text, a, b )
        self.assertIn ( "must be coprime with 26", str ( context.exception ) )

    def test_mod_inverse(self):
        # Test modular inverse function
        self.assertEqual ( mod_inverse ( 5 ), 21 )  # 5 * 21 % 26 == 1
        self.assertEqual ( mod_inverse ( 7 ), 15 )  # 7 * 15 % 26 == 1

        # Test modular inverse error for invalid 'a'
        with self.assertRaises ( ValueError ) as context:
            mod_inverse ( 13 )  # 13 has no modular inverse mod 26
        self.assertIn ( "No modular inverse", str ( context.exception ) )

    def test_non_alpha_characters(self):
        # Test encryption and decryption with non-alphabet characters in text
        text = "HELLO, WORLD!"
        a, b = 5, 8
        encrypted_text = encrypt_text ( text, a, b )
        decrypted_text = decrypt_text ( encrypted_text, a, b )

        # Ensure non-alpha characters are preserved
        self.assertEqual (
            decrypted_text,
            "HELLO, WORLD!"
        )


if __name__ == "__main__":
    unittest.main ()
