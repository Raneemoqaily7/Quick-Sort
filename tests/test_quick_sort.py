
from quick_sort.quick import QuickSort

def test_one():
    assert [-911, 1, 2, 10, 14, 90] == QuickSort([10,90,14,-911,1,2], 0, 5)
def test_two():

    assert [-7, 1, 5, 7, 10, 70, 100] == QuickSort([1,5,100,-7,7,10,70], 0, 6)

def test_three():

    assert [10, 20, 30, 40] == QuickSort([30,20,10,40], 0, 2)