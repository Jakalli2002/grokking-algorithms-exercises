# big O notation (introduction): Logarithms

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

## Exercises

1.1) u have a list with 128 names, whats the maximum steps if you search it with binary search?
log 128 = 7
it would take a maximum of 7 steps to find a name

1.2) double the size of the lsit, how many steps now?
log 256 = 8
it would take 8 steps at max

## Running Time

linear time: O(n)

- simple search is in linear time, it means that the maximum number of guesses is the same as the size of the list
- max guesses = list length

logarithmic time (log time): O(log n)

- example is binary search which runs in logarithmic time, as seen by the examples above, it is better than simple search

## big O notation: what is it

- bg O notation is a special notation that tells you how fast an algorithm is
- big O notation lets u compare the number of opertations not the time in seconds an algorithm runs
- big O notation: O(number of operations)
- big O notation is for worst case scenario analysis

list of most common run times: sorted from fastest to slowest

- O(log n) - log time, example: binary search
- O(n) - linear time, example: simple search
- O(n*log n) - example: a fast sorting algorithm, like quicksort
- O(n^2) - example: a slow sorting algorithm, like selection sort
- O(n!) - example: a really slow algorithm, like the traveling salesperson

## main takeaways

- algorithm speed isnt measured in seconds but in growth of the numbers of operations
- instead of seconds, we talk about how quickly the run time of an algorithm increases as the size of the input increases
- run time of algorithms is expressed in big O notation
- O(log n) is faster than O(n), and gets a lot faster as the list of items youre searching grows
