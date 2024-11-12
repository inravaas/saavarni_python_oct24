#p12 - Find sum of Even/Odd digits in the number

input_number = int(input("Enter a number: "))
reverse_num = 0

#for reversing the input_number
while (input_number != 0): 
	reverse_num = (reverse_num * 10) + (input_number % 10) 
	input_number //= 10

sum_odd = 0
sum_even = 0
i = 1
while (reverse_num != 0):    #i is used for pointing each digit in the number
	if (i % 2 == 0): 
		sum_even += reverse_num % 10
	else: 
		sum_odd += reverse_num % 10
	reverse_num //= 10
	i += 1

print("Sum odd =", sum_odd) 
print("Sum even =", sum_even) 
