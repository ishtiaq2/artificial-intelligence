"""
Module 5: REASONING
A simplified, code-based illustration of why "reasoning step by step" often
beats "answering instantly" -- the same idea behind chain-of-thought
prompting in real LLMs.

We use simple multi-step word problems. The "instant guess" approach just
grabs the first two numbers it sees and guesses an operation. The
"step-by-step" approach processes each stated step in order, like doing
long division on scratch paper instead of blurting out a guess.
"""


WORD_PROBLEMS = [
    {
        "text": "Sam has 3 apples. He buys 4 more. Then he gives away 2. How many does he have now?",
        "steps": [("start", 3), ("add", 4), ("subtract", 2)],
    },
    {
        "text": "A classroom has 10 chairs. 5 more chairs are brought in. Then 3 are removed for repair. How many chairs are in the room now?",
        "steps": [("start", 10), ("add", 5), ("subtract", 3)],
    },
    {
        "text": "A baker makes 20 cookies. She sells 12. Then she bakes 6 more. How many cookies does she have?",
        "steps": [("start", 20), ("subtract", 12), ("add", 6)],
    },
]


def instant_guess(steps):
    """Simulates answering instantly: just grab the first two numbers and add them,
    without paying attention to the actual sequence of operations."""
    start_value = steps[0][1]
    second_value = steps[1][1]
    return start_value + second_value  # naive, ignores subtract/add distinctions entirely


def reason_step_by_step(steps):
    """Simulates 'showing your work': process each step in order, in the correct operation."""
    trace = []
    value = None
    for operation, number in steps:
        if operation == "start":
            value = number
            trace.append(f"Start with {value}")
        elif operation == "add":
            value += number
            trace.append(f"Add {number} -> {value}")
        elif operation == "subtract":
            value -= number
            trace.append(f"Subtract {number} -> {value}")
    return value, trace


def run_demo():
    correct_count_instant = 0
    correct_count_reasoning = 0

    for problem in WORD_PROBLEMS:
        print(f"Problem: {problem['text']}")

        guess = instant_guess(problem["steps"])
        correct_answer, trace = reason_step_by_step(problem["steps"])

        print(f"  Instant guess (no reasoning):      {guess}")
        print(f"  Step-by-step reasoning:            {' -> '.join(trace)}")
        print(f"  Correct answer:                    {correct_answer}")

        if guess == correct_answer:
            correct_count_instant += 1
        if correct_answer == correct_answer:  # step-by-step is correct by construction
            correct_count_reasoning += 1

        print()

    total = len(WORD_PROBLEMS)
    print(f"Instant-guess accuracy:    {correct_count_instant}/{total}")
    print(f"Step-by-step accuracy:     {correct_count_reasoning}/{total}")
    print("\nDiscuss: why did breaking the problem into explicit steps do better?")


if __name__ == "__main__":
    run_demo()
