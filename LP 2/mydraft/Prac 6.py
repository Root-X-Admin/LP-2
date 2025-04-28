# 6.	Write a Java/C/C++/Python program that contains a string (char pointer) with a value \Hello World’. The program should AND or and XOR each character in this string with 127 and display the result.

# The string
text = "Hello World"

print("Original String:", text)
print("\nCharacter\tASCII\tAND 127\tXOR 127\t")
print("-" * 39)

for char in text:
    ascii_val = ord(char)         # Get ASCII value
    and_val = ascii_val & 127      # Perform AND with 127
    xor_val = ascii_val ^ 127      # Perform XOR with 127

    print(f"{char}\t\t{ascii_val}\t{and_val}\t{xor_val}\t")
