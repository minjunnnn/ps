import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    a, b = map(int, input().split())
    s = 0
    # 4 8
    while a != b:
        if a > b:
            if a % b == 0:
                n = a - b
                return s + n // b
            k = a // b
            a %= b
        else:
            if b % a == 0:
                n = b - a
                return s + n // a
            k = b // a
            b %= a

        s += k

    return s
if __name__ == "__main__":
    print(solve())
