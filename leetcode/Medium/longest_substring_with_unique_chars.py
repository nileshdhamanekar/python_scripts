# https://leetcode.com/problems/longest-substring-without-repeating-characters/


def lengthOfLongestSubstring(s: str) -> int:
    if len(set(s)) == len(s):
        print("Oh! we found it pretty quickly")
        return len(s)
    longest_substring = ""
    current_sequence_len = len(s)
    while current_sequence_len > 0:
        print("******** Current sequence len:{0} *******".format(current_sequence_len))
        for i in range(0, len(s) - current_sequence_len):
            print("i is {0}".format(i))
            print(s[i:i+current_sequence_len])
            if len(s[i:i+current_sequence_len]) == len(set(s[i:i+current_sequence_len])) and \
                    len(s[i:i+current_sequence_len]) > len(longest_substring):
                longest_substring = s[i:i+current_sequence_len]
                return len(longest_substring)
        current_sequence_len -= 1
    return len(longest_substring)


#print(lengthOfLongestSubstring("abcdb"))
#print(lengthOfLongestSubstring(""))
#print(lengthOfLongestSubstring("a"))
#print(lengthOfLongestSubstring("ab"))
#print(lengthOfLongestSubstring("abb"))
#print(lengthOfLongestSubstring("babb"))
#print(lengthOfLongestSubstring("abcb"))
print(lengthOfLongestSubstring("aab"))
#print(lengthOfLongestSubstring("aabcdeg"))
#print(lengthOfLongestSubstring("zxcvbnmlkjhgffddaaqwertyui"))
#print(lengthOfLongestSubstring("zxcvbnmlkjhgfdaqwertyui"))
