# Caesar Cipher

A small, dependency-free desktop app for encrypting and decrypting text with a
Caesar cipher. It uses Python's built-in Tkinter toolkit, so there is no
application dependency to install.

## Features

- Encrypt and decrypt lowercase and uppercase English letters.
- Preserve spaces, punctuation, numbers, and non-English characters.
- Choose a shift from 1 through 25.
- Copy encrypted or decrypted output to the clipboard.
- Use the cipher logic as a standalone Python module.

## Requirements

- Python 3.10 or newer
- Tkinter (usually included with Python; some Linux distributions provide it
  as a separate system package)

## Run the app

From the repository root:

```bash
PYTHONPATH=src python -m caesar_cipher
```

Or install the package in editable mode first:

```bash
python -m pip install -e .
python -m caesar_cipher
```

## Use the library

```python
from caesar_cipher.cipher import decrypt, encrypt

encrypted = encrypt("Attack at dawn!", 3)
print(encrypted)  # Dwwdfn dw gdzq!

print(decrypt(encrypted, 3))  # Attack at dawn!
```

Invalid shifts raise `ValueError`:

```python
encrypt("hello", 0)       # ValueError
encrypt("hello", "three") # ValueError
```

## Run tests

The test suite uses Python's standard library and needs no third-party
packages:

```bash
python -m unittest discover -s tests -v
```

## Project layout

```text
.
├── .github/workflows/ci.yml  # Continuous integration
├── src/caesar_cipher/
│   ├── cipher.py             # Pure encryption/decryption logic
│   ├── gui.py                # Tkinter user interface
│   └── __main__.py           # Application entry point
└── tests/
    └── test_cipher.py        # Unit tests for the cipher
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).