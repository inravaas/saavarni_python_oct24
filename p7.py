#p7 - Check if the character is only a alpha-numeric
input_char = input("Enter a character: ")
if input_char.isalnum() == True:
    print(f"{input_char} is an alpha-numeric")
else:
    print(f"{input_char} is not alpha-numeric")