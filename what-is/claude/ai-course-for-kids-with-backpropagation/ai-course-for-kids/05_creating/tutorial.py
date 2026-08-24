"""
Module 5: CREATING
A tiny text generator built with a Markov chain -- the simplest possible
version of "predict the next word." Real LLMs use giant neural networks
(Module 3, scaled up enormously) instead of this simple word-map, but the
core idea -- predict a plausible next token from patterns in training text --
is the same.

No API key, no internet connection needed.
"""

import random
from collections import Counter


def build_next_word_model(training_text):
    """Learn, for each word, a PROBABILITY DISTRIBUTION over what tends to
    follow it -- counted directly from the training text. This is a real
    (tiny) statistical model: the numbers below were never typed by a human,
    they were counted from data."""
    words = training_text.split()
    next_word_counts = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        following_word = words[i + 1]
        next_word_counts.setdefault(current_word, Counter())[following_word] += 1
    return next_word_counts


def show_learned_probabilities(next_word_counts, word):
    """Print the probability distribution the model learned for a given word --
    proof that these numbers came from counting the data, not from a rule."""
    counts = next_word_counts.get(word)
    if not counts:
        print(f"  (no data learned for '{word}')")
        return
    total = sum(counts.values())
    print(f"  After '{word}', the model learned these probabilities:")
    for next_word, count in counts.most_common():
        probability = count / total
        print(f"    '{next_word}': {probability:.0%} (seen {count} times)")


def generate(next_word_counts, start_word, length=10, seed=None):
    """Generate new text by sampling from the LEARNED probability distribution
    at each step -- words seen more often after the current word are more
    likely to be picked, just like a real LLM weighting likely next tokens."""
    rng = random.Random(seed)
    current = start_word
    result = [current]
    for _ in range(length):
        counts = next_word_counts.get(current)
        if not counts:
            break
        candidates = list(counts.keys())
        weights = list(counts.values())
        current = rng.choices(candidates, weights=weights, k=1)[0]
        result.append(current)
    return " ".join(result)


DEFAULT_TRAINING_TEXT = """the cat sat on the mat the cat likes the mat
the dog sat on the rug the dog likes the rug
the cat and the dog sat on the mat together"""


def run_demo():
    next_word_counts = build_next_word_model(DEFAULT_TRAINING_TEXT)

    print("What the model actually LEARNED (counted from the training text,")
    print("nobody typed these numbers):\n")
    show_learned_probabilities(next_word_counts, "the")

    print("\nGenerated text (run this a few times -- the output changes, like")
    print("a real LLM's variability, because it's SAMPLING from probabilities,")
    print("not just picking uniformly at random):\n")
    for i in range(3):
        print(f"  Attempt {i + 1}: {generate(next_word_counts, 'the', length=12)}")

    print("\nTry replacing DEFAULT_TRAINING_TEXT with your own paragraph, a")
    print("nursery rhyme, or a short story, and see what it generates!")


if __name__ == "__main__":
    run_demo()
