
def max_sub_array(l):
    i_start = 0
    i_end = 0
    i_min_end = -1
    sum_so_far = 0
    sum_max = 0
    sum_min = 0
    for i, v in enumerate(l):
        sum_so_far += v
        if sum_so_far - sum_min > sum_max:
            sum_max = sum_so_far - sum_min
            i_end = i
            i_start = i_min_end + 1
        elif sum_so_far <= sum_min:
            sum_min = sum_so_far
            i_min_end = i
    return i_start, i_end, l[i_start: i_end+1], sum_max

print max_sub_array([1, 2, 3])
# (0, 2, [1, 2, 3], 6)
print max_sub_array([-1, 2, -3, 1, -1, 6])
# (5, 5, [6], 6)
print max_sub_array([1, -2, 3, 4, -5, 6])
# (2, 5, [3, 4, -5, 6], 8)
