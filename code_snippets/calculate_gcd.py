# Calculates the Greatest Common Divisor between the 2 numbers.


def gcd(num1, num2):
    div = 1
    i = 1
    while i <= num1 and i <= num2:
        if (num1 % i) == 0 and (num2 % i) == 0:
            div = i
        i += 1
    return div


def main():
    print(gcd(1660, 1590))
    print(gcd(100, 15))
    print(gcd(25, 150))
    print(gcd(2100, 219))


if __name__ == "__main__":
    main()
