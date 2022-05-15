from findy import fun

def test_4_nums():
    x = fun([2,7,11,15],9)
    assert x == [0,1]

def test_4m_nums():
    x = fun([2,5,5,11],10)
    assert x == [1,2]

def test_3_nums():
    x = fun([3,2,4],6)
    assert x == [1,2]
    
def test_323_nums():
    x = fun([3,2,3],6)
    assert x == [0,2]

def test_2_nums():
    x = fun([3,3],6)
    assert x == [0,1]

def test_target_0():
    x=fun([0,4,3,0],0)
    assert x == [0,3]

def test_4more():
    x=fun([1,3,4,2],6)
    assert x == [2,3]
