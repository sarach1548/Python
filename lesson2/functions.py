import math


def find_primes(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
        return True


def sort_list(list):
    list(list).sort()
    return list


def calculate_expression(s):
    return ""
