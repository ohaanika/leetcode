"""
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/
"""

# class Solution:
#     def trap(self, height: List[int]) -> int:


from copy import deepcopy


# METHOD 1:
def trap(height: list[int]) -> int:

    num_water = 0
    max_level = max(height)

    for current_level in range(max_level + 1):

        print(f"{current_level}\t- {height}")

        # remove leading zeros and negative numbers
        leading_i = 0
        for i, h in enumerate(height):
            if i - leading_i <= 0 and h <= 0:
                leading_i += 1
        del height[:leading_i]
        print(f"\t- {height}")

        # remove trailing zeros and negative numbers
        reversed_height = list(reversed(height))
        trailing_i = 0
        for i, h in enumerate(reversed_height):
            if i - trailing_i <= 0 and h <= 0:
                trailing_i += 1
        del reversed_height[:trailing_i]
        height = list(reversed(reversed_height))
        print(f"\t- {height}")

        # count current occurences of zeros and negative numbers
        num_water += len(list(filter(lambda x: x < 1, height)))

        # prepare to check next level
        height = list(map(lambda x: x - 1, height))

    return num_water


# METHOD 2:
def trap2(height):
    def clean_elevation(l):
        copy_l = deepcopy(l)  # assuming this exists
        isLeadingNonPositive = True
        leadingNonPositiveCount = 0

        for i in range(len(copy_l)):
            isLeadingNonPositive = isLeadingNonPositive and copy_l[i] <= 0
            if isLeadingNonPositive:
                leadingNonPositiveCount += 1
            else:
                break
        del copy_l[:leadingNonPositiveCount]

        isTrailingNonPositive = True
        trailingNonPositiveCount = 0
        for i in range(len(copy_l)):
            isTrailingNonPositive = isTrailingNonPositive and l[-i - 1] <= 0
            if isTrailingNonPositive:
                trailingNonPositiveCount += 1
            else:
                break
        del copy_l[-1:-(trailingNonPositiveCount)]

        return copy_l

    m = max(height)
    w = 0
    elevation = deepcopy(height)
    for i in range(m):
        elevation = clean_elevation(elevation)
        where_water_can_fill = list(filter(lambda x: x < 1, elevation))
        w += len(where_water_can_fill)
        elevation = list(map(lambda x: x - 1, elevation))

    return w


print(trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # OUTPUT: 6
print(trap(height=[4, 2, 0, 3, 2, 5]))  # OUTPUT: 9
