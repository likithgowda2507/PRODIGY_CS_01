##Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.

Caesar Cipher Encryption-Decryption Tool

This Python program allows users to encrypt and decrypt messages using the Caesar Cipher algorithm, a classic substitution cipher technique. Unlike traditional implementations limited to alphabetic characters, this version supports:

✅ Letters (a-z, A-Z)
✅ Digits (0-9)
✅ Symbols and punctuation (!@#$%^&*, etc.)
✅ Whitespace characters
🛠 Features
User-friendly interactive CLI
Input any message and shift value
Supports both encryption and decryption
Works with all printable ASCII characters
🚀 How It Works
Characters are shifted along the ASCII printable character set (string.printable)
Wrap-around logic ensures shifted characters stay within printable bounds
Decryption reverses the shift to recover the original message
📦 Usage
Run the script.
Enter your message.
Provide a shift value (positive integer).
Choose whether to encrypt or decrypt.
