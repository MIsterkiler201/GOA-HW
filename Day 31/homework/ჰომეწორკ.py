#1. შექმენით ფუნქცია, რომელიც იღებს რაიმე რიცხვს და აბრუნებს მასზე 5'ით მეტს.

#2. შექმენით ფუნქცია, რომელიც იღებს ორ integer'ს და აბრუნებს მათ ნამრავლს

#3. შექმენით ფუნქცია, რომელიც იღებს string'ს ამ string'ის სიგრძეს (გამოიყენეთ ფუნქცია len(), ახალი მასალაა).

#4. შექმენით ფუნქცია, რომელიც იღებს string'ების list'ს და აბრუნებს ამ string'ების სიგრძეების list'ს (გამოიყენეთ ფუნქცია len()).

#5. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს True-ს თუ ის არის Palindrome (ანუ იგივენაირად იკითხება მარცნიდანაც და მარჯვნიდანაც მაგალითად: "wow") და სხვა შემთხვევაში False-ს.

#6. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს იმავე string'ს uppercase'ში. 
#(მაგალითად: input: "Hello World". output: "HELLO WORLD".


# 1. ფუნქცია, რომელიც რიცხვს უმატებს 5-ს
def add_five(number):
    return number + 5
# 1
print(add_five(10))  # 15


# 2. 
def multiply(a, b):
    return a * b
#

# 2
print(multiply(4, 5))  # Output: 20


# 3. 

def string_length(s):
    return len(s)

# 3
print(string_length("hello"))  #  5

#4
def list_of_lengths(strings):
    return [len(s) for s in strings]

print(list_of_lengths(["hello", "world", "Python"]))  # Output: [5, 5, 6]

# 5
print(is_palindrome("wow"))  # Output: True
print(is_palindrome("hello"))  # Output: False

# 6
print(to_uppercase("Hello World"))  # Output: "HELLO WORLD"

# 5. 
def is_palindrome(s):
    return s == s[::-1]

# 6. ფუნქცია, რომელიც string-ს გარდაქმნის uppercase'ში
def to_uppercase(s):
    return s.upper()
