"""
01 – Learning from examples (the AI way)

Instead of writing:
    if hours >= 6: print("tired")

We give the computer many examples of (hours_slept → tired or not)
and let it discover the relationship itself.

This is a tiny illustration of supervised learning.
"""

# ---------- 1. DATA (examples we show the computer) ----------
# Each pair is: [hours_slept, is_tired]
# 1 = tired, 0 = not tired
training_data = [
    [3, 1],   # slept 3 hours → tired
    [4, 1],
    [5, 1],
    [6, 0],   # slept 6 hours → not tired
    [7, 0],
    [8, 0],
    [9, 0],
    [2, 1],
    [10, 0],
]

# ---------- 2. The computer "learns" a simple threshold ----------
# In real AI this is done with complex math (gradients, neural nets…).
# Here we use a very simple method so you can see the idea:
# Find a threshold that best separates tired from not-tired.

def find_best_threshold(data):
    """Try different thresholds and keep the one with fewest mistakes."""
    best_threshold = 0
    best_errors = len(data) + 1

    for possible in [3.5, 4.5, 5.5, 6.5, 7.5]:
        errors = 0
        for hours, label in data:
            prediction = 1 if hours < possible else 0
            if prediction != label:
                errors += 1
        if errors < best_errors:
            best_errors = errors
            best_threshold = possible
    return best_threshold, best_errors


threshold, mistakes = find_best_threshold(training_data)

print("The computer looked at the examples and decided:")
print(f"  → If a person sleeps less than {threshold} hours, they are probably tired.")
print(f"  → This rule made only {mistakes} mistake(s) on the training data.\n")

# ---------- 3. Now use the learned rule on NEW people ----------
new_people = [4.0, 5.0, 6.0, 7.0, 8.5]

print("Predictions for new people (the computer has never seen these exact numbers):")
for hours in new_people:
    prediction = "tired" if hours < threshold else "not tired"
    print(f"  Slept {hours} hours → {prediction}")

print("\nNotice: We never wrote 'if hours < 5.5'.")
print("The computer found that threshold by looking at the examples.")
