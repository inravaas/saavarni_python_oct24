import random

player_number = int(input("Enter a number of your choice between 0 to 9: "))

# system_number = int(random(random.seed(0), 10))  #seed means start value -> [0,10)= 0 to 9
system_number = random.randint(0,10)
print(system_number)

if player_number == system_number:
    print("You are crorepati")
else:
    print("You are roadpati")