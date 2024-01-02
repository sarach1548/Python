import pytest
import functions


@pytest.mark.parametrize('num', [(3), (7)])
def test_find_primes(num):
    assert functions.find_primes(num) == None


@pytest.mark.parametrize('list', [([2, 6, 8, 5, 4]), ([1, 6, 8, 5, 4])])
def test_sort_list(list):
    assert functions.sort_list(list) == list.sort()


@pytest.mark.skip(reason="skiped")
def test_sort_list(list):
    assert functions.sort_list([5, 8, 9, 31, 2, 1]) == list.sort()
