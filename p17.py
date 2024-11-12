#Program to check if a number is Perfect Square
import math
input_number = float(input("Enter the number"))
root = math.sqrt(input_number)
print("Root = ",root)
if (root * root)==input_number:
    print("{} is a perfect square".format(input_number))
else:
    print("{} is not a perfect square".format(input_number))