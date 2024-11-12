#p6 - Check if the input digit is Composite number
input_number = int(input("Enter a number:"))
count = 0
if input_number > 1:
    for i in range(1,input_number+1):
        if (input_number % i) == 0:
            count += 1
    if count == 2:
        print(f'{input_number} is not a composite number')
    else:
        print(f'{input_number} is a composite number')

elif input_number == 0 or 1:
    print(f'{input_number} is neither prime nor composite number')
else:
    print("Invalid Input")