# The below function doesn't work correctly. It should sum all the numbers at the
# current time. For example, 01:02:03 should return 6. Improve and fix the function,
# and write unit test(s) for it. Use any testing framework you're familiar with.


# [TODO]: fix the function
def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""

    if not isinstance(time_str, str):
        raise TypeError("Error: please input a string representing time in HH:MM:SS format.")

    list_of_nums = time_str.split(":")

    if len(list_of_nums) != 3:
        raise ValueError("Error: Input string not in the right format.")

    for i, num in enumerate(list_of_nums):
        list_of_nums[i] = int(num)
    return sum(list_of_nums)
