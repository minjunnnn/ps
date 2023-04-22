import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    a, b = map(int, input().split())

    return (a + b) * (a - b)

if __name__ == "__main__":
    print(solve())
