import unittest
from src.services.mono_alphabetic_service import encrypt_text, decrypt_text

class TestMonoAlphabeticCipher(unittest.TestCase):
    """
    Unit tests for the mono-alphabetic cipher encryption and decryption functions.
    
    Test Methods:
    - test_encrypt_text: Verifies encryption with a sample key and plaintext.
    - test_decrypt_text: Verifies decryption with a sample key and ciphertext.
    """
    def test_encrypt_text(self):
        text = "hello"
        key = "zyxwvutsrqponmlkjihgfedcba"
        encrypted_text = encrypt_text(text, key)
        self.assertIsInstance(encrypted_text, str)
        self.assertNotEqual(encrypted_text, text)

        # Text and key generated randomly from https://www.101computing.net/mono-alphabetic-substitution-cipher/
        text2 = "A long time ago, in a galaxy far, far away... It is a dark time for the Rebellion. Although the Death Star has been destroyed, Imperial troops have driven the Rebel forces from their hidden base and pursued them across the galaxy. Evading the dreaded Imperial Starfleet, a group of freedom fighters led by Luke Skywalker has established a new secret base on the remote ice world of Hoth. The evil lord Darth Vader, obsessed with finding young Skywalker, has dispatched thousands of remote probes into the far reaches of space…"
        key2 = "MXEKQSCWGFYBJITRVDNZHUOPAL"
        encrypt_text2 = encrypt_text(text2, key2)
        self.assertIsInstance(encrypt_text2, str)
        self.assertNotEqual(encrypt_text, text)

    def test_decrypt_text(self):
        text = "svool"
        key = "zyxwvutsrqponmlkjihgfedcba"
        decrypted_text = decrypt_text(text, key)
        self.assertEqual(decrypted_text, "hello")

        # Used encrypted result above and same key to assert correct decryption of the same original text
        text2 = "m btic zgjq mct, gi m cmbmpa smd, smd moma... gz gn m kmdy zgjq std zwq dqxqbbgti. mbzwthcw zwq kqmzw nzmd wmn xqqi kqnzdtaqk, gjrqdgmb zdttrn wmuq kdguqi zwq dqxqb stdeqn sdtj zwqgd wgkkqi xmnq mik rhdnhqk zwqj medtnn zwq cmbmpa. qumkgic zwq kdqmkqk gjrqdgmb nzmdsbqqz, m cdthr ts sdqqktj sgcwzqdn bqk xa bhyq nyaombyqd wmn qnzmxbgnwqk m iqo nqedqz xmnq ti zwq dqjtzq geq otdbk ts wtzw. zwq qugb btdk kmdzw umkqd, txnqnnqk ogzw sgikgic athic nyaombyqd, wmn kgnrmzewqk zwthnmikn ts dqjtzq rdtxqn gizt zwq smd dqmewqn ts nrmeq…"
        key2 = "MXEKQSCWGFYBJITRVDNZHUOPAL"
        decrypted_text = decrypt_text(text2, key2)
        self.assertEqual(decrypted_text, "a long time ago, in a galaxy far, far away... it is a dark time for the rebellion. although the death star has been destroyed, imperial troops have driven the rebel forces from their hidden base and pursued them across the galaxy. evading the dreaded imperial starfleet, a group of freedom fighters led by luke skywalker has established a new secret base on the remote ice world of hoth. the evil lord darth vader, obsessed with finding young skywalker, has dispatched thousands of remote probes into the far reaches of space…")

if __name__ == '__main__':
    unittest.main()
