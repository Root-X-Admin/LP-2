import hashlib

text = input("Enter text to hash: ")
result = hashlib.md5(text.encode())
print("MD5 Hash:", result.hexdigest())
