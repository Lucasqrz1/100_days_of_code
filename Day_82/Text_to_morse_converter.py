#!/usr/bin/env python3
"""
Morse Code Converter
Converts text strings to Morse code and vice versa
"""

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', 
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

# Reverse dictionary for decoding
REVERSE_MORSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    """Convert text to Morse code"""
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        elif char == ' ':
            morse_code.append('/')  # Space between words
        else:
            morse_code.append('?')  # Unknown character
    return ' '.join(morse_code)

def morse_to_text(morse):
    """Convert Morse code to text"""
    # Split by spaces to get individual morse characters
    morse_chars = morse.split(' ')
    text = []
    
    for morse_char in morse_chars:
        if morse_char in REVERSE_MORSE_DICT:
            text.append(REVERSE_MORSE_DICT[morse_char])
        elif morse_char == '':
            continue  # Skip empty strings from multiple spaces
        else:
            text.append('?')  # Unknown morse code
    
    return ''.join(text).replace('/', ' ')

def display_morse_table():
    """Display the Morse code reference table"""
    print("\nMorse Code Reference Table:")
    print("=" * 30)
    
    # Letters
    print("LETTERS:")
    for i, (char, morse) in enumerate(list(MORSE_CODE_DICT.items())[:26]):
        print(f"{char}: {morse:6}", end="  ")
        if (i + 1) % 4 == 0:
            print()
    
    print("\n\nNUMBERS:")
    for char, morse in list(MORSE_CODE_DICT.items())[26:36]:
        print(f"{char}: {morse:6}", end="  ")
    
    print("\n\nPUNCTUATION:")
    for char, morse in list(MORSE_CODE_DICT.items())[36:]:
        print(f"'{char}': {morse:8}", end="  ")
    print("\n")

def main():
    """Main program loop"""
    print("🔤 MORSE CODE CONVERTER 🔤")
    print("=" * 40)
    
    while True:
        print("\nOptions:")
        print("1. Convert text to Morse code")
        print("2. Convert Morse code to text")
        print("3. Show Morse code table")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            text = input("\nEnter text to convert: ")
            if text:
                morse = text_to_morse(text)
                print(f"\nOriginal: {text}")
                print(f"Morse:    {morse}")
            else:
                print("Please enter some text.")
                
        elif choice == '2':
            morse = input("\nEnter Morse code (use spaces between letters, '/' for word spaces): ")
            if morse:
                text = morse_to_text(morse)
                print(f"\nMorse:    {morse}")
                print(f"Text:     {text}")
            else:
                print("Please enter some Morse code.")
                
        elif choice == '3':
            display_morse_table()
            
        elif choice == '4':
            print("\nGoodbye! 73s (Best wishes in Morse code)")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()