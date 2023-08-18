from main import calculate_score, assign_tiles, import_text, is_valid_word
import pytest

@pytest.fixture
def scorer():
    return {
        'E':1,'A':1,'I':1,'O':1,'N':1,'R':1,'T':1,'L':1,'S':1,'U':1,
        'D':2,'G':2,
        'B':3,'C':3,'M':3,'P':3,
        'F':4,'H':4,'V':4,'W':4,'Y':4,
        'K':5,
        'J':8,'X':8,
        'Q':10,'Z':10}

@pytest.fixture
def bag():
    return {
        'E':12,
        'A':9,'I':9,
        'O':8,
        'N':6,'R':6,'T':6,
        'L':4,'S':4,'U':4,'D':4,
        'G':3,
        'B':2,'C':2,'M':2,'P':2,'F':2,'H':2,'V':2,'W':2,'Y':2,
        'K':1,'J':1,'X':1,'Q':1,'Z':1
    }


def test_calculate_score(scorer):
    assert calculate_score("DOG", scorer) == 5


def test_assign_tiles(bag):
    assert len(assign_tiles(bag)) == 7
    assert assign_tiles(bag)[0] in "QWERTYUIOPLKJHGFDSAZXCVBNM"


def test_bag_updates():
    bag = {"D": 2, "O": 5, "G": 1}
    tiles = assign_tiles(bag)
    assert len(bag.keys()) == 1


def test_if_word_valid():
    valid_words = import_text("words.txt")
    assert is_valid_word("ogd", valid_words)

