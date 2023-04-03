import sys

input = lambda: sys.stdin.readline().rstrip()
mii = lambda: map(int, input().split())
miiL = lambda: [*map(int, input().split())]
si = lambda: input()
ii = lambda: int(input())

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def solve():
    n = ii()
    L = miiL()

    l = 0
    r = n-1
    result = 0
    prefixSum = []
    for i in range(len(L)):
        if i == 0:
            prefixSum.append(L[i])
        else:
            prefixSum.append(prefixSum[-1] + L[i])


    for i in range(0, n - 1):
        l = i + 1
        r = n - 1
        l1 = prefixSum[i]
        while l <= r:
            mid = (l + r) // 2
            l2 = prefixSum[mid] - prefixSum[i]
            l3 = prefixSum[n-1] - prefixSum[mid]

            if l3 < l2:
                r = mid - 1
            else:
                l = mid + 1

        f1 = l
        l = f1
        r = n - 1

        while l <= r:
            mid = (l + r) // 2
            l3 = prefixSum[n-1] - prefixSum[mid]

            if l1 < l3:
                l = mid + 1
            else:
                r = mid - 1
        f2 = l
        result += f2 - f1

    print(result)

if __name__ == "__main__":
    solve()
