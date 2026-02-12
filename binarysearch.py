"""
binary search:
- binary search is an search algortihm
- the input is a sorted list
- if an element youre looking for is in that list, binary search returns the position where its located, otherwise it returns NULL
- with binary search u eliminate haf the elements everytime until u find the right one
- example 1: u can guess a number between 1-100 in a maximum of seven steps (100 - 50 - 25 - 13 - 7 - 4 - 2 - 1)
- example 2: u want to find the a word in the dictionary (240.000 words). In the worst case it would take -
  simple search 240.000 steps to get to the word (if it were the last one). with binary search the worst case would be 18 steps because u always cut in half

big O notation (introduction): Logarithms 
- for any list of n, binary search will take log(2) n steps to run in the worst case, where simple search will take n steps
- Logarithms (log) are the inverse of exponentials
- example 1: log(10) 100 is like asking: how many 10s do we multiply together to get 100, the answer is 2: 10x10 = 100, so log(10) 100 = 2
- example 2: 10^2 = 100 <--> log(10) 100 = 2, 10^3 = 1000 <--> log(10) 1000 = 3, 2^4 = 16 <--> log(2) 16 = 4
- log(n) r = m
- n = number to multiply by itself
- r = wanted result
- m = number of times we have to multiply n with itself to get r

- so if we have log(2) n, for binary search and we are given a sorted list with n = 100 the result would be: log(2) 100 = 7 (2^7 = 128)

- log always means log(2)

- example 3: simple search vs binary search with a sorted list of len(n = 8):
  simple search: steps = 8 (worst case 8 steps)
  binary search: log 8 = 3 (worst case 3 steps)
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
            return f"position: {mid_position}, steps: {counter}"
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

"""
Exercises:
1.1) u have a list with 128 names, whats the maximum steps if you search it with binary search?
log 128 = 7
it would take a maximum of 7 steps to find a name

1.2) double the size of the lsit, how many steps now?
log 256 = 8
it would take 8 steps at max
"""
