# 1. 
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
list3 = [100, 200, 300, 400, 500]
print("Max of list1:", max(list1))
print("Max of list2:", max(list2))
print("Max of list3:", max(list3))

# 2. 
print("Min of list1:", min(list1))
print("Min of list2:", min(list2))
print("Min of list3:", min(list3))

# 3. 
list4 = [1, 2, 3, 4, 5]
list5 = [6, 7, 8, 9, 10]
list6 = [11, 12, 13, 14, 15]
print("Length of list4:", len(list4))
print("Length of list5:", len(list5))
print("Length of list6:", len(list6))

# 4. 
print("Sum of list1:", sum(list1))
print("Sum of list2:", sum(list2))
print("Sum of list3:", sum(list3))

# 5. 
list7 = [i for i in range(1, 11)]
list8 = [i for i in range(11, 21)]
list9 = [i for i in range(21, 31)]
list10 = [i for i in range(31, 41)]


print("List7 (1 to 4):", list7[:4])


for i in range(3, 8):
    print("List8 (4 to 8):", list8[i])


print("List9 (9 to 6):", list9[8:5:-1])


i = 0
while i < len(list10):
    print("List10 element:", list10[i])
    i += 1

# 6. 
def analyze_list(user_list):
    if len(user_list) < 5:
        print("List must have at least 5 elements.")
        return
    print("Max:", max(user_list))
    print("Min:", min(user_list))
    print("Sum:", sum(user_list))
    print("Length:", len(user_list))


user_list = [1, 5, 10, 15, 20]
analyze_list(user_list)
