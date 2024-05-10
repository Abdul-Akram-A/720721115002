from typing import List
def SingleOne(array:List[int]):
    for i in array:
        if array.count(i)==1:
            return i
        
print("Test_Case1:",SingleOne([2,2,1]))
print("Test_Case2:",SingleOne([4,1,2,1,2]))
print("Test_Case3:",SingleOne([1]))
