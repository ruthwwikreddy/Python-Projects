def text_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary_string):
    return ''.join([chr(int(b, 2)) for b in binary_string.split() if len(b) == 8 and all(c in '01' for c in b)])

for _ in range(100):
    choice = input("Enter 'encode' to convert text to binary or 'decode' to convert binary to text: ").strip().lower()

    if choice == 'encode':
        text = input("Enter text to encode: ")
        binary_string = text_to_binary(text)
        print(f"Encoded binary: {binary_string}")
    elif choice == 'decode':
        binary_string = input("Enter a binary string (each byte separated by a space): ")
        text = binary_to_text(binary_string)
        print(f"Decoded text: {text}")
    else:
        print("Invalid choice. Please enter 'encode' or 'decode'.")
        continue
    
    print()
