import unittest

from caesar_cipher.cipher import caesar, decrypt, encrypt


class CaesarCipherTests(unittest.TestCase):
    def test_encrypts_lowercase_and_uppercase_letters(self):
        self.assertEqual(encrypt("Abc XyZ", 3), "Def AbC")

    def test_decrypt_reverses_encryption(self):
        original = "Meet me at 10:30!"
        self.assertEqual(decrypt(encrypt(original, 11), 11), original)

    def test_preserves_punctuation_numbers_and_unicode(self):
        text = "Hello, world! 123 — café."
        self.assertEqual(encrypt(text, 1), "Ifmmp, xpsme! 123 — dbgé.")

    def test_caesar_can_decrypt_with_keyword_argument(self):
        self.assertEqual(caesar("Khoor", 3, encrypting=False), "Hello")

    def test_rejects_non_integer_shift(self):
        with self.assertRaises(ValueError):
            encrypt("hello", "3")

    def test_rejects_shift_outside_supported_range(self):
        for shift in (0, 26, -1):
            with self.subTest(shift=shift):
                with self.assertRaises(ValueError):
                    encrypt("hello", shift)

    def test_rejects_non_string_text(self):
        with self.assertRaises(TypeError):
            encrypt(123, 3)


if __name__ == "__main__":
    unittest.main()