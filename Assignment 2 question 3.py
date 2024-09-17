#Define a function to decrypt the code based off the encryption function

def decrypt(text, key):
    decrypted_text = ""

    for char in text:
        if char.isalpha():
            shifted = ord(char) - key   #This reverses the original encryption which is ord(char) + key

            if char.islower():  #Ensures that lower case characters remain lowercase
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():    #Ensures that uppercase characters remain uppercase
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26

            decrypted_text += chr(shifted)  #Adds decrypted characters to the new decrypted text as the function iterates through the encrypted text
        else:
            decrypted_text += char

    return decrypted_text

# Start with key = 1 and loop until valid Python code is decrypted
key = 13
encrypted_code = """
tybony_inevnoyr = 100

zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr 
    ybpny_inevnoyr = 5 
    ahzoref = [1, 2, 3, 4, 5]

    juvyr ybpny_inevnoyr > 0: 
        vs ybpny_inevnoyr % 2 == 0: 
            ahzoref.erzbir(ybpny_inevnoyr) 
        ybpny_inevnoyr = 1

    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg(): 
    ybpny_inevnoyr = 10 
    zl_qvpg['xrl4'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony(): 
    tybony tybony_inevnoyr 
    tybony_inevnoyr += 10

sbe v va enatr(5): 
    cevag(v)
    v += 1

vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10: 
    cevag("Pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanel!")

cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
"""
decrypted_code = decrypt(encrypted_code, key) #Decryption of original encrypted code
print(decrypted_code)


# Finally, the original code (decrypted code) after fixing errors:
global_variable = 100

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers(numbers):  # Add parameter 'numbers'
    global global_variable 
    local_variable = 5 
    numbers = list(numbers)  # Convert set to list
    while local_variable > 0: 
        if local_variable % 2 == 0: 
            numbers.remove(local_variable) 
        local_variable -= 1  # Decrement local_variable
    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
new_set = set(process_numbers(numbers=my_set))

def modify_dict(): 
    local_variable = 10 
    my_dict['key4'] = local_variable

modify_dict()  # Remove argument from modify_dict()

def update_global(): 
    global global_variable 
    global_variable += 10

update_global() #Call the function to ensure global value is updated before printing

for i in range(5): 
    print(i)
    # Remove i += 1 since it's redundant in this loop

if my_set is not None and my_dict['key4'] == 10:
    print("Condition met!")

if 5 not in my_dict:
    print("5 not found in the dictionary!")

print(global_variable) 
print(my_dict) #Prints the new dictionary with 4th key added and corresponding value
print(new_set) #Prints the new set of processed numbers