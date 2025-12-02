def find_occurances_in_file(file, key):
    count = 0
    with open(file, "r") as fp:
        for line in fp:
            print(line)
            if line.find(key):
                count += 1
    return count


print(find_occurances_in_file("find_occurances_of_word_from_file.txt", "these"))

