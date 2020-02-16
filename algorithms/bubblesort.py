"""
  sorting list of numbers with bubble sort
"""

lst = [4,2,9,6,1,3]
swapping = True
while swapping:
    swapping = False
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            swapping = True

print(lst)
