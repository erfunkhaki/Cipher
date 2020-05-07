# encrypts the plaintext using the vigenere cipher by the user entering a message and keyword
def vigenere_encrypt():
    keyword = input("Please enter a keyword: ")
    message = input("Please enter a message you would like to encrypt using the vigenere cipher: ")
    keyword = keyword.lower()
    message = message.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_message = ""
    a = 0
    for x in message:
        if x == " ":
            new_message += " "
            continue
        alphabet_index = alphabet.find(x) + alphabet.find(keyword[a % (len(keyword))])
        if(alphabet_index > 25):
            alphabet_index = alphabet_index % 26
        new_message += alphabet[alphabet_index]
        a += 1
    print("This is the encrypted message: " + new_message)



# decrypts the ciphertext by the user entering a keyword and message
def vigenere_decrypt():
    keyword = input("Please enter a keyword: ")
    message = input("Please enter a message you would like to decrypt from vigenere cipher: ")
    keyword = keyword.lower()
    message = message.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_message = ""
    a = 0
    for x in message:
        if x == " ":
            new_message += " "
            continue
        alphabet_index = alphabet.find(x) - alphabet.find(keyword[a % (len(keyword))])
        if(alphabet_index < 0):
            value = abs(alphabet_index) % 26
            alphabet_index = 26 - value
        new_message += alphabet[alphabet_index]
        a += 1
    print("This is the decrypted message: " + new_message)




