# https://leetcode.com/problems/reverse-integer/
# Note: Read the problem statement carefully, its interesting


def reverse_integer(number):
    """
    Reverse Integer.
    e.g. 123 --> 321, -159 --> -951
    """
    if not isinstance(number, int):
        return None
    number_to_string = str(number)
    reversed_str = ""
    for i in range(len(number_to_string) - 1, 0, -1):
        reversed_str += number_to_string[i]
    if number_to_string[0] == "-":
        reversed_str = "-" + reversed_str
    else:
        reversed_str += number_to_string[0]
    reversed_int = int(reversed_str)
    if reversed_int < -2 ** 31 or reversed_int > 2 ** 31 - 1:
        return 0
    else:
        return int(reversed_str)


print(reverse_integer(-123))
print(reverse_integer(""))
print(reverse_integer(-413516764543564273656273837))
print(reverse_integer(-1))
print(reverse_integer(2))
print(reverse_integer(-10))
print(reverse_integer(10))
print(reverse_integer(1534236469))