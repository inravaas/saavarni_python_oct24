# num = int(input("Enter a number:"))
# num_list = []
# count = {}
# # while num != 0:
# #     digit = num % 10
# #     num = num // 10
# #     num_list.append(digit)

# num = str(num)
# for d in num:
#     if d in count:
#         count[d]+=1
#     else:
#         count[d]=1
        
# print("Digit counts:")
# for d, c in count.items():
#     print(f'{d}:{count}')

number = "8088528858"
count = {}
for w in number:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1
print ("Digit Count:")
for w, c in count.items():
    print(f"{w}: {c}")