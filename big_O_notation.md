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
