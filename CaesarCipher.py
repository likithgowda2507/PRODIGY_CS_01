import string

def caesar_cipher_all_chars(text, shift, mode):
    chars = string.printable  # All printable ASCII characters
    result = ""

    for char in text:
        if char in chars:
            idx = chars.index(char)
            if mode == "encrypt":
                new_idx = (idx + shift) % len(chars)
            elif mode == "decrypt":
                new_idx = (idx - shift) % len(chars)
            result += chars[new_idx]
        else:
            result += char  # Leave unprintable characters unchanged
    return result

def main():
    print("=== Caesar Cipher (All Characters) ===")
    message = input("Enter your message: ")
    
    while True:
        try:
            shift = int(input("Enter shift value (e.g., 3): "))
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        choice = input("Encrypt or Decrypt (E/D)? ").lower()
        if choice in ['e', 'encrypt']:
            mode = "encrypt"
            break
        elif choice in ['d', 'decrypt']:
            mode = "decrypt"
            break
        else:
            print("Invalid choice. Enter E or D.")

    result = caesar_cipher_all_chars(message, shift, mode)
    print(f"\nResult ({mode.title()}ed): {result}")

if __name__ == "__main__":
    main()
