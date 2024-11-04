# Extended Euclid Algorithm API

## Overview
The Extended Euclidean Algorithm API calculates the modular inverse of a number under a given modulus. This algorithm is used extensively in cryptographic applications, particularly in modular arithmetic operations required in ciphers and other mathematical computations.

## API Endpoints
### 1. Calculate Modular Inverse
- **Endpoint**: `/euclid/encrypt`
- **Method**: `GET`
- **Parameters**:
  - `a` (int): The number for which the modular inverse is calculated.
  - `mod` (int): The modulus under which to calculate the inverse.
  - `cipher` (str): Must be set to `'euclid'`.
- **Response**:
  - **Success**: `{ "inverse": inverse_value, "table": "formatted Euclidean table" }`
  - **Error**: `{ "error": "error message" }`, status code 400.

### 2. Decryption Endpoint (Unsupported)
- **Endpoint**: `/euclid/decrypt`
- **Method**: `GET`
- **Response**: Always returns an error since decryption is not supported for the Euclidean algorithm.
  - **Error**: `{ "error": "Decrypt not supported for Euclidean cipher." }`, status code 400.

## Input/Output Formats
- **Input Example (GCD=1)**:
  ```json
  {
    "a": 3,
    "mod": 11,
    "cipher": "euclid"
  }

- **Output Example (GCD=1)**:
  ```json
  {
  "inverse": 4,
  "table": "formatted Euclidean table"
  }

- **Input Example (GCD!=1)**:
  ```json
  {
    "a": 2,
    "mod": 4,
    "cipher": "euclid"
  }

- **Output Example  (GCD!=1)**:
  ```json
  {
  "error": "No modular inverse for 2 mod 4",
  "table": "formatted Euclidean table"
  }

## Setup Instructions:
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. **Install Dependencies:**:
   ```bash
   pip install flask

3. **Run the Server**:
   ```bash
   python main.py

## Testing:
To run the tests for the Extended Euclidean algorithm:
1. Navigate to the project root directory.
2. Run the tests:
   ```bash
   python -m unittest discover -s tests
