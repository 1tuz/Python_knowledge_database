def merge_sorted_lists(list1, list2):
    # initialize pointers for both lists
    i, j = 0, 0
    # initialize an empty list to store the merged elements
    merged_list = []
    # loop through both lists until the end of one of the lists is reached
    while i < len(list1) and j < len(list2):
        # compare the current elements of both lists
        if list1[i] < list2[j]:
            # if the current element of list1 is smaller, add it to the merged list
            merged_list.append(list1[i])
            # move to the next element in list1
            i += 1
        else:
            # if the current element of list2 is smaller or equal, add it to the merged list
            merged_list.append(list2[j])
            # move to the next element in list2
            j += 1
    # if one of the lists has been fully traversed, add the remaining elements from the other list
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    # return the merged list
    return merged_list


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
print(merge_sorted_lists(list1, list2))
