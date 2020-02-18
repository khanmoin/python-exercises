"""
  Calculating sum of n numbers using dynamic programming
"""


# used for backing up the previously calculated sums
cached_results = {}


def sum_to_n(num):
    result = 0
    for i in reversed(range(num)):
        # check if the result is already computed
        if i+1 in cached_results:
            result += cached_results[i+1]
            break
        else:
            result += i+1
    # add the results to our backing store
    cached_results[num] = result
    return result


if __name__ == '__main__':
    print("Import in python shell to get the benefits")
