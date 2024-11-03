# Mono-Alphabetic Cipher API

## Overview
The Mono-Alphabetic Cipher API provides encryption and decryption using a substitution cipher. In this cipher, each letter in the plaintext is replaced by a corresponding letter in a 26-character key. This key serves as a substitution pattern, making the cipher more secure when compared to simple ciphers like Caesar. It’s commonly used in cryptography education and simple text-based encryption tasks.

## API Endpoints
### 1. Encrypt Text
- **Endpoint**: `/monoalphabetic/encrypt`
- **Method**: `GET`
- **Parameters**:
  - `text` (str): The plaintext to encrypt.
  - `key` (str): A 26-character alphabetic string representing the substitution key.
  - `cipher` (str): Must be set to `'mono_alphabetic'`.
- **Response**:
  - **Success**: `{ "encrypted_text": "ciphertext" }`
  - **Error**: `{ "error": "error message" }`, status code 400.

### 2. Decrypt Text
- **Endpoint**: `/monoalphabetic/decrypt`
- **Method**: `GET`
- **Parameters**:
  - `text` (str): The ciphertext to decrypt.
  - `key` (str): A 26-character alphabetic string representing the substitution key.
  - `cipher` (str): Must be set to `'mono_alphabetic'`.
- **Response**:
  - **Success**: `{ "decrypted_text": "plaintext" }`
  - **Error**: `{ "error": "error message" }`, status code 400.

## Input/Output Formats
- **Encryption Input Example**:
  ```json
  {
    "text": "hello",
    "key": "zyxwvutsrqponmlkjihgfedcba",
    "cipher": "mono_alphabetic"
  }

- **Encryption Output Example**:
  ```json
  {
  "encrypted_text": "svool"
  }

- **Decryption Input Example**:
  ```json
  {
    "text": "svool",
    "key": "zyxwvutsrqponmlkjihgfedcba",
    "cipher": "mono_alphabetic"
  }


- **Decryption Output Example**:
  ```json
  {
    "decrypted_text": "hello"
  }
