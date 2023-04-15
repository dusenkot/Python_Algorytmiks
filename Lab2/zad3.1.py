def bubble_Sort(arr):
    n=len(arr)
    swapped= False
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                swapped=True
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
        if not swapped:
            return
arr=[24,7,15,34,5,18]
bubble_Sort(arr)
print("sorted array is:")
for i in range(len(arr)):
    print(arr[i],end=" ")




