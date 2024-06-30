import random
n=0
num=random.randint(1,101)
while True:
    user_num=int(input("Вгадайте чісло в діапазоні від 1 до 100\t"))
    if  user_num<num:
        print("Загадкове чісло більше")
        n+=1
    if  user_num>num:
        print("Загадкове чісло меньше")
        n+=1
    if  user_num==num:
        print("Ви виграли")
        n+=1
        print(n)
       






