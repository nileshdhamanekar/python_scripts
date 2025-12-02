def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    print('*'*50)
    roman_str = ""
    int_to_roman = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I",
                    4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
    divide_by = [1000, 500, 100, 50, 10, 5, 1]
    for i in range(0, len(divide_by)):
        print("Num:{0}, diving by: {1}".format(num, divide_by[i]))
        if num == 0:
            break
        elif num in int_to_roman.keys():
            roman_str = roman_str + int_to_roman[i]
            break
        elif num <= 3:
            for j in range(0, num):
                roman_str = roman_str + "I"
            break
        elif num < divide_by[i]:
            print("Moving on to next biggest")
            i += 1
        else:
            roman_str = roman_str + int_to_roman[divide_by[i]]
            num = num % divide_by[i]
            print(roman_str)
            print("New num:{0}".format(num))
            i += 1
    return roman_str


def int_to_roman_working(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num//val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


print(int_to_roman_working(8))
print(int_to_roman_working(3))
print(int_to_roman_working(4))
print(int_to_roman_working(9))
print(int_to_roman_working(58))
print(int_to_roman_working(1994))