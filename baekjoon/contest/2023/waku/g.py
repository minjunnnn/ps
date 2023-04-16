
import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    n, k = map(int, input().split())
    ans = 0

    for i in range(1, n + 1):
        ans += i
        ans %= k

    print(ans)

if __name__ == "__main__":
    solve()
