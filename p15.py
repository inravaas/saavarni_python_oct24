#p15 - Find the second smallest digit in the number
num = int(input("Enter a number:"))
num_list = []
count = {}
while num != 0:
    digit = num % 10
    num = num // 10
    num_list.append(digit)

sorted_num_list = sorted(num_list)
print("The second smallest digit in the number is: ",sorted_num_list[1])