input_number = int(input("Enter a number to find it's sum of digits: "))
num = input_number
sum = 0
while(num != 0):
    sum = sum + (num % 10)  #Adds the last digit to the sum
    num = int(num / 10) #Removes the last digit from the input_number
    
print(f'The sum of digits of {input_number} is {sum}')
