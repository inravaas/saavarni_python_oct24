# To print the math table of number for multiples upto 20

input_number = int(input("Enter a number to print its Math table: "))

for i in range(1,21):
    print('%2d * %02d = %3d'%(input_number, i, input_number*i))