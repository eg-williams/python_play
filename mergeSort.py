to_sort = [8, 1, 9, 2, 7, 3, 6, 4, 5, 10, 11]

# Divide the array in to two, and sort them recursively.
# We want to do all the divisions before we do the merge.
def merge_sort(array, left_index, right_index):
    if left_index >= right_index:
        return
    mid = (left_index + right_index) // 2
    merge_sort(array, left_index, mid)
    merge_sort(array, mid + 1, right_index)
    merge(array, left_index, right_index, mid)


# Do the actual merge. We have a lhs array and a rhs array, and the middle bit.
def merge(array, left_index, right_index, mid):
    # Get a copy of both sides of the array
    l_copy = array[left_index:mid + 1]
    r_copy = array[mid + 1:right_index + 1]

    # We need to track the index as we do the merge.
    l_copy_index = 0
    r_copy_index = 0
    sorted_index = left_index

    # Traverse both copies until we run out of elements in one of the copies.
    while l_copy_index < len(l_copy) and r_copy_index < len(r_copy):
        # if the lhs copy has the smaller element, put it in the sorted array and move on
        if l_copy[l_copy_index] <= r_copy[r_copy_index]:
            array[sorted_index] = l_copy[l_copy_index]
            l_copy_index += 1
        else:
            # if the rhs has the smaller element, put it in the sorted array and move on.
            array[sorted_index] = r_copy[r_copy_index]
            r_copy_index += 1

        # Move the sorted index along, no matter which side the element came from.
        sorted_index += 1

    # We've run out of elements either on the lhs or rhs copy, so we
    # need to traverse the remaining elements and add them to the sorted array.
    while l_copy_index < len(l_copy):
        array[sorted_index] = l_copy[l_copy_index]
        l_copy_index += 1
        sorted_index += 1

    while r_copy_index < len(r_copy):
        array[sorted_index] = r_copy[r_copy_index]
        r_copy_index += 1
        sorted_index += 1


# Testing time
merge_sort(to_sort, 0, len(to_sort) - 1)

print(to_sort)
