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
    product = 1
    num = a
    for i in range(n):
        num = num % s
        modulus.append(num)
        if powers[i]:
            product = product * modulus [i] %s
        num = num ** 2
    print(modulus)
    print (product)
    return product

fpa(5,1375,37)
print((5**1375)%37)