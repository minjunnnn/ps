import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    a, b = map(int, input().split())

    c = a ^ b

    print(c)

if __name__ == "__main__":
    solve()
