# encrypts the plaintext using the caesar cipher by adding 3 to each letter index
def caesar_cipher_encrypt():
    message = input("Hello, Please enter a message you would like to encrypt to a casear cipher: ")
    message = message.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_message = ""
    for x in message:
        if x == " ":
            new_message += " "
            continue
        alphabet_index = alphabet.find(x) + 3
        if(alphabet_index > 25):
            alphabet_index = alphabet_index % 26
        new_message += alphabet[alphabet_index]
    print("This is the encrypted message: " + new_message)



# decrypts the ciphertext using the caesar cipher by subracting 3 from the letter index
def caesar_cipher_decrypt():
    message = input("Hello, Please enter a message you would like to decrypt from casear cipher ")
    message = message.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_message = ""
    for x in message:
        if x == " ":
            new_message += " "
            continue
        alphabet_index = alphabet.find(x) - 3
        if(alphabet_index < 0):
            value = abs(alphabet_index) % 26
            alphabet_index = 26 - value
        new_message += alphabet[alphabet_index]
    print("This is the decrypted message: " + new_message)

