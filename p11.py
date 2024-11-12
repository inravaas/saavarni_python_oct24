# #p11 - Accept a number and find biggest/smallest digit in the number
input_num = int(input("Enter a number to find it's smallest and biggest digit: "))
s=str(input_num) 
print("The biggest digit in the number is: ",max(s)) 
print("The samllest digit in the number is: ",min(s)) 

#OR
# num = int(input("Enter a number:"))
# num_list = []
# count = {}
# while num != 0:
#     digit = num % 10
#     num = num // 10
#     num_list.append(digit)
# i = len(num_list)
# sorted_num_list = sorted(num_list)
# print("The smallest digit in the number is: ",sorted_num_list[0])
# print("The largest digit in the number is: ",sorted_num_list[i-1])