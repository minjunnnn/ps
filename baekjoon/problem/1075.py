import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    n = int(input())
    f = int(input())

    lastTwoDigit = n % 100

    n -= lastTwoDigit

    for i in range(0, 100):
        if (n + i) % f == 0:
            if len(str(i)) == 1:
                return '0' + str(i)
            else:
                return i

if __name__ == "__main__":
    print(solve())
