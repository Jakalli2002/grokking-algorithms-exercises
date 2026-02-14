"""
selection sort:
- runs in O(n^2) - u have to perfom a O(n) operation for every item in the list (n times) --> O(n*n) = O(n^2)
- how it works: go trough the given list, look for the biggest element, then add that element to a new list, and -
  delete it from the old one so its size decreases for the next iteration
"""

# selection sort: input is an unsorted list, returns sorted list
# my code:

# get the biggest element in the list
def find_biggest(arr):
    biggest = 0
    for i in arr:
        if i > biggest:
            biggest = i
        else:
            continue

    return biggest

# selection sort: find biggest element, add it to new list and delete it from the old one
def selection_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        biggest = find_biggest(arr)
        sorted_arr.append(biggest)
        arr.remove(biggest)

    return sorted_arr

print(selection_sort([5,7,3,9,2]))


# code from book

def findSmallest(arr): 
    smallest = arr[0]       
    smallest_index = 0      
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    copiedArr = list(arr)
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr

print(selectionSort([5,7,3,9,2]))

"""
big o calc results (https://www.bigocalc.com/):

my code:
- Time complexity: O(n^2)
- Space complexity: O(n)

book code:
- Time complexity: O(n^2)
- Space complexity: O(n)

"""