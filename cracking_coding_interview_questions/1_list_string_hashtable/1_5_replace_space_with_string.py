def replace_space_with_string2(my_str):
    return my_str.replace(" ", "%20")


def replace_space_with_string(my_str):
    new_str = ""
    for char in my_str:
        if char == " ":
            new_str += "%20"
        else:
            new_str += char
    return new_str



print(replace_space_with_string("Hello There"))
print(replace_space_with_string("Hello There"))
