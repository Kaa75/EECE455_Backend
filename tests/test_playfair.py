import unittest
from src.services.playfair_service import playfair_encryption, playfair_decryption, create_playfair_key_matrix
from src.controllers.playfair_controller import encrypt,decrypt

class TestPlayFairCipher(unittest.TestCase):
  '''Applying some testcases to check functionality'''
  def test_encryption(self):
    '''Encrypting a text, validating its type, and checking for a mismatch between the original text and the ciphertext'''
    key = "PROBLEMS"
    plaintext = "SHE WENT TO THE STORE"
    encrypted_text = playfair_encryption(plaintext,key)
    self.assertIsInstance(encrypted_text, str)
    self.assertNotEqual(encrypted_text, plaintext)
  def test_decryption(self):
    '''Decrypting a text, validating its type, and checking for a mismatch between the ciphertext and the plaintext'''
    key = "PROBLEMS"
    plaintext = "SHE WENT TO THE STORE"
    ciphertext = "AGMVMKQYQBYTMAQBPM"
    decrypted_text = playfair_decryption(ciphertext,key)
    self.assertIsInstance(decrypted_text,str)
    self.assertEqual(plaintext,decrypted_text)
  def test_keys(self):
    '''Testing an invalid key to see if an error gets raised'''

if __name__ == "__main__":
    unittest.main()
