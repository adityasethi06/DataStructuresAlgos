def sort_arr(arr):
    low, mid = 0, 0
    high = len(arr)-1
    while mid<=high:
        if arr[mid] == 0:
            arr[low], arr[mid] =  arr[mid], arr[low]
            mid += 1
            low += 1
            continue
        if arr[mid] == 2:
            arr[mid], arr[high] =  arr[high], arr[mid]
            high -= 1
            continue
        if arr[mid] == 1:
            mid += 1


if __name__ == '__main__':
    arr = [2,0,1,1,0,0]
    sort_arr(arr)
    print(arr)