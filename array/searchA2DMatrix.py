# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

#Approach 1: Brute Force search (linear search)
#Approach 2: Binary search O(NlogM)
#Approach 3: Staircase search O(N+M)

def staircaseSearch(matrix,target,n,m):
    i = 0 
    j = m-1
    while(i<n and j>=0):
        if(matrix[i][j] == target):
            return (i,j)
        elif matrix[i][j] > target:
            j -= 1
        else:
            i += 1
    return -1
    
if __name__ == "__main__":
    matrix = [[10,20,30,40],
              [15,25,35,45],
              [27,29,37,48],
              [32,33,39,50]]
    target = 33
    n = 4 #row
    m = 4 #column
    print(staircaseSearch(matrix,target,n,m))