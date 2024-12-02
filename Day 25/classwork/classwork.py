# მომხმარებლისთვის შემოტანა
number1 = float(input("შეიტანეთ პირველი რიცხვი: "))
number2 = float(input("შეიტანეთ მეორე რიცხვი: "))
operator = input("შეიტანეთ ოპერატორი (+, -, *, /): ")

# გამოთვლის შედეგი
if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    if number2 != 0:
        result = number1 / number2
    else:
        result = "გაყოფა 0-ით შეუძლებელია"
else:
    result = "არასწორი ოპერატორი"

# შედეგის გამოყვანა
print("სწორად გამოთვლილი შედეგი:", result)





#2
# პაროლის სახელი
correct_password = "password"
user_input = ""

# while ციკლი რომელიც შესრულდება მანამდე, სანამ სწორი პაროლი არ შევა
while user_input != correct_password:
    user_input = input("გთხოვთ შეიტანოთ პაროლი: ")

print("პაროლი სწორია! მიესალმებით.")
