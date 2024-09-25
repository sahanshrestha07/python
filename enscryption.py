import random
import string


chars =" " + string.whitespace + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)


#encrypt
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text :
    index = chars.index(letter)
    cipher_text += key[index]
print(f"original message:{plain_text}")
print(f"encrypted_text : {cipher_text}")

decrypt_value = input("do you want to decrypt the message(y/n)")

if decrypt_value == "y":
    decrypted_message = ""
    for letter in cipher_text:
        index = key.index(letter)
        decrypted_message += chars[index]
    print(f"decrypted_text : {decrypted_message}")

