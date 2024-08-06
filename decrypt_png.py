from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os


def encrypt_file(input_file, output_file, key, iv):
    with open(input_file, 'rb') as f:
        data = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)

    with open(output_file, 'wb') as f:
        f.write(encrypted_data)


def decrypt_file(input_file, output_file, key, iv):
    # Verify if the file exists
    if not os.path.exists(input_file):
        print(f"File does not exist: {input_file}")
        return

    # Read the encrypted data from the file
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()

    # Check if the encrypted data length is a multiple of 16
    if len(encrypted_data) % 16 != 0:
        print("Error: Encrypted data length is not a multiple of 16 bytes.")
        return

    # Create the cipher object and decrypt the data
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    except ValueError as e:
        print(f"Decryption error: {e}")
        return

    # Write the decrypted data to the output file
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)


# Example usage
key = b'16bytekey1234567'  # 16 bytes for AES-128
iv = b'16byteiv12345678'  # 16 bytes for AES-CBC

# Encrypt the file
input_file = 'encrypted.xpng'
encrypted_file = 'encrypted_file.xpng'
encrypt_file(input_file, encrypted_file, key, iv)

# Decrypt the file
output_file = 'decrypted_output.png'
decrypt_file(encrypted_file, output_file, key, iv)
