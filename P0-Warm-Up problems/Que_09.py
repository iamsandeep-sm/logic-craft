
# ? Print the ASCII value of a character and the character for a given ASCII value.

char = input("User enter any character : ")[0]  # [0] it is used prevent the type error if user type anything instead of character ( single character ) then index[0] will used only except everything will be ignored
# * converting character to the ASCII value ----
asci_value = ord(char)
print(f"The ASCII value of entered character is : {asci_value}")

char_back = chr(asci_value)
print(f"The character for this ASCII value is : {char_back}")

