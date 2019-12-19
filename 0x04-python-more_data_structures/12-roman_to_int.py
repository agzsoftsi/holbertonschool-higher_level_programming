#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    val, total = 0, 0
    nums = []
    legend = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
              'D': 500, 'M': 1000}
    for n, num in enumerate(roman_string):
        nums.append(legend.get(num))
        total += nums[n]
        if n > 0 and nums[n] > nums[n - 1]:
                total -= (nums[n - 1] * 2)
    return total
