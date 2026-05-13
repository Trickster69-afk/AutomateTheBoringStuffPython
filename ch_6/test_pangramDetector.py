import pytest
from pangramDetector import pangram

def test_pangram():
    true_pangram = [
    "The quick brown fox jumps over the lazy dog.",
    "Pack my box with five dozen liquor jugs.",
    "Sphinx of black quartz, judge my vow.",
    "How vexingly quick daft zebras jump!",
    "Jackdaws love my big sphinx of quartz.",
    "The five boxing wizards jump quickly.",
    "Quick zephyrs blow, vexing daft Jim.",
    "Waltz, bad nymph, for quick jigs vex!",
    "Bright vixens jump; dozy fowl quack.",
    "Crazy Fredrick bought many very exquisite opal jewels."
    ]

    not_pangram = [
    "The cat slept on the sofa.",
    "I like eating mangoes in summer.",
    "Birds flew across the lake.",
    "We watched a movie last night.",
    "Python is fun to learn.",
    "The baby laughed loudly.",
    "She opened the wooden door slowly.",
    "My phone battery is almost dead.",
    "Rain fell throughout the evening.",
    "Students completed their homework early."
    ]

    #sentences that are pangrams
    for sentence in true_pangram:
        assert pangram(sentence) == True
    
    #sentences that are not pangrams
    for sentence in not_pangram:
        assert pangram(sentence) == False