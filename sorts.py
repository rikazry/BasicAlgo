import random as rd

def merge_sort(x):
    '''
    x: unsorted list
    '''
    if len(x) == 1:
        return x

    left = x[:len(x)/2]
    right = x[len(x)/2:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # merge!
    Y = []
    left_k = 0
    right_k = 0
    for k in range(len(x)):
        if left_sorted[left_k] < right_sorted[right_k]:
            Y.append(left_sorted[left_k])
            left_k += 1
        else:
            Y.append(right_sorted[right_k])
            right_k += 1

        # if either of the list reached the end, simply append the other
        if left_k == len(left_sorted):
            Y.extend(right_sorted[right_k:])
            return Y
        if right_k == len(right_sorted):
            Y.extend(left_sorted[left_k:])
            return Y
    return Y

