def bsearch(arr, target):
    left = 0
    right = len(arr)-1
    while (left<=right):
        mid = (left+right)//2
        if(target == arr[mid]):
            return mid
        elif(target<arr[mid]):
            right = mid-1
        else:
            left = mid + 1
    return -1

#time complexity: O(log n)
if __name__ == "__main__":
    arr = [-1,0,3,5,9,12]
    target = 90
    print(bsearch(arr,target))