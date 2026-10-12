# ======================================================================
# Name:        Souroosh Memarian
# Date:        October 12, 2026
# File:        fpa.py
# Description: Fast power algorithm (modular exponentiation).
#              Computes a^m mod s using iterative square-and-multiply,
#              which needs only O(log m) multiplications instead of m.
# ======================================================================

def fpa(a, m, s):
    """Compute a^m mod s via iterative square-and-multiply."""
    result = 1
    base = a % s
    while m > 0:
        if m & 1:                  # lowest bit of m is set
            result = result * base % s
        base = base * base % s     # square for the next bit
        m >>= 1                    # shift to the next bit
    return result % s              # % s handles s == 1

##Testing
print(fpa(5,1375,37))