"""
This module provides number processing and implements interaction with the player.
"""

def happy_numbers(n: int) -> bool:
    """
    This function defines happy number
    >>> happy_numbers(7)
    True
    >>> happy_numbers(12)
    False
    """
    try:
        past = set()
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n in past:
                return False
            past.add(n)
        return True
    except TypeError:
        return None

def get_happy_numbers(n: int) -> list:
    """
    This function returns list of happy numbers
    >>> get_happy_numbers(20)
    [1, 7, 10, 13, 19]
    >>> get_happy_numbers(40)
    [1, 7, 10, 13, 19, 23, 28, 31, 32]
    >>> get_happy_numbers(0)
    []
    >>> get_happy_numbers('0')
    """
    try:
        prime_flag = [True] * (n+1)
        prime_flag[0] = False
        primes = []
        happy = []
        for prime in range(n + 1):
            if prime_flag[prime]:
                primes.append(prime)
        for i in primes:
            if happy_numbers(i)==True:
                happy.append(i)
        return happy
    except TypeError:
        return None


def get_ulam_numbers(roof: int) -> list:
    """
    Return a list of Ulam numbers up to roof (inclusive).
    If roof is not an integer, return None.

    >>> get_ulam_numbers(10)
    [1, 2, 3, 4, 6, 8]
    >>> get_ulam_numbers(1)
    [1]
    >>> get_ulam_numbers(0)
    []
    >>> get_ulam_numbers(-1)
    []
    >>> get_ulam_numbers('a')

    """
    if not isinstance(roof, int):
        return None
    else: 
        if roof <= 0:
            return []
        if roof == 1:
            return [1]
        ulam_numbers = [1, 2]
        while True:
            sum_list = []
            i = 0
            while i < len(ulam_numbers):
                num1 = ulam_numbers[i]
                j = i + 1
                while j < len(ulam_numbers):
                    num2 = ulam_numbers[j]
                    sum_list.append(num1 + num2)
                    j += 1
                i += 1
            potential_number = sum_list[-1]
            for num in sum_list[1:]:
                if ulam_numbers[-1] < num < potential_number:
                    count = 0
                    for sum_number in sum_list:
                        if sum_number == num:
                            count += 1
                    if count == 1:
                        potential_number = num
            if potential_number > roof:
                break
            ulam_numbers.append(potential_number)

        return ulam_numbers

def get_prime_numbers(diapazon:int) -> list:
    '''
    Returns list of simple numbers, which is formed by numbers from diapason
    If diapazon is smaller than one or diapazon is not int, returns None
    >>> get_prime_numbers(10)
    [2, 3, 5, 7]
    >>> get_prime_numbers(15)
    [2, 3, 5, 7, 11, 13]
    >>> get_prime_numbers(-15)

    '''
    try:
        if diapazon < 1:
            return None
        numbers = []
        simple_nums = []
        for i in range(2,diapazon+1):
            numbers.append(i)

        for k,num in enumerate(numbers):
            simple_nums.append(num)
            for num in numbers:
                if (num % simple_nums[k] == 0) and (num > numbers[k]):
                    numbers.remove(num)
    except TypeError:
        return None
    return simple_nums

