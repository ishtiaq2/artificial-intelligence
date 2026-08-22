import random

subjects = ["The robot", "A curious cat", "My best friend", "An old computer"]
verbs = ["discovered", "invented", "dreamed about", "built"]
objects = ["a flying bicycle", "a talking sandwich", "a portal to space", "a new game"]
endings = ["and everyone was amazed!", "but then it disappeared.", "and they became best friends."]

def make_sentence():
    return f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)} {random.choice(endings)}"

print("Here are 5 generated sentences:")
for i in range(5):
    print(f"{i+1}. {make_sentence()}")
