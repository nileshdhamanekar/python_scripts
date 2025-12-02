# Leetcode: https://leetcode.com/problems/maximum-subarray/

def maximum_subarray_brute_force(my_list):
    if len(my_list) <= 1:
        return sum(my_list)
    subarray = my_list
    sum_all_subarray = sum(subarray)
    for i in range(len(my_list)-1, -1, -1):
        for j in range(0, len(my_list)-i + 1):
            if sum(my_list[j:i+j]) > sum_all_subarray:
                subarray = my_list[j:i+j]
                sum_all_subarray = sum(my_list[j:i+j])
    return subarray, sum_all_subarray
print(maximum_subarray_brute_force([-2,1,-3,4,-1,2,1,-5,4]))
print(maximum_subarray_brute_force([-1]))