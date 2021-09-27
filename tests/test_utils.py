from lam.utils import flatten, foldr


def test_flatten():
    for i in range(10):
        test = [j for j in range(i)]
        assert flatten(test) == test

    assert flatten([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
    assert flatten([[1, [2, 3], [[4]]], 5]) == [1, 2, 3, 4, 5]


def test_foldr():
    assert foldr(lambda x, y: x + y, 5, [1, 2, 3, 4]) == 15
    assert foldr(lambda x, y: x / y, 2, [8, 12, 24, 4]) == 8.
    assert foldr(max, 111, [3, 6, 12, 4, 55, 11]) == 111

    assert foldr(lambda x, y: x / y, 3, []) == 3
