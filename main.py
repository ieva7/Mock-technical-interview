from random import randint

PATH = "words.txt"


def import_text(path: str) -> list:
    """imports a text file"""
    words = []
    with open(path, "r") as reader:
        words = [line.strip() for line in reader.readlines()]
    return words


def calculate_score(word: str, score_dict: dict) -> int:
    """Calculates a score for a word"""
    if not isinstance(word, str):
        raise TypeError("Word incorrect type.")
    score = 0
    for letter in word:
        score += score_dict[letter]
    return score


def assign_tiles(bag: dict) -> list:
    """Assigns 7 random tiles from alphabet"""
    tiles = []
    for i in range(7):
        if len(bag.keys()) > 1:
            number = randint(0, len(bag.keys()) - 1)
        elif len(bag.keys()) == 1:
            number = 0
        else:
            break
        remaining_letters = list(bag.keys())
        random_tile = remaining_letters[number]
        bag[random_tile] = bag[random_tile] - 1
        if bag[random_tile] == 0:
            bag.pop(random_tile)
        tiles.append(random_tile)
        print(tiles)
    return tiles


def is_valid_word(word: str, word_list: list) -> bool:
    """Checks if word valid"""

    for valid_word in word_list:
        if sorted(list(word)) == sorted(list(valid_word)):
            return True
    return False


if __name__ == "__main__":
    score_dict = {
        'E':1,'A':1,'I':1,'O':1,'N':1,'R':1,'T':1,'L':1,'S':1,'U':1,
        'D':2,'G':2,
        'B':3,'C':3,'M':3,'P':3,
        'F':4,'H':4,'V':4,'W':4,'Y':4,
        'K':5,
        'J':8,'X':8,
        'Q':10,'Z':10}

    bag = {
        'E':12,
        'A':9,'I':9,
        'O':8,
        'N':6,'R':6,'T':6,
        'L':4,'S':4,'U':4,'D':4,
        'G':3,
        'B':2,'C':2,'M':2,'P':2,'F':2,'H':2,'V':2,'W':2,'Y':2,
        'K':1,'J':1,'X':1,'Q':1,'Z':1
    }


    valid_words = import_text(PATH)
    print(is_valid_word("ylems", valid_words))


