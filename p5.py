# p5- Check if the year is Leap year
input_year = int(input("Enter the year to be checked for leap year: "))

if(input_year % 4 == 0):
    print("The year", input_year," is a leap year")
else:
    print("It is not a leap year")
