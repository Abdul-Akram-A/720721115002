from typing import List
def LongestCommonPrefix(strs:List[str]):
    min_length=min(len(i) for i in strs)
    common_prefix=""
    for i in range(min_length):
        char=strs[0][i]
        for s in strs[1:]:
            if s[i]!=char:
                return common_prefix
        common_prefix += char
    return common_prefix

print("Test_Case1:",LongestCommonPrefix(["flower","flow","flight"]))
print("Test_Case2:",LongestCommonPrefix(["dog","racecar","car"]))