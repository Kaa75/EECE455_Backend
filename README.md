# How to Run Backend
- Download the GitHub repository (either clone or via zip download and extract)
- Go to backend folder root directory (i.e. `cd EECE455_Backend`)
- `pip install -r requirements.txt`
- `cd src` --> `python main.py`

# How to Run Unit Tests
- From the backend folder root:
    * To run all unit tests together: `python -m unittest discover -s tests -p "test_*.py"`
    * To run only one unit test Python file (e.g. Vigenere unit tests): `python -m unittest tests/test_vigenere.py`


# Branch and Development Workflow

## Branch Creation
Each team member should create a dedicated branch for their assigned cipher, using the following format for branch names:

[YourName]/[CipherName]
If you are working on multiple ciphers, create a separate branch for each.

Also as We Said we will use Flask

## Encryption/Decryption Implementation

Complete the encryption and decryption functionality for your assigned cipher(s) according to project requirements.
If you are also responsible for implementing specific API endpoints, ensure those are fully developed, tested, and documented.
Commit and Pull Request Protocol

# Do not push directly to the main branch.
Submit all work through pull requests for review. Ensure each pull request clearly indicates the functionality implemented and any associated tests.

### Documentation
After completing all encryption and decryption functions, replace this file with a comprehensive README.md. The README should include:

- Overview of each cipher and its purpose

- Details on API endpoints, including input/output formats
- Setup instructions and any dependencies
- Instructions for testing


# Project Deadlines
Mandatory Part (Project 1):
Complete all required work by Monday morning.

Team Meeting:
Ensure timely submission so we can review everything in our scheduled meeting.

### Contributers
- [Karim Abboud](https://github.com/Kaa75)
- [Omar Ramadan](https://github.com/omarram811)
- [Ranam Hamoud](https://github.com/ranamkhamoud)
- [Kevin Kfoury](https://github.com/SeeKraken1)
- [Hadi Al Mubasher](https://github.com/hadi-mubasher)
