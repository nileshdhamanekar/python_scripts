# https://leetcode.com/problems/palindrome-number/


def is_integer_palindrome(x):
    """
    :param int x:
    """
    reversed_str = ""
    if not isinstance(x, int):
        return False
    x = str(x)
    for i in range(len(x) - 1, -1, -1):
        reversed_str += x[i]
    if reversed_str == x:
        return True
    else:
        return False


print(is_integer_palindrome((121)))
print(is_integer_palindrome((-121)))
print(is_integer_palindrome((1212)))
print(is_integer_palindrome(("121")))
print(is_integer_palindrome(("")))
print(is_integer_palindrome((1)))
print(is_integer_palindrome((12)))
print(is_integer_palindrome((121343121)))