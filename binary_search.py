"""
binary search:
- binary search is an search algortihm
- the input is a sorted list
- if an element youre looking for is in that list, binary search returns the position where its located, otherwise it returns NULL
- with binary search u eliminate half the elements everytime until u find the right one
- example 1: u can guess a number between 1-100 in a maximum of seven steps (100 - 50 - 25 - 13 - 7 - 4 - 2 - 1)
- example 2: u want to find the a word in the dictionary (240.000 words). In the worst case it would take -
  simple search 240.000 steps to get to the word (if it were the last one). with binary search the worst case would be 18 steps
- binary search is log(n)
"""

# implementet binary search algorithm
# function takes a sorted array and item, and returns the position of the item in the array or None if the item is not in the array
def binary_search(arr, item):
    counter = 0

    # defining start and end of search area
    start_position = 0 # first list index 0
    end_position = len(arr) - 1 # last list index

    while start_position <= end_position: # while there is more than 1 element in the list
        counter += 1

        mid_position = (start_position + end_position) // 2
        guess = arr[mid_position] # get element from the mid position of the list

        if guess == item:
            return f"position: {mid_position}, steps: {counter}" # returns position of the item and how many steps it took to find it
        elif guess < item:
            start_position = mid_position + 1 # update the start_position to the guess(mid_position) and add 1 to cut out the guess (delete first half of the list)
        else:
            end_position = mid_position - 1
        
    return None # returns None if item is not in the list
    

# testing
my_list = [1,3,5,7,9]
print(binary_search(my_list, 3)) # returns 1 (position/index of item(3) in the array)
print(binary_search(my_list, -1)) # returns None (the item was not found)

# testing with bigger list
big_list = []
for i in range(0, 10001):
    big_list.append(i)

print(binary_search(big_list, 6437))

