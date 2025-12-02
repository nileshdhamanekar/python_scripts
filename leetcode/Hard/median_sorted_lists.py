# Leetcode: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Optimized solution: https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46
# Optimized_solution: https://www.youtube.com/watch?v=LPFhl65R7ww&list=PLC8kzThK0MeSR3VR9jh0Hurv30RH_Ss3o&index=22


def median_sorted_lists_brute_force(nums1, nums2):
    combined_list = list()
    while len(nums1) > 0 and len(nums2) > 0:
        if nums1[0] < nums2[0]:
            combined_list.append(nums1.pop(0))
        elif nums2[0] < nums1[0]:
            combined_list.append(nums2.pop(0))
    combined_list.extend(nums1 + nums2)
    print(combined_list)
    middle = int(len(combined_list) / 2)
    if len(combined_list) % 2 == 1:
        median = combined_list[middle]
    else:
        median = (combined_list[middle] + combined_list[middle-1]) / 2
    return median


def median_sorted_arrays_binary_search(nums1, nums2):
    # Because we are going to do binary search on nums1, we want nums1 to be smaller
    # So we swap nums1 and nums2 if nums1 is bigger
    import math
    if len(nums1) > len(nums2):
        median_sorted_arrays_binary_search(nums2, nums1)

    x = len(nums1)
    y = len(nums2)
    low = 0
    high = x
    median = None
    while low <= high:
        print(nums1)
        print(nums2)
        print("low:{0} high:{1}".format(low, high))
        partition_x = int((low + high)/2)
        partition_y = int((x + y + 1)/2) - partition_x
        print("partition_x:{0}".format(partition_x))
        print("partition_y:{0}".format(partition_y))

        if partition_x == 0:
            max_left_x = -math.inf
            print("Setting max_left_x to -INF")
        elif partition_x == x:
            min_right_x = math.inf
            print("Setting min_right_x to INF")
        else:
            max_left_x = nums1[partition_x - 1]
            min_right_x = nums1[partition_x]
            print("max_left_x:{0}, min_right_x:{1}".format(max_left_x, min_right_x))

        if partition_y == 0:
            max_left_y = -math.inf
            print("Setting max_left_y to -INF")
        elif partition_y == y:
            min_right_y = math.inf
            print("Setting min_right_y to INF")
        else:
            max_left_y = nums2[partition_y-1]
            min_right_y = nums2[partition_y]
            print("max_left_y:{0}, min_right_y:{1}".format(max_left_y, min_right_y))

        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            # We found the perfect partitions
            if (x + y) % 2 == 1:
                median = max(max_left_x, max_left_y)
                print("Odd length: median:{0}".format(median))
            else:
                median = (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                print("Even length: median:{0}".format(median))
        elif max_left_x > min_right_y:
            print("Reducing high by 1")
            high = partition_x - 1
        else:
            print("Increasing low by 1")
            low = partition_x + 1
        print("-"*50)
    return median


print("================ This solution isn't working yet ================")
print(median_sorted_arrays_binary_search([1,3,5,7,9], [2,4,6,8,10]))
print('*'*50)
print("================ This solution isn't working yet ================")
# print(median_sorted_arrays_binary_search([1,3,5,7,9], [2,4,6,8]))
# print('*'*50)
# print(median_sorted_arrays_binary_search([1,2,3,4,5], [6]))
# print('*'*50)
# print(median_sorted_arrays_binary_search([5], [6,7,8,9,10]))
# print('*'*50)
# print(median_sorted_arrays_binary_search([1,2,3,4,5], []))
# print('*'*50)
# print(median_sorted_arrays_binary_search([], [6,7,8,9,10]))
# print('*'*50)
# print(median_sorted_arrays_binary_search([1,2], [3,4]))
