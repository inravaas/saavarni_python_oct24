#p10 - Accept a number and find count the number of digits in it.

input_num = int(input("Enter a number to find the number of digits in it: "))
count = 0
num = input_num
while (num != 0):
    num = num // 10
    count = count + 1
print(f'There are {count} digits in {input_num}')