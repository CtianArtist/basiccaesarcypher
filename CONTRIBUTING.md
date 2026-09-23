# Contributing

Thanks for helping improve Caesar Cipher.

## Local setup

This project uses only the Python standard library at runtime. A virtual
environment is optional, but recommended for development:

```bash
python -m venv .venv
source .venv/bin/activate
```

## Before opening a pull request

Run the test suite from the repository root:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Keep the cipher logic in `src/caesar_cipher/cipher.py` independent from the
GUI. New behavior should have a corresponding test in `tests/`.

## Pull requests

- Explain what changed and why.
- Keep pull requests focused.
- Update the README when user-facing behavior changes.