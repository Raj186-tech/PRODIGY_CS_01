def get_cipherletter(new_key, letter):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letter in alpha:
        return alpha[(alpha.index(letter) + new_key) % len(alpha)]
    else:
        return letter

def encrypt(key, message):
    message = message.upper()
    result = ""

    for letter in message:
        if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result += get_cipherletter(key, letter)
        else:
            result += letter

    return result

def decrypt(key, message):
    message = message.upper()
    result = ""

    for letter in message:
        if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result += get_cipherletter(-key, letter)
        else:
            result += letter

    return result

def main():
    print("Caesar Cipher Program")
    print("---------------------")

    while True:
        mode = input("\nChoose mode (encrypt/decrypt): ").lower()

        if mode == "encrypt" or mode == "decrypt":
            message = input("Enter your message: ")
            key = int(input("Enter the shift value (1-25): "))

            if mode == "encrypt":
                result = encrypt(key, message)
                print(f"Encrypted message: {result}")
            else:
                result = decrypt(key, message)
                print(f"Decrypted message: {result}")

        elif mode == "quit":
            print("Goodbye!")
            break

        else:
            print("Invalid mode. Please choose 'encrypt', 'decrypt', or 'quit'.")

if __name__ == "__main__":
    main()