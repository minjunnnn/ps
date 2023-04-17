import sys
from bisect import bisect_right, bisect_left
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    n, m = map(int, input().split())
    A = [*map(int, input().split())]
    B = [int(input()) for i in range(n)]
    prefixSum = [0]
    for i in range(m):
        prefixSum.append(prefixSum[-1] + A[i])

    for i in B:
        index = bisect_left(prefixSum, i)
        if index > m:
            print("Go away!")
        else:
            print(index)


if __name__ == "__main__":
    solve()
