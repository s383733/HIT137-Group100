# Code by Mafuja Akhtar for HIT137 groups assignment2 
# Question2 > Chapter 2: Caesar Cipher


def caesar_cipher(text, shift):
    result = ""
    
    # Traverse through each character in the input text
    for char in text:
        # Check if it's an uppercase letter
        if char.isupper():
            # Shift the letter and wrap around the alphabet using modulo 26
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if it's a lowercase letter
        elif char.islower():
            # Shift the letter and wrap around the alphabet using modulo 26
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    
    return result

def main():
    # Step 1: Ask for the input text only once
    text = input("Enter the text to decrypt/encrypt: ")

    # Step 2: Loop to allow multiple shift key attempts
    while True:
        shift_input = input("Enter the shift value (or 'q' to quit): ")
        
        # Check if the user wants to quit
        if shift_input.lower() == 'q':
            print("Exiting the program.")
            break
        
        try:
            # Convert the shift input to an integer
            shift = int(shift_input)
        except ValueError:
            print("Please enter a valid integer for the shift value.")
            continue  # Skip to the next iteration and ask again for the shift key
        
        # Step 3: Call the caesar_cipher function and print the result
        shifted_text = caesar_cipher(text, shift)
        print(f"Shifted Text (Shift {shift}): {shifted_text}")

if __name__ == "__main__":
    main()
