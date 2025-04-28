# 7.	Write a Java/C/C++/Python program to perform encryption and decryption using the method of Transposition technique.

def encrypt_transposition(plaintext, key):
    # Create an empty list with 'key' number of strings
    ciphertext = [''] * key

    # Loop through each column
    for column in range(key):
        pointer = column

        while pointer < len(plaintext):
            ciphertext[column] += plaintext[pointer]
            pointer += key  # Move to the next character in the same column

    # Join all strings to get the final ciphertext
    return ''.join(ciphertext)


def decrypt_transposition(ciphertext, key):
    # Calculate number of columns and rows
    num_of_columns = key
    num_of_rows = (len(ciphertext) + key - 1) // key  # Ceiling division
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(ciphertext)

    # Create an empty list with 'num_of_rows' strings
    plaintext = [''] * num_of_rows

    column = 0
    row = 0

    for symbol in ciphertext:
        plaintext[row] += symbol
        row += 1  # move to next row

        if (row == num_of_rows) or (row == num_of_rows - 1 and column >= num_of_columns - num_of_shaded_boxes):
            row = 0
            column += 1

    return ''.join(plaintext)


# Example usage
if __name__ == "__main__":
    message = "WEAREDISCOVEREDFLEEATONCE"
    key = 5

    print("Original Message:", message)

    encrypted = encrypt_transposition(message.replace(" ", ""), key)
    print("Encrypted Message:", encrypted)

    decrypted = decrypt_transposition(encrypted, key)
    print("Decrypted Message:", decrypted)
