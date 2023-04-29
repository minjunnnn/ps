import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    n, a, b = map(int, input().split())
    L = [*map(int, input().split())]
    k = a + b

    for idx, i in enumerate(L, start=1):
        if i == k:
            return idx

if __name__ == "__main__":
    print(solve())
