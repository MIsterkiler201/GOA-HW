#1. შექმენი ცვლადი, სადაც შეინახავ სტრინგს, შემდეგ გამოიტანე იმ სტრინგის მეორე ასო.
#2. შექმენით 2 int ტიპის ცვლადი და გამოიტანეთ მათი ჯამი.
#3. შექმენით 2 str ტიპის ცვლადი და გამოიტანეთ მათი შეერთებული ვერსია (ასევე კომენტარის სახით აღწერეთ რა არის კონკატენაცია).
#4. შექმენით 2 int ტიპის ცვლადი და გამოიტანეთ მათი განაყოფი, შემდეგ კი ახსენით რატომ გამოიტანა floatი და რა ქვია ამ convert'ს (implicit or explicit)
#5. გაიხსენეთ ყველა შედარების ოპერატორი და ჩამოწერეთ ყველაზე 1 მაგალითი
#6. შეურიეთ შედარების ოპერატორები და მათემატიკური ოპერაციები (მაგ: 5 + 5 == 8  + 2)
#7. გაიხსენეთ ლოგიკური ოპერატორი და ჩამოწერეთ ყველა კომბინაცია რაც საჭიროა (სულ უნდა იყოს რვა, გაიხსენეთ ნასწავლიდან)
#8. შეურიეთ ერთმანეთს ლოგიკური და შედარების ოპერატორები და მოიყვანეთ 5 მაგალითი
#9. შექმენით for loop'ი 1-დან 10-მდე რიცხვების დასაბეჭდად.
#10. შექმენით რიცხვების list'ი, შექმენით for loop'ი list'ის რიცხვების ჯამის გამოსათვლელად.
#11. შექმენით for loop'ი თითოეული სიმბოლოს დასაბეჭდად სტრინგში -> "Hello, World!".
#12. შექმენით while loop'ი 1-დან 10-მდე რიცხვების დასაბეჭდად.
#13. შექმენით while loop'ი რომელიც დათვლის რიცხვებს 1დან 100მდე თუმცა გამოტოვებს რიცხვებს 50დან 60მდე.
#14. შექმენით while loop'ი, რომელიც დაიწყებს რიცხვების შეკრებას 1-დან, სანამ ჯამი არ გაუტოლდება 50-ს.


#1
string = "Hello"
print(string[1])  # Output the second letter (indexing starts at 0)

#2
num1 = 5
num2 = 10
print(num1 + num2)  # Output the sum

#3
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)  # Concatenation is the process of joining two strings together

#4
int1 = 10
int2 = 3
print(int1 / int2)  # Output the division
# Explanation: Division in Python with '/' always produces a float, even if the numbers are integers. This is an example of implicit type conversion.


#5
#== (equal to)
#!= (not equal to)
#> (greater than)
#< (less than)
#>= (greater than or equal to)
#<= (less than or equal to)

#6
print(5 + 5 == 8 + 2)  # True (since both sides are equal)

#7
#and
#or
#not
True and True    # True
True and False   # False
False and True   # False
False and False  # False
True or True     # True
True or False    # True
False or True    # True
False or False   # False

#8
print(5 > 3 and 2 < 4)  # True (both conditions are true)
print(5 == 5 or 2 > 4)  # True (one condition is true)
print(not 7 == 7)       # False (negation of true)
print(3 <= 5 and 4 == 4)  # True (both conditions are true)
print(6 > 8 or 3 == 3)  # True (second condition is true)

#9
for i in range(1, 11):
    print(i)

#10
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = 0
for num in numbers:
    sum_of_numbers += num
print(sum_of_numbers)

#11
for char in "Hello, World!":
    print(char)

#12
i = 1
while i <= 10:
    print(i)
    i += 1

#13
i = 1
while i <= 100:
    if 50 <= i <= 60:
        i += 1
        continue  # Skip numbers between 50 and 60
    print(i)
    i += 1


#14
sum = 0
i = 1
while sum < 50:
    sum += i
    i += 1
print(sum)
