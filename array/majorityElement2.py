# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow up: Could you solve the problem in linear time and in O(1) space?

def solution(arr):
    n = len(arr)
    lst = []
    for i in range(n):
        if arr[i] not in lst:
            cnt = 0
            for j in range(n):
                if arr[j] == arr[i]:
                    cnt += 1
            if cnt > n//3:
                lst.append(arr[i])
        if(len(lst) == 2): break
    return lst

#Time complexity: O(n) * O(log n)
#space complexity: O(2)
def optimalMethod(arr):
    ls = []
    hashmap = {}
    n = len(arr)
    mini = n//3+1
    for i in range(n):
        hashmap[arr[i]] = hashmap.get(arr[i],0)+1
        if hashmap[arr[i]] == mini:
            ls.append(arr[i])
        if len(ls) == 2:
            break
    ls.sort()
    return ls

def optimalSolution(arr):
    cnt1 = 0
    cnt2 = 0
    el1 = None
    el2 = None
    ls = []
    n = len(arr)
    for i in range(len(arr)):
        if(cnt1 == 0 and arr[i] != el2):
            cnt1 = 1
            el1 = arr[i]
        elif(cnt2 == 0 and arr[i] != el1):
            cnt2 = 1
            el2 = arr[i]
        elif(el1 == arr[i]): cnt1 += 1
        elif(el2 == arr[i]): cnt2 += 1
        else: 
            cnt1 -= 1
            cnt2 -= 1
    cnt1 = 0
    cnt2 = 0
    for i in range(len(arr)):
        if(el1 == arr[i]): cnt1 += 1
        if(el2 == arr[i]): cnt2 += 1
    mini = n//3 + 1
    if (cnt1 >= mini): ls.append(el1)
    if (cnt2 >= mini): ls.append(el2)
    sorted(ls)
    return ls
    

if __name__ == "__main__":
    arr = [3,2,1,2,1]
    print(solution(arr))
    print(optimalMethod(arr))
    print(optimalSolution(arr))