from sub_and_div import subtract as sub, divide as div

def test_subtract():
    assert sub(3, 2) == 1
    assert sub(3, 3) == 0
    assert sub(3, 4) == -1

def test_divide():
    assert div(3, 2) == 1.5
    assert div(3, 3) == 1
    assert div(3, 0) == None
