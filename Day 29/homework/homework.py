#1. შექმენით BMI-ის გამომთვლელი ფუნქცია, რომელიც არამარტო ქულას უპრინტავს მომხმარებელს, არამედ ტექსტურად ეუბნება, თუ რომელ წონით კატეგორიაში არის ის, დავალების შესასრულებლად გამოიყენეთ შემდეგი ფორმულა:
#2. შექმენით ფუნქცია სახელად threeproduct, რომელიც არგუმენტათ იღებს 3 რიცხვს და პრინტავს მათ ნამრავლს.
#3. შექმენით ფუნქცია სახელად greet, რომელიც არგუმენტად იღებს სახელს და პრინტავს მისალმების მესიჯს.
#4. შექმენით ფუნქცია სახელად comparison, რომელიც არგუმენტად იღებს 2 რიცხვს და პრინტავს მათ შორის ჩატარებული 4 არითმეტიკული ოპერაციის შედეგს: <,>,<=,>=.
#5. შექმენით ფუნქცია სახელად agecalc, რომელსაც არგუმენტად გადაეცემა მომხმარებლის ასაკი და პრინტავს, თუ რომელ წელს დაიბადა იგი.



# BMI გამოთვლა დავალების მიხედვით;)
def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obese")

# სამი რიცხვის ნამრავლი ანუ a.b,c ნამრავლი ერთმანეთზე
def threeproduct(a, b, c):
    print(a * b * c)

# მისალმება ანუ როცა მომხმარებელი შემოიტანს თავის სახელს სისტემა მიესალმოს
def greet(name):
    print("Hello, " + name + "!")

# შედარება
def comparison(x, y):
    print(x < y, x > y, x <= y, x >= y)

# დაბადების წლის გამოთვლა (შესით:)
def age



