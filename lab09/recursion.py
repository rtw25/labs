def product_of_digits(x):
    """Returns the product of the digits of an integer x."""
    x = abs(x)  # ignore the minus sign for negative numbers
    if x < 10:  # base case: single digit number
        return x
    else:
        # multiply last digit by product of remaining digits
        return (x % 10) * product_of_digits(x // 10)


def array_to_string(a, index=0):
    """Returns a comma-separated string of all elements in list a starting from index."""
    if index >= len(a):  # base case: no more elements left
        return ""
    elif index == len(a) - 1:  # last element, no comma needed
        return str(a[index])
    else:
        # add current element and recurse with next index
        return str(a[index]) + "," + array_to_string(a, index + 1)


def log(base, value):
    """Returns the floored logarithm of 'value' with respect to 'base' using recursion."""
    if value <= 0 or base <= 1:
        raise ValueError("Value must be greater than 0 and base must be greater than 1.")
    if value < base:  # base case: value is less than base
        return 0
    else:
        # perform division and count the number of divisions
        return 1 + log(base, value // base)


# example tests for each function
if __name__ == "__main__":
    # test product_of_digits
    print("Product of digits of 234:", product_of_digits(234))  # output: 24
    print("Product of digits of -12:", product_of_digits(-12))  # output: 2

    # test array_to_string
    print("Array to string [1, 2, 3, 4]:", array_to_string([1, 2, 3, 4]))  # output: "1,2,3,4"

    # test log
    print("Log base 10 of 123456:", log(10, 123456))  # output: 5
    print("Log base 2 of 64:", log(2, 64))            # output: 6
