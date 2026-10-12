# ======================================================================
# Name:        Souroosh Memarian
# Date:        October 12, 2026
# File:        fpa_learning.py
# Description: My version of fpa (learning). Computes a^m mod s by
#              1) writing the exponent m in binary (LSB first),
#              2) building the table a^1, a^2, a^4, a^8, ... mod s,
#              3) multiplying together only the entries whose bit is 1.
#              The printed lists let me see each step by hand.
# ======================================================================

def power2(m):
    """Return the binary digits of m, least significant bit first.
    Example: m = 13 (0b1101) -> [1, 0, 1, 1]
    """
    powers = []
    i = 1                       # bit mask: 1, 2, 4, 8, ...
    while i <= m:
        if i & m:               # is this bit set in m?
            powers.append(1)
        else:
            powers.append(0)
        i <<= 1                 # move the mask to the next bit
    print(powers)               # debug: bits of the exponent
    return powers


def fpa(a, m, s):
    """Compute a^m mod s.
    Uses a^m = product of a^(2^i) over every bit i that is 1 in m.
    """
    powers = power2(m)          # bits of the exponent, LSB first
    n = len(powers)             # number of bits
    modulus = []                # modulus[i] will hold a^(2^i) mod s
    product = 1                 # running answer
    num = a                     # current square: a^(2^i)

    for i in range(n):
        num = num % s                          # reduce so numbers stay small
        modulus.append(num)                    # store a^(2^i) mod s
        if powers[i]:                          # bit i of m is 1 -> use this term
            product = product * modulus[i] % s
        num = num ** 2                         # square: a^(2^(i+1))

    print(modulus)              # debug: table of repeated squares
    print(product)              # debug: result
    return product


# ---- test: compare against Python's own operator ----
fpa(5, 1375, 37)                # my algorithm
print((5**1375) % 37)           # brute force (builds a huge number first)