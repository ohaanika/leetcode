"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/
"""

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:


# METHOD 1:
def longestCommonPrefix(strs: list[str]) -> str:
    common_prefix = ""
    sorted_strs = sorted(strs)
    first_str = sorted_strs[0]
    last_str = sorted_strs[-1]
    for idx in range(len(first_str)):
        if first_str[idx] == last_str[idx]:
            common_prefix += first_str[idx]
        else:
            return common_prefix
    return common_prefix


# METHOD 2: Incorrect for strs = ["a"]
def longestCommonPrefix2(strs: list[str]) -> str:
    sorted_strs = sorted(strs)
    first_str = sorted_strs[0]
    last_str = sorted_strs[-1]
    for idx in range(len(first_str)):
        if first_str[idx] != last_str[idx]:
            return first_str[: idx + 1]
    return ""


print(longestCommonPrefix(["flower", "flow", "flight"]))  # OUTPUT: "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))  # OUTPUT: ""
print(longestCommonPrefix(["a"]))  # OUTPUT: "a"
print(longestCommonPrefix([""]))  # OUTPUT: ""
