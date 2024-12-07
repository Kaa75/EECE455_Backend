import unittest
from src.services.euclid_service import modular_inverse, format_table

class TestEuclid(unittest.TestCase):
    """
    Unit tests for the Euclidean algorithm modular inverse and table formatting.

    Test Methods:
    - test_modular_inverse_exists: Verifies calculation of modular inverse for valid inputs.
    - test_no_modular_inverse: Checks error handling for inputs with no inverse.
    - test_table_format: Verifies the format of the Euclidean table.
    """
    def test_modular_inverse_exists(self):
        a, mod = 3, 11
        inverse, _ = modular_inverse(a, mod)
        self.assertEqual(inverse, 4)

        a, mod = 2345, 6789
        inverse, _ = modular_inverse(a, mod)
        self.assertEqual(inverse, 4664) # y = -2125 --> -2125 mod 6789 = 4664

        a, mod = 550, 1759
        inverse, _ = modular_inverse(a, mod)
        self.assertEqual(inverse, 355)

        a, mod = 123457, 765432
        inverse, _ = modular_inverse(a, mod) 
        self.assertEqual(inverse, 656089) # y = -109343 --> -109343 mod 765432 = 656089



    def test_no_modular_inverse(self):
        a, mod = 2, 4
        inverse, table = modular_inverse(a, mod)
        self.assertIsNone(inverse)

        a, mod = 123456, 78910
        inverse, table = modular_inverse(a, mod) # GCD = 2
        self.assertIsNone(inverse) 

        a, mod = 987654, 123456
        inverse, table = modular_inverse(a, mod) # GCD = 6
        self.assertIsNone(inverse) 

    def test_table_format(self):
        a, mod = 3, 11
        _, table = modular_inverse(a, mod)
        formatted = format_table(table)
        self.assertIsInstance(formatted, str)
        self.assertIn("|", formatted)  # Check formatting

if __name__ == '__main__':
    unittest.main()
