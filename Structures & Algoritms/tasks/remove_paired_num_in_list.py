numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def remove_paired_numbers(lst):
    new_lst = []
    for i in lst:
        if i % 2 != 0:
            new_lst.append(i)
    return new_lst


print(remove_paired_numbers(numbers))