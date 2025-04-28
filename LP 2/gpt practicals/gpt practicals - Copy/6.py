s = input("Enter a string: ")

print("Original String:", s)

print("\nAfter XOR with 127:")
for c in s:
    print(chr(ord(c) ^ 127), end='')

print("\n\nAfter AND with 127:")
for c in s:
    print(chr(ord(c) & 127), end='')
