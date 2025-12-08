# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

def medianoftwoarray(num1,num2):
    num = num1+num2
    arr = sorted(num)
    n = len(arr)
    if n%2 == 1:
        mid0 = n//2
        return arr[mid0]
    else:
        mid1 = n//2
        mid2 = n//2 - 1
        return (arr[mid1]+arr[mid2])/2
    
if __name__ == "__main__":
    num1 = [1,3]
    num2 = [2,4]
    print(medianoftwoarray(num1,num2))
    