import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    n = int(input())

    sqrtN = int(n ** 0.5)
    ssqrtN = int(sqrtN ** 0.5)

    k = [True] * (sqrtN + 1)

    for i in range(2, ssqrtN + 1):
        if k[i]:
            for j in range(i + i, sqrtN + 1, i):
                k[j] = False
    primeSet = []
    for idx, i in enumerate(k):
        if i and idx >= 2:
            primeSet.append(idx)

    primeLen = len(primeSet)

    count = 0

    for i in range(primeLen):
        for j in range(i+1, primeLen):
            for z in range(j+1, primeLen):
                if (primeSet[i] ** 2) * primeSet[j] * (primeSet[z] ** 2) <= n:
                    count += 1
                else:
                    break
    
    return count

if __name__ == "__main__":
    print(solve())
