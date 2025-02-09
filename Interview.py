def decode_string(input_str):
    output_str = ""
    i = 0
    while i < len(input_str):
        char = input_str[i]
        if not char.isalpha():
            raise ValueError(f"Invalid character '{char}' at position {i}. Only alphabets are allowed.")
        
        i += 1
        count = 0
        
        while i < len(input_str) and input_str[i].isdigit():
            count = count * 10 + int(input_str[i])
            i += 1
        
        if count == 0:
            count = 1  # If no number is provided, assume count is 1
        
        output_str += char * count
    
    return output_str

def main():
    while True:
        try:
            input_str = input("Enter the alphabets followed by numbers (e.g., a2b3c4): ")
            result = decode_string(input_str)
            print("Decoded string:", result)
            break
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()
