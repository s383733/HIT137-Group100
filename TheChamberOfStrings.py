# Code by Mafuja Akhtar for HIT137 groups assignment2 
# Question2 > Chapter 2: Chamber of Strings

def separate_string(input_string):
    number_substring = ''
    letter_substring = ''

    # Separate the input string into numbers and letters
    for char in input_string:
        if char.isdigit():  # If the character is a number
            number_substring += char
        elif char.isalpha():  # If the character is a letter
            letter_substring += char

    return number_substring, letter_substring

def process_numbers(number_substring):
    even_numbers = []
    for num in number_substring:
        if int(num) % 2 == 0:  # Check if the number is even
            even_numbers.append((num, ord(num)))  # Get ASCII code using ord()

    return even_numbers

def process_uppercase_letters(letter_substring):
    uppercase_letters = []
    for letter in letter_substring:
        if letter.isupper():  # Check if the letter is uppercase
            uppercase_letters.append((letter, ord(letter)))  # Get ASCII code using ord()

    return uppercase_letters

def main():
    # Step 1: Ask for the long string input
    input_string = input("Enter an alphanumeric long string: ")

    # Step 2: Separate the string into number substring and letter substring
    number_substring, letter_substring = separate_string(input_string)

    # Step 3: Print the number and letter substrings
    print(f"Number Substring: {number_substring}")
    print(f"Letter Substring: {letter_substring}")

    # Step 4: Process the even numbers and print them in a single line with ASCII codes
    even_numbers = process_numbers(number_substring)

    # Extract even numbers and their ASCII codes
    even_numbers_str = ', '.join([num for num, _ in even_numbers])
    even_ascii_str = ', '.join([str(ascii_code) for _, ascii_code in even_numbers])
    
    print(f"Even Numbers: {even_numbers_str}")
    print(f"ASCII Codes of Even Numbers: {even_ascii_str}")

    # Step 5: Process the uppercase letters and print them in a single line with ASCII codes
    uppercase_letters = process_uppercase_letters(letter_substring)

    # Extract uppercase letters and their ASCII codes
    uppercase_letters_str = ', '.join([letter for letter, _ in uppercase_letters])
    uppercase_ascii_str = ', '.join([str(ascii_code) for _, ascii_code in uppercase_letters])
    
    print(f"Uppercase Letters: {uppercase_letters_str}")
    print(f"ASCII Codes of Uppercase Letters: {uppercase_ascii_str}")

# Run the main function
if __name__ == "__main__":
    main()
