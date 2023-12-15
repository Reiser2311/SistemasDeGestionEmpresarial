c0 = int(input())
pasos = 0

while c0 > 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = c0 * 3 + 1
    print(c0)
    pasos += 1
    
print("Pasos: ", pasos)