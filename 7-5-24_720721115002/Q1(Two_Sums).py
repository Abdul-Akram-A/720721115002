from typing import List
def TwoSum(nums: List[int],target:int):
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j] == target:
                return [i,j]
    return []

Test_Case = {
    "Case_1": {"array": [2, 7, 11, 15], "target": 9},
    "Case_2": {"array": [3, 2, 4], "target": 6},
    "Case_3": {"array": [3, 3], "target": 6}
}

for Case, Parameter in Test_Case.items():
    print(TwoSum(Parameter["array"], Parameter["target"]))