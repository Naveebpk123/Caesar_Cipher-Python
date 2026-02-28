import string
print("""_____                                           
  / ____|                                          
 | |      __ _  ___  ___  __ _ _ __                
 | |     / _` |/ _ \/ __|/ _` | '__|               
 | |____| (_| |  __/\__ \ (_| | |                  
  \_____|\__,_|\___||___/\__,_|_|                  
  / ____|(_)       | |                             
 | |     _ _ __  __| |__   ___ _ __                
 | |    | | '_ \/ _` | '_ \ / _ \ '__|             
 | |____| | |_) | (_| | | | |  __/ |                
  \_____|_| .__/ \__,_|_| |_|\___|_|                
          | |                                      
          |_|""")
def caesar():
    alphabet = list(string.ascii_lowercase)
    choice = input("decrypt or encrypt?\n").lower()
    message = input("Enter the message\n")
    shift = int(input("Enter the shift number\n"))

    def encrypt(original_text, shift_amount):
        coded_text = ""
        for letter in original_text:
            if letter.lower() in alphabet:
                index = alphabet.index(letter.lower())
                shifted_position = (index + shift_amount) % len(alphabet)
                new_char = alphabet[shifted_position]
                
                if letter.isupper():
                    coded_text += new_char.upper()
                else:
                    coded_text += new_char
            else:
                coded_text += letter
        print(f"Your encrypted message is\n {coded_text}")

    def decrypt(original_text, shift_amount):
        coded_text = ""
        for letter in original_text:
            if letter.lower() in alphabet:
                index = alphabet.index(letter.lower())
                shifted_position = (index - shift_amount) % len(alphabet)
                new_char = alphabet[shifted_position]
                
                if letter.isupper():
                    coded_text += new_char.upper()
                else:
                    coded_text += new_char
            else:
                coded_text += letter
        print(f"Your decrypted message is\n {coded_text}")

    if choice == "decrypt":
        decrypt(message, shift)
    elif choice == "encrypt":
        encrypt(message, shift)

direction = input("Welcome to Caesar Cipher. \nType quit to exit. \nClick Enter to start")
if not direction == "quit":
    while True:
        caesar()
        choice2 = input("Type quit to exit.\nType Enter to continue")
        if choice2 == "quit":
            break








