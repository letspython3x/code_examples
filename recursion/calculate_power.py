#  Recursive power


def power(base, exp):
    if exp == 1:
        return base
    if exp != 1:
        return base * power(base, exp - 1)
