#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    given a number and a list of numbers, write a function, that finds 2 weights in the weight list that sum to the limit
    Go down the list 'weights' and check to see if  the limit - 1 number exists in the list of weights, 
    wthen find the smallest weight that when added to the first equals the sum.  Continue until all options are exhausted. Even limits can have equal weights that sum.
    """
    # If there are fewer than two weights, no solution is possible as you have to have two packages. Test 4 does permit packages of weight zero.
    if length < 2:
        return None

    # Add weights to hashtable. Key is the weight, index is the value. 
    # If there are multiple packages of the same weight, store the values as a list.
    # TODO actually sort the list don't hardcode the logic. It does work for now though so MVP :-)
    for index, weight in enumerate(weights):
        if hash_table_retrieve(ht, weight) is None:
            hash_table_insert(ht, weight, index)
        else:
            hash_table_insert(ht, weight, [index, hash_table_retrieve(ht, weight)])

    # A package can be up to the weight of the limit which would make the 2nd package of weight zero
    max_weight = limit

    # Store if the limit is even or odd
    even = limit % 2 == 0

    # Determine the minimum weight for the range to scan
    if limit % 2 == 0:
        min_weight = limit//2 - 1
    else:
        min_weight = limit//2

    # Sort the range from max to min, move down in increments of -1
    for weight in range(max_weight, min_weight, -1):
        # Check if the current weight and it's corresponding tables are in hashtable
        if weight != min_weight+1:
            first_weight = hash_table_retrieve(ht, weight)
            second_weight = hash_table_retrieve(ht, limit-weight)

            if first_weight is not None and second_weight is not None:
                return (max(first_weight, second_weight), min(first_weight, second_weight) )
        # Special case where the limit is even and I am checking to see if there are 
        # two equal weight packages that add up to the limit
        elif even == True and min_weight+1 == weight:
            # If the case is true, this will return a list
            first_weight = hash_table_retrieve(ht, weight)
            # If the list is returned, return that
            if isinstance(first_weight, list):
                return (first_weight[0], first_weight[1])
    else:
        # None of the cases above are True so the answer must be None
        return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
