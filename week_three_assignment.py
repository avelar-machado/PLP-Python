def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False

# Tests:
print(large_power(10, 3))   # False (1000)
print(large_power(10, 4))   # True (10000)


def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False

# Tests:
print(divisible_by_ten(20))   # True
print(divisible_by_ten(23))   # False
