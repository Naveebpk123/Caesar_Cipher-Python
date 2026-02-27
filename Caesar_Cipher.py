import string

def caesar():
    alphabet = list(string.ascii_lowercase)
    choice = input("decrypt or encrypt?\n").lower()
    message = input("Enter the message\n").lower()
    shift = int(input("Enter the shift number\n"))

    def encrypt(original_text, shift_amount):
        coded_text = ""
        for letter in original_text:
            if letter in alphabet:
                shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
                coded_text += alphabet[shifted_position]
            else:
                coded_text += letter
        print(f"Your encrypted message is:\n{coded_text}")

    def decrypt(original_text, shift_amount):
        decoded_text = ""
        for letter in original_text:
            if letter in alphabet:

                shifted_position = (alphabet.index(letter) - shift_amount) % len(alphabet)
                decoded_text += alphabet[shifted_position]
            else:
                decoded_text += letter
        print(f"Your decrypted message is:\n{decoded_text}")

    if choice == "decrypt":
        decrypt(message, shift)
    elif choice == "encrypt":
        encrypt(message, shift)

print("Welcome to Caesar Cipher.")
direction = input("Type 'quit' to exit or press Enter to start: ").lower()

if direction != "quit":
    while True:
        caesar()
        choice2 = input("\nType 'quit' to exit or press Enter to continue: ").lower()
        if choice2 == "quit":
            break






