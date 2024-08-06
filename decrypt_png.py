import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def decrypt_file(input_file, output_file, key, iv):
    # Print the current working directory
    print("Current working directory:", os.getcwd())

    # Read the encrypted data from the file
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()

    # Create the cipher object and decrypt the data
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    # Write the decrypted data to the output file
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)


# Example usage
key = b'16bytekey1234567'  # 16 bytes for AES-128
iv = b'16byteiv12345678'  # 16 bytes for AES-CBC

input_file = 'encrypted.xpng'
output_file = 'decrypted_output.png'


decrypt_file(input_file, output_file, key, iv)
