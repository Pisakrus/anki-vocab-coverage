import json

def hello():
    print("hello")

def get_json_levels(dataset : str, *levels : int):

    level_words = {level: set() for level in levels}

    with open(dataset, "r") as f:
        raw_words = json.load(f)
        
    levels_set = set(levels) # for faster filtering
    for raw_word in raw_words:
        raw_level = raw_word["level"]

        if raw_level in levels_set:
            level_words[raw_level].add(raw_word["hanzi"]) #? "hanzi" should be replaced to make it compatible with other languages

    return level_words