# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30

def pascals3(numRows):
    triangle = []
    for r in range(numRows):
        row = [1]
        ans = 1
        for i in range(1,r+1):
            ans = ans * (r-i+1)
            ans = ans//i
            row.append(ans)
        triangle.append(row)
    return triangle 

if __name__ == "__main__":
    numRows = 4
    print(pascals3(numRows))