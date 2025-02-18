#1. ფუნქცია უნდა პრინტავდეს დამარცვლილ სახელს, შებრუნებულად.
#2. შექმენით ფუნქცია, რომელსაც გადაეცემა 5 არგუმენტი, 5 ინფუთით მომხარებელს აარჩევინეთ ნებისმიერი რიცხვი, ბოლოს კი დაუპრინტეთ ამ რიცხვებისაგან შემდგარი სია.
#3. შექმენით ფუნქცია რომელიც არგუმენტად აიღებს თქვენს შექმნილ სიას, რომელშიც იქნება მინიმუმ 5 რიცხვი და დაპრინტავს ამ სიისის მაქსიმალურ რიცხვს, მინიმალურ რიცხვს, რიცხვების ჯამს და სიის სიგრძეს.


# 1. ფუნქცია, რომელიც პრინტავს დამარცვლილ სახელს, შებრუნებულად
def print_reversed_name(name):
    reversed_name = '-'.join(name[::-1])
    print(reversed_name)

# გამოყენება:
print_reversed_name("მიხეილი")  # ილიხემ-ი


# 2. ფუნქცია, რომელიც აგროვებს 5 რიცხვს და ბეჭდავს სიას
def collect_numbers():
    numbers = []
    for i in range(5):
        num = int(input(f"შეიყვანეთ {i+1}-ე რიცხვი: "))
        numbers.append(num)
    print("თქვენი რიცხვების სია:", numbers)
    return numbers

# გამოყენება:
numbers_list = collect_numbers()


# 3. ფუნქცია, რომელიც პრინტავს მინიმუმს, მაქსიმუმს, ჯამს და სიის სიგრძეს
def analyze_list(numbers):
    print("მაქსიმალური რიცხვი:", max(numbers))
    print("მინიმალური რიცხვი:", min(numbers))
    print("რიცხვების ჯამი:", sum(numbers))
    print("სიის სიგრძე:", len(numbers))

# გამოყენება:
analyze_list(numbers_list)
