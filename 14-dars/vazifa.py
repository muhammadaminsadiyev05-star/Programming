# n = int(input("n: "))
# if n > 0:
#     print(f"n : {n}")

# 2-massala
# n = int(input("n: "))

# if n>0:
#     n += 1
# else:
#     n -= 2
#     print(n)
    
# n = int(input("N: "))
# if n!=0:
#     if n>0:
#         n += 1
#     else:
#         n -= 2
# else:
#         n = 10
# print(n)

# 3-massala
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# musbat = 0

# if a>0:
#     musbat += 1
# if b>0:
#     musbat += 1
# if c>0:
#     musbat += 1
# print(f"Musbat sonlar soni: {musbat}")

# 4-massala
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# musbat = 0
# manfiy = 0

# if a>0:
#     musbat += 1
# elif a<0:
#     manfiy += 1
# if b>0:
#     musbat += 1
# elif b<0:
#     manfiy += 1
# if c>0:
#     musbat += 1
# elif c<0:
#     manfiy += 1
# print(f"Musbat sonlar soni: {musbat}")
# print(f"Manfiy sonlar soni: {manfiy}")

# 5-massala
# a = int(input("a: "))
# b = int(input("b: "))

# katta = 0
# if a>b:
#     katta = a
# else:
#     katta = b
# print(f"Katta son: {katta}")

# 6-massala
# a = int(input("a: "))
# b = int(input("b: "))

# tartibraqam = 1 if a<b else 2
# # tartibraqam = 0
# # if a<b:
# #     tartibraqam = 1
# # else:
# #     tartibraqam = 2
# print(f"Kichik son tartib raqami: {tartibraqam}")

# 7-massala
a = int(input("a: "))
b = int(input("b: "))

if a<b:
    a, b = b, a
print(f"a: {a}, b: {b}")