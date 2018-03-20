from analyze import running_total

def test_example_one():
    assert running_total([1, 2, 1, 8, 9, 2]) == [3, 18, 2]
