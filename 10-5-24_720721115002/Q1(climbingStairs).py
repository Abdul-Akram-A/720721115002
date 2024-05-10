def climbingStairs(n:int):
    if n<=1:
        return 1
    else:
        return climbingStairs(n-1)+climbingStairs(n-2)
    
print("Test_Case1:",climbingStairs(n=2))
print("Test_Case2:",climbingStairs(n=3))