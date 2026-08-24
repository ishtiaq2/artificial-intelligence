"""
Module 6: REASONING
Three demos, in order:

  A. HAND-CODED RULES (this is NOT really AI)
     A human types out every word that means "add" or "subtract". Any word
     nobody thought of breaks it.

  B. A TINY TRAINED MODEL (this IS real AI -- but watch it fail!)
     We train a real learning algorithm (logistic regression) on just 10
     labelled examples. It genuinely learns from data instead of following
     typed rules -- but with so little data, it does NOT generalize well.
     This is an honest, common AI failure mode, not a mistake in this code.

  C. THE SAME MODEL WITH MORE DATA (still real AI -- now it works better)
     Same exact training process, just fed 24 examples instead of 10. Watch
     accuracy improve on the exact same test sentences. This is the single
     most important fact about modern AI: more (good) data usually means
     better generalization, which is why real LLMs train on billions of
     examples, not dozens.

Requires: scikit-learn (see requirements.txt)
"""

import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


# ---------------------------------------------------------------------------
# A. Hand-coded rules -- a human wrote every one of these words
# ---------------------------------------------------------------------------

def rule_based_operation(sentence):
    text = sentence.lower()
    add_words = ["buys", "gets", "receives", "gains", "finds"]
    subtract_words = ["gives away", "sells", "loses", "spends", "drops"]
    for word in add_words:
        if word in text:
            return "add"
    for word in subtract_words:
        if word in text:
            return "subtract"
    return None  # nobody thought of this word -- it's simply invisible to the rules


# ---------------------------------------------------------------------------
# B. A model trained on only 10 examples -- real learning, but too little data
# ---------------------------------------------------------------------------

SMALL_TRAINING_SENTENCES = [
    "He buys 4 apples", "She gets 5 more coins", "They gain 2 points",
    "He finds 3 dollars on the ground", "She receives 6 gifts",
    "He gives away 2 apples", "She sells 6 cookies", "They lose 3 marbles",
    "He spends 4 dollars", "She drops 2 pencils",
]
SMALL_TRAINING_LABELS = ["add", "add", "add", "add", "add",
                          "subtract", "subtract", "subtract", "subtract", "subtract"]


# ---------------------------------------------------------------------------
# C. The same idea, trained on 24 examples instead
# ---------------------------------------------------------------------------

BIGGER_TRAINING_SENTENCES = SMALL_TRAINING_SENTENCES + [
    "He collects 4 shells", "She wins 3 marbles", "He earns 5 dollars",
    "They gathered 2 more stickers", "She picked up 3 rocks",
    "He was given 4 candies", "They added 5 books",
    "He donates 2 books", "They throw away 3 papers", "She loses 1 toy",
    "He gave 4 coins to his friend", "They used up 3 crayons",
    "She misplaced 2 keys", "He returned 5 toys",
]
BIGGER_TRAINING_LABELS = SMALL_TRAINING_LABELS + [
    "add", "add", "add", "add", "add", "add", "add",
    "subtract", "subtract", "subtract", "subtract", "subtract", "subtract", "subtract",
]


def train_operation_classifier(sentences, labels):
    """The actual training step: an optimization algorithm looks at the
    labelled examples and adjusts internal weights until it separates
    'add' sentences from 'subtract' sentences. Nobody tells it that 'buys'
    means add -- it has to discover that association from the data itself."""
    model = Pipeline([
        ("vectorizer", CountVectorizer()),
        ("classifier", LogisticRegression(max_iter=1000)),
    ])
    model.fit(sentences, labels)
    return model


def extract_number(sentence):
    match = re.search(r"\d+", sentence)
    return int(match.group()) if match else None


def evaluate(model, test_sentences, correct_labels):
    correct_count = 0
    for sentence, correct in zip(test_sentences, correct_labels):
        predicted = model.predict([sentence])[0]
        is_correct = predicted == correct
        correct_count += is_correct
        mark = "correct" if is_correct else "WRONG"
        print(f"  '{sentence}' -> predicted: {predicted}  (expected: {correct})  [{mark}]")
    print(f"  Score: {correct_count}/{len(test_sentences)}\n")


def run_demo():
    print("=== A. Hand-coded rules ===")
    for sentence in ["He buys 4 apples", "He earns 5 dollars"]:
        result = rule_based_operation(sentence)
        note = "  (nobody coded the word 'earns' -- it breaks!)" if result is None else ""
        print(f"  '{sentence}' -> {result}{note}")

    # Test sentences use words NONE of the training sets have seen before.
    test_sentences = ["She wins 3 marbles", "He hands over 3 pencils",
                       "They discard 2 cups", "He picks up 3 rocks"]
    test_labels = ["add", "subtract", "subtract", "add"]

    print("\n=== B. A trained model, but only 10 training examples ===")
    small_model = train_operation_classifier(SMALL_TRAINING_SENTENCES, SMALL_TRAINING_LABELS)
    evaluate(small_model, test_sentences, test_labels)

    print("=== C. The same training process, now with 24 examples ===")
    bigger_model = train_operation_classifier(BIGGER_TRAINING_SENTENCES, BIGGER_TRAINING_LABELS)
    evaluate(bigger_model, test_sentences, test_labels)

    print("Discuss: Version A breaks on any word nobody typed in by hand.")
    print("Version B and C are BOTH real AI (same training code!) -- the only")
    print("difference is how much data they saw. More data -> better")
    print("generalization to words the model has never seen. This is exactly")
    print("why real LLMs train on billions of examples instead of dozens.")


if __name__ == "__main__":
    run_demo()
