# List Functions:

#1. შექმენით სია, 5 რიცხვით, შემდეგ დაპრინტეთ ამ სიაში შემავალი რიცხვების ჯამი.
#2. შექმენით სია, 5 რიცხვით, შემდეგ დაპრინტეთ ამ სიაში შემავალი რიცხვებიდან უდიდესი.
#3. შექმენით სია, 5 რიცხვით, შემდეგ დაპრინტეთ ამ სიაში შემავალი რიცხვებიდან უმცირესი.
#4. შექმენით სია, 5 რიცხვით, შემდეგ დაპრინტეთ ამ სიის სიგრძე.
#5. შექმენით სია, 5 სტრინგით, შემდეგ .append()-ის მეშვეობით სიის ბოლოში დაამატეთ სასურველი სიტყვა.
#6. შექმენით სია, 5 სტრინგით, შემდეგ .insert()-ის მეშვეობით სიაში სასურველ ინდექსზე დაამატეთ სასურველი სიტყვა.
#7. შექმენით სია, 5 სტრინგით, შემდეგ .pop()-ის მეშვეობით სიიან ამოაგდეთ ინდექსის მეშვეობით რომელიმე სიტყვა.

#1
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
#2
numbers = [1, 2, 3, 4, 5]
print(max(numbers))
#3
numbers = [1, 2, 3, 4, 5]
print(min(numbers))
#4
numbers = [1, 2, 3, 4, 5]
print(len(numbers))
#5
strings = ["apple", "banana", "cherry", "date", "elderberry"]
strings.append("fig")
print(strings)
#6
strings = ["apple", "banana", "cherry", "date", "elderberry"]
strings.insert(2, "kiwi")  # დაამატებს "kiwi" ინდექსზე 2
print(strings)
#7
strings = ["apple", "banana", "cherry", "date", "elderberry"]
strings.pop(1)  # ამოიყვანს "banana" ინდექსიდან 1
print(strings)
