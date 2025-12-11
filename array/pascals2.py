# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]
 

# Constraints:

# 0 <= rowIndex <= 33
 

# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?


def pascal2(rowIndex):
    row = [1]
    ans = 1
    for i in range(1,rowIndex+1):
        ans = ans * (rowIndex-i+1)
        ans = ans//i
        row.append(ans)
    return row

if __name__ == "__main__":
    rowIndex = 4
    print(pascal2(rowIndex))