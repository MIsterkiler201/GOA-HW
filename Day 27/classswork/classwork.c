//1. შექმენით სამი პარაგრაფი, სამივეს შეუცვალეთ ფერი სხვადასხვა მეთოდით.
# .strip() - შლის ცარიელ ადგილებს ტექსტის დასაწყისსა და ბოლოში.
text1 = "  Hello World!  "
print(text1.strip())  # -> "Hello World!"

# .replace() - ცვლის ტექსტის ნაწილს.
text2 = "I like Python"
print(text2.replace("like", "love"))  # -> "I love Python"

# .split() - ყოფს ტექსტს ნაწილებად.
text3 = "apple,banana,cherry"
print(text3.split(","))  # -> ['apple', 'banana', 'cherry']
