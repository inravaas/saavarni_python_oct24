my_string = input('Enter a place name: ')

print(f'Type of {my_string} is {type(my_string)}')

for character in my_string: # for each loop
    print(f'{character}, Type={type(character)}')

first_character = chr(my_string[0])
print(f'first charatcer = {first_character}, Type = {type(character)}')