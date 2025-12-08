# # You may recall that an array arr is a mountain array if and only if:

# # arr.length >= 3
# # There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# # arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# # arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# # Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

 

# # Example 1:

# # Input: arr = [2,1,4,7,3,2,5]
# # Output: 5
# # Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
# # Example 2:

# # Input: arr = [2,2,2]
# # Output: 0
# # Explanation: There is no mountain.
 

# # Constraints:

# # 1 <= arr.length <= 104
# # 0 <= arr[i] <= 104
 

# # Follow up:

# # Can you solve it using only one pass?
# # Can you solve it in O(1) space?

def mountain(arr):
    ans = 0
    i = 1
    while i<len(arr)-1:
        isPeak = arr[i]>arr[i-1] and arr[i]>arr[i+1]
        if isPeak:
            cnt = 1
            j = i
            #go backward
            while j>0 and arr[j-1]<arr[j]:
                cnt += 1
                j -= 1
            #go forward
            j = i
            while j<len(arr)-1 and arr[j]>arr[j+1]:
                cnt += 1
                j += 1
            #breadth of mountain
            ans = max(cnt,ans)
            i = j
        else:
            i += 1
    return ans
        

if __name__ == "__main__":
    arr = [1,2,3,5,4,0,10,6,5,-2,-3,2,3]
    print(mountain(arr))