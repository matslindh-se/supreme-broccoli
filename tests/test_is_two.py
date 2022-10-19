from broccoli.main import is_two

def test_is_two_is_two():
    assert is_two(2)
    assert not is_two(3)
