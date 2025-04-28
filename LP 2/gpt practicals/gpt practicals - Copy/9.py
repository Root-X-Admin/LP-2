from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

message = input("Enter message to encrypt: ")
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

print("Private Key:")
print(private_key.decode())
print("\nPublic Key:")
print(public_key.decode())

public_key_obj = RSA.import_key(public_key)
encryptor = PKCS1_OAEP.new(public_key_obj)
encrypted = encryptor.encrypt(message.encode())
print("\nEncrypted:", binascii.hexlify(encrypted))

private_key_obj = RSA.import_key(private_key)
decryptor = PKCS1_OAEP.new(private_key_obj)
decrypted = decryptor.decrypt(encrypted)
print("\nDecrypted:", decrypted.decode())
