#1. შექმენით 4 ლისტი და დაპრინტეთ მათში შეყვანილი ცვლადების რაოდენობა.
#2. შექმენთ 3 ლისტი და თითოეულს append ფუნქციის გამოყენებით დაუმატეთ 2-2 ცვლადი.
#3. შექმენით 2 ლისტი. პირველს მე3ე და მე0ე ადგილას დაუმატეთ ცვლადები ხოლო მეორეს მე4ე და მე2ე ადგილას.
#4. შექმენით 1 ლისტი და ორივედან ამოშალეთ 2 ცვლადი pop ფუნქციის გამოყენებით.
#5. შექმენით 3 ცვლადი და დაითვალეთ რამდენი სიმბოლოა თითოეულ ცვლადში.

#1
list1 = [1, 2, 3]
list2 = ["a", "b", "c", "d"]
list3 = [True, False]
list4 = [10, 20, 30, 40, 50]

print(len(list1))  # 3
print(len(list2))  # 4
print(len(list3))  # 2
print(len(list4))  # 5


#2
list5 = []
list6 = []
list7 = []

list5.append("x")
list5.append("y")
list6.append(100)
list6.append(200)
list7.append(True)
list7.append(False)

print(list5)  # ['x', 'y']
print(list6)  # [100, 200]
print(list7)  # [True, False]

#3
list8 = [1, 2, 3]
list9 = [10, 20, 30, 40]

list8.insert(3, "Inserted_3rd")
list8.insert(0, "Inserted_0th")
list9.insert(4, "Inserted_4th")
list9.insert(2, "Inserted_2nd")

print(list8)  # ['Inserted_0th', 1, 2, 3, 'Inserted_3rd']
print(list9)  # [10, 20, 'Inserted_2nd', 30, 40, 'Inserted_4th']

#4
list10 = [5, 10, 15, 20, 25]

popped1 = list10.pop(1)  # 10
popped2 = list10.pop(-1)  # 25

print(list10)  # [5, 15, 20]
print(popped1, popped2)  # 10, 25

#5
var1 = "OpenAI"
var2 = "Language"
var3 = "Model"

print(len(var1))  # 6
print(len(var2))  # 8
print(len(var3))  # 5
