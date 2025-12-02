# https://leetcode.com/problems/roman-to-integer/


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    if s is None:
        return 0
    previous = None
    sum_roman = 0
    roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    special_case = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}
    for char in s:
        if previous and previous in special_case.keys() and char in special_case[previous]:
            sum_roman = sum_roman + roman_to_int[char] - roman_to_int[previous]
            sum_roman -= roman_to_int[previous]
        elif char in roman_to_int:
            sum_roman += roman_to_int[char]
        previous = char
    return sum_roman


def romanToInt_onedict(s):
    """
    :type s: str
    :rtype: int
    """
    if s is None:
        return 0
    sum_roman = 0
    roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
                    "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    for i in range(0, len(s)):
        if i > 0 and s[i-1:i+1] in roman_to_int.keys():
            sum_roman += roman_to_int[s[i-1:i+1]]
            sum_roman -= roman_to_int[s[i-1]]
        else:
            sum_roman += roman_to_int[s[i]]
    return sum_roman

print(romanToInt_onedict("III"))
print(romanToInt_onedict("IV"))
print(romanToInt_onedict("IX"))
print(romanToInt_onedict("LVIII"))
print(romanToInt_onedict("MCMXCIV"))
print(romanToInt_onedict(""))