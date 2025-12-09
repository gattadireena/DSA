def rainWater(height):
    n = len(height)
    if n<=2:
        return 0
    left = [0 for x in height]
    right = [0 for x in height]
    
    left[0] = height[0]
    right[n-1] = height[n-1]
    for i in range(1,n):
        left[i] = max(left[i-1],height[i])
        right[n-i-1] = max(right[n-i],height[n-i-1])
    water = 0
    for i in range(n):
        water += min(left[i],right[i]) - height[i]
    return water
    

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(rainWater(height))