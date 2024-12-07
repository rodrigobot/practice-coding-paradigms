import time

# Returns the n-th fibonacci number
# but for large number this will be very slow.
# We need optimization
def fib(number):
    if number <= 2:
        return 1
    return fib(number-1) + fib(number-2)

# The time complexity is time = O(2^number) since we will traverse the
# tree as follow if number is 4 or 5:
#          4                                    5
#      3        2                         4             3
#    2    2   1   1                   3       2      2      2
#  1  1  1  1                      2    2   1   1   1  1  1   1
#                                1  1  1  1
# As seen above we will have to calculate at least 2*number
# giving us O(2^number)
# space = O(number)
if __name__ == '__main__':
    start = time.time()
    print fib(5)
    end = time.time()
    print (end - start)
    start = time.time()
    print fib(10)
    end = time.time()
    print (end - start)
    start = time.time()
    print fib(30)
    end = time.time()
    print (end - start)
    start = time.time()
    print fib(100)
    end = time.time()
    print (end - start)

