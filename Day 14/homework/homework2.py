#Python

'''2. Input()-ის გამოყენებით მომხმარებელს შემოატანინეთ მისი სახელი, შემდეგ for loop-ით კი დაპრინტეთ "hello (მომხმარებლის სახელი)" 5 ჯერ.
3. for loop-ის გამოყენებით დაპრინტეთ 20-მდე რიცხვები, თითოეული გაყოფილი 2-ზე.
4. for loop-ის გამოყენებით დაპრინტეთ 15-მდე რიცხვები, თითოეული გამრავლებული 2-ზე.
5. for loop-ის გამოყენებით დაპრინტეთ 10-მდე რიცხვები, თითოეულის კვადრატი.
6. for loop-ის გამოყენებით დაპრინტეთ 10-მდე არსებული ყველა რიცხვის ჯამი, ეს ჯამი უნდა შეინახოს for loop-ის გარეთ შექმნილ ცვლად sum-ში.
 (edited'''

#1
name=input(" anter your name:")
for i in range(5):
    print(name+" hello")




#2

for i in range(20):
    print(i/2)
    




#3

for i in range(15):
    print(i*2)


#4


for i in range(10):
    print(i**2)



#5

sum=0
for i  in range(11):
    sum=sum+i
print(sum)



