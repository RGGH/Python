#  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#  |r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import pytest
from src.ind import two_sum


testdata = [
    ([1,2,3],5,(1,2)),
    ([1,6,3],7,(0,1)),
    ([1,6,3],4,(0,2)),
    ([1,6,3,-5],7,(0,1))
]


@pytest.mark.parametrize("a,b,expected", testdata)
def test_two_sum(a, b, expected):
    assert two_sum(a,b)==expected