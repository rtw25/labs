# Write your code here :-)
# Task 2: Fibonacci with Memoization

# Memoization decorator
def memoize(f):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return wrapper

# Recursive Fibonacci with memoization
@memoize
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)

# Standard recursive Fibonacci (without memoization)
def standard_fibo(n):
    if n <= 1:
        return n
    else:
        return standard_fibo(n - 1) + standard_fibo(n - 2)

# Main Program for Task 2
if __name__ == "__main__":
    # Speed test for Fibonacci computation
    import time

    # Compare speed of both implementations for n = 35
    start_time = time.time()
    print(f"Fibonacci (standard) of 35: {standard_fibo(35)}")
    print(f"Time taken for standard Fibonacci: {time.time() - start_time:.6f} seconds")

    start_time = time.time()
    print(f"Fibonacci (memoized) of 35: {recur_fibo(35)}")
    print(f"Time taken for memoized Fibonacci: {time.time() - start_time:.6f} seconds")
