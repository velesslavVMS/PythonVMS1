n = int(input("Введите трехзначное число: ")) 
a1 = n % 10
a2 = (n//10)%10
a3 = n//100
s = a1 + a2 + a3
print(a1)
print(a2)
print(a3)
print(s)