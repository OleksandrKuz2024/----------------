import string
import random
password=""
n= int(input("Введіть довжину пароля\t"))
for i in range(1):
    symbol_class = input("Введіть клас символів для пароля.Великі букви - upp,малі букви - low,спецсимволи - punct, цифри - dig\t")
    if symbol_class.lower()=="upp":
        for i in range(n):
            b = string.ascii_uppercase
            password+=random.choice(b)
    if symbol_class.lower()=="low":    
        for i in range(n):
            b = string.ascii_lowercase
            password+=random.choice(b)
    if symbol_class.lower()=="punct": 
        for i in range(n): 
            b = string.punctuation  
            password+=random.choice(b)
    if symbol_class.lower()=="dig":
        for i in range(n):
            b = string.digits
            password+=random.choice(b)
print(password)

    














