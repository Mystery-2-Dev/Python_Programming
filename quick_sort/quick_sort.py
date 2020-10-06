# L is starting index
# R is ending index
def partition(arr, L, R):
    # i index of smaller element
	i = (L-1)
	pivot = arr[R]

	for j in range(L, R):
		if arr[j] <= pivot:
			i = i+1
            # Swap
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[R] = arr[R], arr[i+1]
	return (i+1)

def quickSort(arr, L, R):
	if len(arr) == 1:
		return arr
	if L < R:

		# p is partitioning index
		p = partition(arr, L, R)
        
        # Sort elements before and after Partition
		quickSort(arr, L, p-1)
		quickSort(arr, p+1, R)

# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end =" ")
    print()

# Driver code to test above
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is :")
    printList(arr)
    # Sort
    quickSort(arr, 0, len(arr) - 1)
    print("Sorted array is :")
    printList(arr) 
