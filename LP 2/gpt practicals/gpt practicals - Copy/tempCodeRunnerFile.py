def encrypt_message(msg, key):
    cipher = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(msg):
            cipher[col] += msg[pointer]
            pointer += key
    return ''.join(cipher)

def decrypt_message(ciphertext, key):
    num_of_columns = int(len(ciphertext) / key)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_columns
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_columns) or (col == num_of_columns -1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

message = input("Enter message to encrypt: ")
key = int(input("Enter key (number of columns): "))
encrypted = encrypt_message(message, key)
print("Encrypted:", encrypted)
decrypted = decrypt_message(encrypted, key)
print("Decrypted:", decrypted)
