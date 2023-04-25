import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    n = int(input())
    L = [*map(int, input().split())]

    L.sort()

    a = max(L[0] * L[1], L[n-1] * L[n-2])

    return a

if __name__ == "__main__":
    for i in range(int(input())):
        print(solve())
