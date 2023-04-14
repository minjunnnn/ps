import sys
input = lambda: sys.stdin.readline().rstrip()

def quickSort(l):
	if len(l) <= 1:
		return l
	pivot = l[0]
	
	left = []
	right = []
	
	for i in range(1, len(l)):
		if l[i] < pivot:
			left.append(l[i])
		else:
			right.append(l[i])
	
	return quickSort(left) + [pivot] + quickSort(right)


def solve():
	arr = [15, 22, 13, 27, 12, 10, 20, 25]

	newArr = quickSort(arr)	
	print(newArr)

if __name__ == "__main__":
	solve()

