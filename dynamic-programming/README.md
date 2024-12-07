# Dynamic Programming
________________
## Memoization
____
### What is memoization? 

It is the optimization of algorithms by storing results of expensive functions and reusing them when the same input occurs. This is a caching technique used in dynamic programming.
Think recursion and how expensive it is for large numbers. For optimization, we use memoization.

### How is it implemented?
Usually we use a sort of map that allows for (key, value) storage.
_________
## Tips!
1. Make it Work!!!
    + visualize the problem as a tree
    + implement the tree using recursion
    + test it
2. Make it efficient
    + Add memo object
    + Add base case to return memo objects
    + Store returned value into memo object