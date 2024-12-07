import time

# Returns the n-th fibonacci number using memoization.
# This will reduce time complexity compared to the fib.py
# implementation.
def fib(number, memo={}):
    if number in memo:
        return memo[number]
    if number <= 2:
        memo[number] = 1
        return 1

    memo[number] = fib(number-1, memo) + fib(number-2, memo)
    return memo[number]

# The time complexity is time = O(number) since we will traverse the
# tree as follow if number is 4 or 5:
#        4                              5
#      3   2                          4   3
#     2     1                       3       2
#    1                             2          1
#                                 1
# As seen above we will have to calculate at least 2*number
# giving us O(2*number) or O(number)

# space = O(number)
if __name__ == '__main__':
    memo = {}
    start = time.time()
    print fib(5, memo)
    end = time.time()
    print (end - start)
    start = time.time()
    print fib(10,memo)
    end = time.time()
    print (end - start)
    start = time.time()
    print fib(30, memo)
    end = time.time()
    print (end - start)
    start = time.time()
    print fib(100, memo)
    end = time.time()
    print (end - start)
    start = time.time()
    print fib(400, memo)
    end = time.time()
    print (end - start)