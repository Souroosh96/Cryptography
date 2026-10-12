import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "Fast Power Algorithm"))
from fpa import fpa


def fermat_test(p):
    if p > 2:
        if fpa(2, p - 1, p) != 1:
            print("p is composite!")
        else:
            print("Probably prime!")