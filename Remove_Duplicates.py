number = [3,4,5,4,6,5,7,6,8,2,1,3]
unique = []
for num in number:
    if num not in unique:
        unique.append(num)
print(unique)
