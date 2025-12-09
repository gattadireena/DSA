#Linear search
def search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key: 
            return i
    return -1

#time complexity: O(N)
if __name__ == "__main__":
    arr = [1,2,3,5,0,7,8]
    key = 1
    #print(search(arr,key))
    idx = search(arr,key)
    if idx == -1:
        print("Element not found")
    else:
        print(idx)