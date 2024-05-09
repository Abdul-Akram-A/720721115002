from typing import List
def FindIndex(nums:List[int],target:int):
    left=0
    right=len(nums)-1
    while left <= right:
        middle = (left+right)//2
        if nums[middle]==target:
            return middle
        elif nums[middle] < target:
            left= middle+1
        elif nums[middle]>target:
            right=middle-1
    return left

print("Test_Case1:",FindIndex([1,3,5,6],5))
print("Test_Case2:",FindIndex([1,3,5,6],2))
print("Test_Case3:",FindIndex([1,3,5,6],7))