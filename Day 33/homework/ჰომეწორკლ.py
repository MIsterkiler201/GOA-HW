#1. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვს და აბრუნებს მის კვადრატს.
#2. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს ორ რიცხვს და აბრუნებს მათ ჯამს.
#3. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვთა სიას და აბრუნებს ყველაზე პატარას.
#4. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვს და ამოწმებს, არის თუ არა ის დადებითი.
#5. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვთა სიას და აბრუნებს მათ ჯამს.

# 1. 
def square(num):
    return num ** 2

# 2.
def add(a, b):
    return a + b

# 3. 
def find_min(numbers):
    return min(numbers) if numbers else None  

# 4.
def is_positive(num):
    return num > 0

# 5.
def sum_list(numbers):
    return sum(numbers)

