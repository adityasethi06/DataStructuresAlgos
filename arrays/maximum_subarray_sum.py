def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = 0

    for n in arr:
        if current_sum < 0:
            current_sum = 0
        current_sum += n
        max_sum = max(max_sum , current_sum)
    return max_sum

if __name__ == '__main__':
    print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))
    print(max_subarray_sum([-2,1,3,-1,2]))