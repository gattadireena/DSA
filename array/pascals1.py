##

def pascalTriangle(row,col):
    n = row - 1
    r = col - 1
    res = 1
    i = 0
    for i in range(r):
        res = res*(n-i)
        res = res//(i+1)
    return res
    

if __name__ == "__main__":
    #arr = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1]]
    row = 5
    col = 3
    print(pascalTriangle(row,col))