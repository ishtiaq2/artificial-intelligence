"""
03 – Side-by-side: Traditional rules vs Learning from data

Same goal: decide if a fruit is likely a banana.
"""

print("=" * 50)
print("TRADITIONAL PROGRAMMING (human writes the rules)")
print("=" * 50)

def traditional_is_banana(color, shape, size):
    # The programmer had to think of every rule
    if color == "yellow" and shape == "curved" and size in ["medium", "large"]:
        return True
    if color == "yellow" and shape == "curved":
        return True
    return False

print("Rule written by human:")
print('  if color == "yellow" and shape == "curved" ... → banana')
print()
print("Test:")
print("  yellow + curved + medium →", traditional_is_banana("yellow", "curved", "medium"))
print("  green  + curved + medium →", traditional_is_banana("green", "curved", "medium"))
print("  yellow + straight + small →", traditional_is_banana("yellow", "straight", "small"))


print("\n" + "=" * 50)
print("AI / LEARNING STYLE (computer finds the pattern)")
print("=" * 50)

# We give many examples instead of writing rules
# Features: [is_yellow, is_curved, size_score]  →  is_banana
training_examples = [
    ([1, 1, 0.7], 1),  # yellow, curved, medium → banana
    ([1, 1, 0.8], 1),
    ([1, 1, 0.6], 1),
    ([0, 1, 0.7], 0),  # green, curved → not banana
    ([1, 0, 0.5], 0),  # yellow, straight → not banana
    ([0, 0, 0.4], 0),
    ([1, 1, 0.9], 1),
    ([0, 1, 0.3], 0),
]

# Very simple "learning": find average feature values for bananas vs non-bananas
def learn_banana_pattern(examples):
    banana_features = []
    other_features = []
    for features, label in examples:
        if label == 1:
            banana_features.append(features)
        else:
            other_features.append(features)

    # Average of each feature for bananas
    avg_banana = [sum(f[i] for f in banana_features) / len(banana_features) for i in range(3)]
    return avg_banana

pattern = learn_banana_pattern(training_examples)
print("Computer looked at the examples and found a typical banana pattern:")
print(f"  is_yellow ≈ {pattern[0]:.2f},  is_curved ≈ {pattern[1]:.2f},  size ≈ {pattern[2]:.2f}")
print()

def ai_predict_banana(features, learned_pattern):
    # Distance to the learned "banana average"
    distance = sum((features[i] - learned_pattern[i]) ** 2 for i in range(3))
    return distance < 0.3   # close enough → call it banana

print("Predictions using the learned pattern (no if-else rules for the decision):")
tests = [
    ([1, 1, 0.75], "yellow curved medium"),
    ([0, 1, 0.7],  "green curved medium"),
    ([1, 0, 0.5],  "yellow straight small"),
    ([1, 1, 0.85], "yellow curved large"),
]
for feats, name in tests:
    result = ai_predict_banana(feats, pattern)
    print(f"  {name:25} → {'banana' if result else 'not banana'}")

print("\nKey point: the decision boundary was not written by a human.")
print("It came from the data.")
