"""
I should probably loop through the whole thing
"""

# my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
# my_list = [14, 57, 15, 33, 72, 79, 26, 56, 42, 40]
# my_list = [14, 15, 57, 33, 72, 79, 26, 56, 42, 40]
# my_list = [14, 15, 26, 33, 72, 79, 57, 56, 42, 40]
# my_list = [14, 15, 26, 33, 72, 79, 57, 56, 42, 40]
# my_list = [14, 15, 26, 33, 40, 79, 57, 56, 42, 72]
# my_list = [14, 15, 26, 33, 40, 42, 57, 56, 79, 72]
# my_list = [14, 15, 26, 33, 40, 42, 56, 57, 79, 72]
# my_list = [14, 15, 26, 33, 40, 42, 56, 57, 79, 72]
# my_list = [14, 15, 26, 33, 40, 42, 56, 57, 72, 79]

# This is selection sort. Selecting the smallest number and swapping.


def selection_sort(my_list):
    for cur_pos in range(len(my_list)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(my_list)):
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp


# my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
# selection_sort(my_list)
# print(my_list)

# This is for selection:
# n = 10, 10 * 5 = 50
# n = 100, 100 * 50 = 5000


# 15, 57, 14, 33, 72, 79, 26, 56, 42, 40
# 14, 15, 57, 33, 72, 79, 26, 56, 42, 40
# 14, 15, 33, 57, 72, 79, 26, 56, 42, 40
# 14, 15, 33, 57, 72, 79, 26, 56, 42, 40
# 14, 15, 33, 57, 72, 79, 26, 56, 42, 40
# 14, 15, 26, 33, 57, 72, 79, 56, 42, 40
# 14, 15, 26, 33, 56, 57, 72, 79, 42, 40

# This is insertion sort


def insertion_sort(my_list):
    for key_pos in range(1, len(my_list)):  # 100
        key_value = my_list[key_pos]
        scan_pos = key_pos - 1
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):  # worst - 50, avg - 25
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos -= 1

        my_list[scan_pos + 1] = key_value


my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
insertion_sort(my_list)
print(my_list)

# This is for insertion sort, worst case
# n = 10, 10 * 5 = 50
# n = 100, 100 * 50 = 5000
# n * (n/2) = n^2 / 2

# This is insertion sort, average case
# n = 10, 10 * 2.5 = 25
# n = 100, 100 * 25 = 2,500
# n * (n/4) = n^2 / 4

# Insertion sort, best case
# n = 10, 10 * 1 = 10
# n = 100, 100 * 1 = 100
# n = 1000, 1000 * 1 = 1000
