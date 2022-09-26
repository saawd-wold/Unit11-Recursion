from src.mystery import qs

def test_qs():
    assert qs([9, 3, 20, 19, 1, 5, 21]) == [1, 3, 5, 9, 19, 20, 21]

def test_qs_recursion():
    try:
        l = qs(list(range(2000)))
        assert False, "Expected recursion error for adversarial input!"
    except RecursionError as r:
        assert True
