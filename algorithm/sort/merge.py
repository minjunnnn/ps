import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def merge(left, right):
	s= []
	i = 0
	j = 0
	while True:
		if i < len(left) and j < len(right):
			if left[i] < right[j]:
				s.append(left[i])
				i+=1
			else:
				s.append(right[j])
				j+=1
		elif i < len(left):
				s.append(left[i])
				i+=1
		elif j < len(right):
				s.append(right[j])
				j+=1
		else:
				break
	return s

def mergeSort(arr):
  if len(arr) < 2:
     return arr
  mid = len(arr) >> 1
  l = mergeSort(arr[:mid])
  r = mergeSort(arr[mid:])
  return merge(l, r)


if __name__ == "__main__":
    print(mergeSort([6,5,3,1,8,7,2,4]))
