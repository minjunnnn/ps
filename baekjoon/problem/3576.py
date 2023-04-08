import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n = int(input())
    a = [0] + [*map(int, input().split())]
    a[0] = 0
    prefixsum = [0]

    for i in range(2, n + 1, 2):
        lastBin = i & -i
        curr = prefixsum[i - 2] - prefixsum[i - lastBin]
        a[i - 1] = -curr

        for j in range(1, -1, -1):
            prefixsum.append(prefixsum[-1] + a[i - j])


    print(*a[1:])


if __name__ == "__main__":
    solve()