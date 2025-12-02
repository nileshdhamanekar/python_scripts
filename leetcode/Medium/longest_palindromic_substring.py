# https://leetcode.com/problems/longest-palindromic-substring/
def brute_force(s):
    # https://medium.com/@celinesurai/cracking-the-coding-interview-longest-palindromic-substring-python-solution-9c5606e1b750
    longest = ""
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if s[i:j] == s[i:j][::-1]:
                if len(longest) < len(s[i:j]):
                    longest = s[i:j]
    return longest

def helper(s, l, r):
    while l>=0 and r<len(s) and s[l]==s[r]:
        l -= 1
        r += 1
    return s[l+1:r]

def optimized(s):
    # Time complexity = O(n*2)
    # https://medium.com/@celinesurai/cracking-the-coding-interview-longest-palindromic-substring-python-solution-9c5606e1b750
    longest = ""
    for i in range(len(s)):
        tmp = helper(s, i, i)
        if len(tmp) > len(longest):
            longest = tmp
        tmp = helper(s, i, i+1)
        if len(tmp) > len(longest):
            longest = tmp
    return longest

def optimized_linear_manacher(s):
    # https://www.youtube.com/watch?v=V-sEwsca1ak
    # Couldn't find a good python implementation of Manacher's algorithm in pthon

print(optimized("cbabcdb"))
print(optimized("c"))
print(optimized("cb"))
print(optimized(""))
print(optimized("babcbaabcbaccba"))
print(optimized("abbababba"))
print(optimized("cbabcdb"))
print(optimized("cdbabcbabdab"))
