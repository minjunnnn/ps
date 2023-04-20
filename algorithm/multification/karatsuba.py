import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def karatsuba(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y

    n = max(len(str(x)), len(str(y)))
    n2 = n // 2

    a = x // (10 ** (n2))
    b = x % (10 ** (n2))
    c = y // (10 ** (n2))
    d = y % (10 ** (n2))

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a+b, c+d) - ac - bd

    return ac * (10 **  (2*n2)) + ad_bc * (10 **n2) + bd

def solve():
    a, b = map(int, input().split())
    result = karatsuba(a, b)

    print(result)

if __name__ == "__main__":
    solve()
