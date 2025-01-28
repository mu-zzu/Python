
print("1. Encryption")
print("2. Decryption")
choice = int(input("Enter choice (1 for encryption, 2 for decryption): "))

if choice == 1:
    text = input("Enter text to encrypt: ")
    key = int(input("Enter the key (shift value): "))
    encrypted_text = ""

    for char in text:
        if char.isalpha():  
            shift = key % 26  

            if char.islower():  
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():  # Handle uppercase letters
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char  

    print("Encrypted text:", encrypted_text)

elif choice == 2:
    text = input("Enter text to decrypt: ")
    key = int(input("Enter the key (shift value): "))
    decrypted_text = ""

    for char in text:
        if char.isalpha():  
            shift = key % 26 

            if char.islower():  
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif char.isupper():  
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_text += char  

    print("Decrypted text:", decrypted_text)

else:
    print("Invalid choice. Please enter 1 for encryption or 2 for decryption.")