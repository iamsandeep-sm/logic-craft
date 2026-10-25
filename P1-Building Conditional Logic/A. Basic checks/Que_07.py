
# ? Check whether a character is a vowel, consonant, digit, uppercase letter, lowercase letter or special symbol.

character = input("Enter your character from the keyboard : ")

vowels = "aeiouAEIOU"
if character.isalpha() and len(character) == 1:
    
    if character in vowels:
        print("It is belong to vowel")
    else:
        print("It is consonant")

    if character.isupper():
        print("The character is uppercase")
    elif character.islower():
        print("The character is lowercase")    
    
elif character.isdigit():
    print("The character is digit")
elif len(character) == 1:
    print("This is special symbol")

else:
    print("enter only single character")
    