import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    n = int(input())

    return 26 + (n-4) * 10 + (n-4) ** 2

if __name__ == "__main__":
    for i in range(int(input())):
        print(solve())
