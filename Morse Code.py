MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

MORSE_TO_TEXT_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        elif char == ' ':
            morse_code += ' '
    return morse_code.strip()

def morse_to_text(morse_code):
    text = ''
    morse_chars = morse_code.split(' ')
    for morse_char in morse_chars:
        if morse_char in MORSE_TO_TEXT_DICT:
            text += MORSE_TO_TEXT_DICT[morse_char]
        elif morse_char == '':
            text += ' '
    return text.strip()

if __name__ == "__main__":
    choice = input("Enter '1' to convert text to Morse code or '2' to convert Morse code to text: ")
    if choice == '1':
        text = input("Enter text to convert to Morse code: ")
        morse_code = text_to_morse(text)
        print("Morse Code:", morse_code)
    elif choice == '2':
        morse_code = input("Enter Morse code to convert to text (use space between letters and '  ' between words): ")
        text = morse_to_text(morse_code)
        print("Text:", text)
    else:
        print("Invalid choice")
