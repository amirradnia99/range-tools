def expand_ranges(my_list):
    """
    Expands a list of range strings into a list of individual numbers.

    Args:
        my_list (list): A list of strings representing ranges (e.g., ['1000-1003', '1008-1010']).

    Returns:
        list: A list of individual numbers.
    """
    res = []
    for range_str in my_list:
        start, end = map(int, range_str.split('-'))
        res.extend(range(start, end + 1))
    return res


def collapse_ranges(my_list):
    """
    Collapses a list of individual numbers into a list of range strings.

    Args:
        my_list (list): A list of integers (e.g., [1000, 1001, 1002, 1009]).

    Returns:
        list: A list of formatted range strings (e.g., ['1000-1003', '1008-1010']).
    """
    if not my_list:
        return []
    
    my_list.sort()
    formated_nums = []
    nums = []
    
    for num in my_list:
        if not nums:
            nums.append(num)
        else:
            if num == nums[-1] + 1:
                nums.append(num)
            else:
                formated_nums.append(f"{nums[0]}-{nums[-1]}")
                nums = [num]
    
    if nums:
        formated_nums.append(f"{nums[0]}-{nums[-1]}")
    
    return formated_nums


# Example usage
if __name__ == "__main__":
    # Example for expand_ranges
    range_list = ['1000-1003', '1008-1010', '1018-1018', '1039-1040']
    expanded = expand_ranges(range_list)
    print("Expanded Ranges:", expanded)

    # Example for collapse_ranges
    number_list = [1000, 1001, 1002, 1009, 1003, 1010, 1008, 1040, 1039, 1018]
    collapsed = collapse_ranges(number_list)
    print("Collapsed Ranges:", collapsed)