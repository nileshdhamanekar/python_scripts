# https://leetcode.com/problems/longest-common-prefix/

# 10 ways to solve: https://medium.com/@d_dchris/10-methods-to-solve-the-longest-common-prefix-problem-using-python-leetcode-14-a87bb3eb0f3a

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    common_prefix = ""
    if strs is None or len(strs) < 1:
        return common_prefix
    if len(strs) == 1:
        return strs[0]
    for i in range(0, len(strs[0])):
        for each_str in strs:
            if strs[0][0:i+1] != each_str[0:i+1]:
                return common_prefix
            print("iteration {0} --> strs[0][0:i+1]: {1}, each_str[0:i+1]:{2}".format(i, strs[0][0:i+1], each_str[0:i+1]))
        common_prefix = strs[0][0:i+1]
    return common_prefix


print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix([]))
print(longestCommonPrefix(["Hello"]))
print(longestCommonPrefix(["Hello", "Hi"]))
print(longestCommonPrefix(["c","c"]))