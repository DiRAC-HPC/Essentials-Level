from power2 import power2

def test_0():
    assert power2(0) == []

def test_1():
    assert power2(1) == [1]

def test_2():
    assert power2(2) == [2]

def test_3():
    assert power2(3) == [2, 1]

def test_4():
    assert power2(4) == [4]

def test_27():
    assert power2(27) == [16, 8, 2, 1]

def test_255():
    assert power2(255) == [128, 64, 32, 16, 8, 4, 2, 1]

def test_256():
    assert power2(256) == [256]

def test_257():
    assert power2(257) == [256, 1]
