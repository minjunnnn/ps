
import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    n = int(input())
    materials = input().split()
    mS = set(materials)
    count = 0
    for i in mS:
        if i[-6:] == 'Cheese':
            count += 1

    return "yummy" if count >= 4 else "sad"

if __name__ == "__main__":
    print(solve())
