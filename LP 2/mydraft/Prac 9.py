# 9.	Write a Java/C/C++/Python program to implement RSA algorithm.
# pip install sympy

import random
from sympy import isprime, mod_inverse

# Function to generate a large prime number (used to generate p and q)
def generate_prime():
    while True:
        num = random.randint(100, 999)  # Random 3-digit number
        if isprime(num):
            return num

# Function to generate the RSA keys
def generate_rsa_keys():
    # Generate two large prime numbers p and q
    p = generate_prime()
    q = generate_prime()

    # Compute n = p * q
    n = p * q

    # Calculate Euler's Totient function φ(n) = (p - 1) * (q - 1)
    phi_n = (p - 1) * (q - 1)

    # Choose public exponent e such that 1 < e < φ(n) and e is coprime with φ(n)
    e = random.randrange(2, phi_n)
    while gcd(e, phi_n) != 1:
        e = random.randrange(2, phi_n)

    # Compute private exponent d such that (d * e) % φ(n) = 1
    d = mod_inverse(e, phi_n)

    # Public key is (n, e) and private key is (n, d)
    public_key = (n, e)
    private_key = (n, d)
    
    return public_key, private_key

# Function to compute the greatest common divisor (gcd) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to encrypt a message using the public key
def encrypt(message, public_key):
    n, e = public_key
    # Convert the message to integers (characters to their ASCII values)
    message_int = [ord(char) for char in message]
    # Encrypt each character using the formula: c = m^e % n
    encrypted = [pow(m, e, n) for m in message_int]
    return encrypted

# Function to decrypt a message using the private key
def decrypt(encrypted_message, private_key):
    n, d = private_key
    # Decrypt each character using the formula: m = c^d % n
    decrypted = [chr(pow(c, d, n)) for c in encrypted_message]
    return ''.join(decrypted)

# Example usage
if __name__ == "__main__":
    # Generate RSA keys
    public_key, private_key = generate_rsa_keys()

    print("Public Key:", public_key)
    print("Private Key:", private_key)

    message = "HELLO RSA"
    print("Original Message:", message)

    # Encrypt the message
    encrypted_message = encrypt(message, public_key)
    print("Encrypted Message:", encrypted_message)

    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, private_key)
    print("Decrypted Message:", decrypted_message)
