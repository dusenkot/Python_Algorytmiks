def insertionSort(arr):
    if (n := len(arr)) <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
        arr[j+1]=key



arr = [24, 7, 15, 34, 5, 18]
insertionSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print(arr[i])





