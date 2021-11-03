from typing import MutableMapping


def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    i = 0
    ind_1 = []
    ind_2 = []
    paired_nums = nums.copy()
    for num in nums:
        paired_nums.pop(0)
        i += 1
        for el in paired_nums:
            sum = num + el
            if sum == goal:
                ind_1.append(nums.index(num)) 
                ind_2.append(paired_nums.index(el) + i)
                
    if ind_2:
        ind_of_min_ind_2 = ind_2.index(min(ind_2))
        val_2 = nums[min(ind_2)]
        ind_of_val_1 = ind_1[ind_of_min_ind_2]
        val_1 = nums[ind_of_val_1]
        return (val_1, val_2)
    else:
        return ()
        

    
    
