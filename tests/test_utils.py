from lam.utils import flatten


def test_flatten():
    for i in range(10):
        test = [j for j in range(i)]
        assert flatten(test) == test

    assert flatten([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
    assert flatten([[1, [2, 3], [[4]]], 5]) == [1, 2, 3, 4, 5]
