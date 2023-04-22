import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    n, h = map(int, input().split())
    L = [int(input()) for i in range(n)]
    prefixSum = [0] * (h + 2)

    for idx, i in enumerate(L):
        if idx % 2 == 0:
            prefixSum[1] += 1
            prefixSum[i+1] -= 1
        else:
            prefixSum[h+1] -= 1
            prefixSum[h+1-i]+=1

    for i in range(1, h+2):
        prefixSum[i] += prefixSum[i-1]

    min_ = min(prefixSum[1:-1])
    count = prefixSum[1:-1].count(min_)

    print(min_, count)

    



if __name__ == "__main__":
    solve()
