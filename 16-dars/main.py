# while

# qadam = salom = 1

# while qadam <= 10:
#     print(f"Qadam raqami: {qadam}")
#     qadam += 1

# a = 1
# s = int(input("son kiriting: "))
# while a <= s:
#     print(f"{a} - salom")
#     a  += 1

# i = 1 
# n = int(input("son kiriting: "))
 
# while i <= 10:
#     b = n * i
#     print(f"{n} x {i} = {b}")
#     i += 1
    
# gisht = int(input("Gishtlar sonini kiriting: "))
# sigim = int(input("1 ta aravaga sigadigan gisht soni: "))

# arava = 0
# yigildi = 0

# while yigildi < gisht:
#     yigildi += sigim
#     arava += 1

# print("tashishlar soni: ", arava)

# fruit = ["apple", "banana", "orange", "strawbery"]

# i = 0

# while i < len(fruit):
#     print(fruit[i])
#     i += 1
    
# n = int(input("n: "))
# i = 1
# sum_div = 0
# divisors = []
# while i <= n:
#     if n % i == 0:
#         divisors.append(i)
#         sum_div += i
#     i += 1

# print("Bo'luvchilar:", *divisors)
# print(f"{n} ning bo'luvchilar yig'indisi: {sum_div}")
    
# n = int(input('n: '))
# j = 1 
# while j <= n:
#     i = 1
#     sum = 0 
#     while i < j:
#         if j % i == 0:
#             sum += i
            
#         i += 1
#     if sum == j:
#         print(j)
#     j += 1
    
#     print(f"{n}sonning boluvchilari yigindisi: {sum}")
    
#     if sum  == n:
#         print("Mukammal son")
#     else:
#         print("Mukammal son emas")

saqlangan_parol = "12345"   

k  = int(input("parol kiriting: "))             

while k != saqlangan_parol:
    k = input("Parolni kiriting: ")
    if k != saqlangan_parol:
        print("Xato! Qayta urinib ko‘ring./n")

print("Parol to‘g‘ri! Xush kelibsiz!")
