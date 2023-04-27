import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    s = input()
    BCheck = 0
    RCheck = []
    KIndex = 0

    for idx, i in enumerate(s):
        if i == 'B':
            BCheck += (idx + 1) % 2
        elif i == 'R':
            RCheck.append(idx+1)
        elif i == 'K':
            KIndex = idx + 1

    if  RCheck[0] < KIndex < RCheck[1] and BCheck == 1:
        return "Yes"
    
    return  "No"

if __name__ == "__main__":
    print(solve())
