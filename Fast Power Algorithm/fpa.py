def power2(m):
    powers=[]
    i=1
    while i <= m:
        if i & m:
            powers.append(1)
        else:
            powers.append(0)
        i <<= 1
    print(powers)
    return powers

def fpa(a,m,s):
    powers = power2(m)
    n = len(powers)
    modulus = []
    final = []
    product = 1
    num = a
    for i in range(n):
        num = num % s
        modulus.append(num)
        final.append(powers[i] * modulus[i])
        if final[i]:
            product = product * final [i]
        num = num ** 2
    product1 = product % s
    print(modulus)
    print (final)
    print (product)
    print (product1)

fpa(5,1375,37)
print((5**1375)%37)