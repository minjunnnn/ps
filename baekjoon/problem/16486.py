import sys
input = lambda: sys.stdin.readline().rstrip()
min_ = float('inf')
INF = sys.maxsize

def solve():
    d1 = int(input())
    d2 = int(input())

    return f"{2 * d1 + 2 * 3.141592 * d2:.6f}"

if __name__ == "__main__":
    print(solve())