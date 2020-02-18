"""
  Computing fibonacci number using dynamic programming
"""


# storing results of already computed numbers
cached_results = {0: 0, 1: 1}


def fibonacci(num):
    # looking in the cache
    if num in cached_results:
        return cached_results[num]
    else:
        cached_results[num] = fibonacci(num-2) + fibonacci(num-1)
        return cached_results[num]


if __name__ == '__main__':
    print("Import in python shell to see the benefits")
