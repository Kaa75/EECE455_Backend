import unittest
from src.services.vigenere_service import encrypt_text, decrypt_text

class TestVigenereCipher(unittest.TestCase):
    """
    Unit tests for Vigenère cipher encryption and decryption.

    Test Methods:
    - test_encryption: Verifies Vigenère encryption for given plaintext and key.
    - test_decryption: Verifies Vigenère decryption for given encrypted text and key.
    - test_non_alpha_characters: Checks that non-alphabetic characters remain unchanged.
    """

    def test_encryption(self):
        plaintext = "HELLO WORLD"
        key = "KEY"
        expected_encryption = "RIJVS UYVJN"
        self.assertEqual(encrypt_text(plaintext, key), expected_encryption)

        plaintext = "ATTACKATDAWN"
        key = "LEMON"
        expected_encryption = "LXFOPVEFRNHR"
        self.assertEqual(encrypt_text(plaintext, key), expected_encryption)

    def test_decryption(self):
        encrypted_text = "RIJVS UYVJN"
        key = "KEY"
        expected_plaintext = "HELLO WORLD"
        self.assertEqual(decrypt_text(encrypted_text, key), expected_plaintext)

        encrypted_text = "LXFOPVEFRNHR"
        key = "LEMON"
        expected_plaintext = "ATTACKATDAWN"
        self.assertEqual(decrypt_text(encrypted_text, key), expected_plaintext)

    def test_non_alpha_characters(self):
        plaintext = "HELLO, WORLD!"
        key = "KEY"
        encrypted_text = encrypt_text(plaintext, key)
        decrypted_text = decrypt_text(encrypted_text, key)
        self.assertEqual(decrypted_text, plaintext)  # Non-alpha characters should remain unchanged

    def test_empty_string(self):
        plaintext = ""
        key = "ANYKEY"
        self.assertEqual(encrypt_text(plaintext, key), "")
        self.assertEqual(decrypt_text(plaintext, key), "")

    def test_single_character(self):
        plaintext = "A"
        key = "B"
        expected_encryption = "B"
        self.assertEqual(encrypt_text(plaintext, key), expected_encryption)
        self.assertEqual(decrypt_text(expected_encryption, key), plaintext)

    def test_key_same_length_as_text(self):
        plaintext = "HELLO"
        key = "XMCKL"  # Same length as plaintext
        expected_encryption = "EQNVZ"
        self.assertEqual(encrypt_text(plaintext, key), expected_encryption)
        self.assertEqual(decrypt_text(expected_encryption, key), plaintext)

    def test_long_key(self):
        # Test with a long key relative to the plaintext
        plaintext = "HELLO"
        key = "LONGKEYTHATISLONGER"
        expected_encryption = "SSYRY"
        self.assertEqual(encrypt_text(plaintext, key), expected_encryption)
        self.assertEqual(decrypt_text(expected_encryption, key), plaintext)

if __name__ == '__main__':
    unittest.main()
