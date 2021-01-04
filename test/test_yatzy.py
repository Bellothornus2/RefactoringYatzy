from src.yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/
def test_chance():
    assert 15 == Yatzy.chance([2,3,4,5,1])
    assert 16 == Yatzy.chance([3,3,4,5,1])

def test_yatzy():
    assert 50 == Yatzy.yatzy([4,4,4,4,4])
    assert 50 == Yatzy.yatzy([6,6,6,6,6])
    assert 0 == Yatzy.yatzy([6,6,6,6,3])

def test_aces():
    assert 1 == Yatzy.aces([1,2,3,4,5])
    assert 2 == Yatzy.aces([1,2,1,4,5])
    assert 0 == Yatzy.aces([6,2,2,4,5])
    assert 4 == Yatzy.aces([1,2,1,1,1])


def test_twos():
    assert 4 == Yatzy.twos([1,2,3,2,6])
    assert 10 == Yatzy.twos([2,2,2,2,2])


def test_threes():
    assert 6 == Yatzy.threes([1,2,3,2,3])
    assert 12 == Yatzy.threes([2,3,3,3,3])


def test_fours():
    assert 12 == Yatzy.fours([4,4,4,5,5])
    assert 8 == Yatzy.fours([4,4,5,5,5])
    assert 4 == Yatzy.fours([4,5,5,5,5])


def test_fives():
    assert 10 == Yatzy.fives([4,4,4,5,5])
    assert 15 == Yatzy.fives([4,4,5,5,5])
    assert 20 == Yatzy.fives([4,5,5,5,5])


def test_sixes():
    assert 0 == Yatzy.sixes([4,4,4,5,5])
    assert 6 == Yatzy.sixes([4,4,6,5,5])
    assert 18 == Yatzy.sixes([6,5,6,6,5])

def test_three_of_a_kind():
    assert 18 == Yatzy.three_of_a_kind([3,3,3,4,5])
    assert 22 == Yatzy.three_of_a_kind([5,3,5,4,5])
    assert 17 == Yatzy.three_of_a_kind([3,3,3,3,5])

def test_four_of_a_kind():
    assert 17 == Yatzy.four_of_a_kind([3,3,3,3,5])
    assert 24 == Yatzy.four_of_a_kind([5,5,5,4,5])
    assert 15 == Yatzy.four_of_a_kind([3,3,3,3,3])
    assert 0  == Yatzy.four_of_a_kind([3,3,3,2,1])

def test_small_straight():
    assert 30 == Yatzy.small_straight([1,2,3,4,5])
    assert 30 == Yatzy.small_straight([2,3,4,5,1])
    assert 0 == Yatzy.small_straight([1,2,2,4,5])

#the name is not in snake case and should be.
#small straight has a fixed number of points if your roll has like a "ladder" of numbers such (1,2,3,4,5) or (2,3,4,5,6) this includes all the five dies
#and the points you get, arent 20, but instead, 40
def test_largeStraight():
    assert 20 == Yatzy.largeStraight(6,2,3,4,5)
    assert 20 == Yatzy.largeStraight(2,3,4,5,6)
    assert 0 == Yatzy.largeStraight(1,2,2,4,5)

#the name is not in snake case and should be.
#small straight has a fixed number of points if your roll has like a trio and a pair, for example (3,3,3,2,2) or (1,1,1,5,5) and such. This includes all the five dies
#and the points you get, arent 18 or whatever, but instead, 25
def test_fullHouse():
    assert 18 == Yatzy.fullHouse(6,2,2,2,6)
    assert 0 == Yatzy.fullHouse(2,3,4,5,6)