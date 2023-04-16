import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    n, m = map(int, input().split())
    return "Yes" if n * 100 >= m else "No"


if __name__ == "__main__":
    print(solve())
