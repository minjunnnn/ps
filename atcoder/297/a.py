import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    n, d = map(int, input().split())
    L = [*map(int, input().split())]

    for i in range(len(L)-1):
        if L[i+1] - L[i] <= d:
            return L[i+1]

    return -1

if __name__ == "__main__":
    print(solve())
