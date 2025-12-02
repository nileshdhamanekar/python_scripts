# https://leetcode.com/problems/implement-strstr/


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    length = len(needle)
    for i in range(0, len(haystack) - len(needle) + 1):
        if haystack[i:i+length] == needle:
            return i
    else:
        return -1

print(strStr("hello", "ll"))
print(strStr("aaaaa", "bb"))
print(strStr("hell", "ll"))
print(strStr("hello", "he"))
print(strStr("hello", "e"))


def strStr_pythonic(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    return haystack.find(needle)