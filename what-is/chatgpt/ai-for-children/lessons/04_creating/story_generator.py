import random

heroes = ["a curious robot", "a young scientist", "a friendly AI"]
places = ["on Mars", "inside a computer", "in a floating city"]
actions = ["solved a difficult problem", "found a hidden pattern", "built a helpful machine"]

hero = random.choice(heroes)
place = random.choice(places)
action = random.choice(actions)

story = f"One day, {hero} travelled {place} and {action}."

print(story)
print()
print("Run the program again to generate a different combination.")
