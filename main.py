def boluvchilar_yigindisi(n):
    """n sonining o'zidan tashqari bo‘luvchilari yig‘indisini qaytaradi"""
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s

print("1 dan 1000 gacha do'st sonlar:")
for a in range(1, 1001):
    b = boluvchilar_yigindisi(a)
    if b > a and b <= 1000:
        if boluvchilar_yigindisi(b) == a:
            print(a, "va", b)
