from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def encrypt_file(file_name, password):
    key = password.ljust(32).encode()[:32]  # Ensure the key is 32 bytes
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv

    with open(file_name, 'rb') as file:
        plaintext = file.read()
    
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    with open(file_name + '.enc', 'wb') as file:
        file.write(iv + ciphertext)

def decrypt_file(file_name, password):
    key = password.ljust(32).encode()[:32]
    
    with open(file_name, 'rb') as file:
        iv = file.read(16)  # Read the IV
        ciphertext = file.read()
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    with open(file_name[:-4], 'wb') as file:  # Remove '.enc' to save the original
        file.write(plaintext)

if __name__ == "__main__":
    choice = input("Do you want to (e)ncrypt or (d)ecrypt a file? ")
    file_name = input("Enter the file name: ")
    password = input("Enter the password: ")
    
    if choice.lower() == 'e':
        encrypt_file(file_name, password)
        print("File encrypted successfully!")
    elif choice.lower() == 'd':
        decrypt_file(file_name, password)
        print("File decrypted successfully!")
    else:
        print("Invalid option!")
