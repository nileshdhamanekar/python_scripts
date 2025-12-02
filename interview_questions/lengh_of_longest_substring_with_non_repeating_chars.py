# Find length of longest substring with non-repeating characters
# Input: abcdbac
# Output: 4 # longest substring is "abcd"
# Input: bbbb
# Output: 1 # longest substring is "b"
# https://medium.com/@dimko1/longest-substring-without-repeating-characters-997ded46e89d


def longest_substring_with_non_repeating_chars(my_str):
    start = max_length = 0
    used_chars = {}
    for i in range(0, len(my_str)):
        if my_str[i] in used_chars and start <= used_chars[my_str[i]]:
            start = used_chars[my_str[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)
        used_chars[my_str[i]] = i
    return max_length

#print(longest_substring_with_non_repeating_chars("abcdbac"))
#print(longest_substring_with_non_repeating_chars("bbbb"))
print(longest_substring_with_non_repeating_chars("abcabcbb"))