"""
Module 4: CREATING
A tiny text generator built with a Markov chain -- the simplest possible
version of "predict the next word." Real LLMs use giant neural networks
(Module 3, scaled up enormously) instead of this simple word-map, but the
core idea -- predict a plausible next token from patterns in training text --
is the same.

No API key, no internet connection needed.
"""

import random


def build_next_word_map(training_text):
    """Learn which words tend to follow which words in the training text."""
    words = training_text.split()
    next_word_map = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        following_word = words[i + 1]
        next_word_map.setdefault(current_word, []).append(following_word)
    return next_word_map


def generate(next_word_map, start_word, length=10, seed=None):
    """Generate new text by repeatedly picking a plausible 'next word'."""
    rng = random.Random(seed)
    current = start_word
    result = [current]
    for _ in range(length):
        choices = next_word_map.get(current)
        if not choices:
            break
        current = rng.choice(choices)
        result.append(current)
    return " ".join(result)


DEFAULT_TRAINING_TEXT = """the cat sat on the mat the cat likes the mat
the dog sat on the rug the dog likes the rug
the cat and the dog sat on the mat together"""


def run_demo():
    next_word_map = build_next_word_map(DEFAULT_TRAINING_TEXT)

    print("Generated text (run this a few times -- the output changes, like")
    print("a real LLM's variability):\n")
    for i in range(3):
        print(f"  Attempt {i + 1}: {generate(next_word_map, 'the', length=12)}")

    print("\nTry replacing DEFAULT_TRAINING_TEXT with your own paragraph, a")
    print("nursery rhyme, or a short story, and see what it generates!")


if __name__ == "__main__":
    run_demo()
