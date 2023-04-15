
import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    n = int(input())
    print('int a;') 
    print('int *ptr = &a;')
    for i in range(1, n):
        print('int ' + '*' * (i+1) + 'ptr' + str(i+1) + ' = ' + '&ptr' + ('' if i == 1 else str(i)) + ';')

if __name__ == "__main__":
    solve()
