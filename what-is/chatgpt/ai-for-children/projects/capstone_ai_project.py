# AI for Children - Capstone Project

print("=== My Helpful AI ===")

goal = input("What do you need help with? (study/game): ").lower()

# RULES
if goal == "study":
    hours = float(input("How many hours did you study? "))

    # LEARNING-LIKE SCORE
    score = hours * 15

    # REASONING
    if score >= 75:
        decision = "You appear ready for a quiz."
    else:
        decision = "More practice may help."

    # ACTION
    print("AI decision:", decision)

elif goal == "game":
    player_health = int(input("Player health (0-100): "))

    # RULES + REASONING
    if player_health < 30:
        action = "Find a health potion."
    elif player_health < 70:
        action = "Be careful and continue."
    else:
        action = "You are strong. Explore!"

    print("AI action:", action)

else:
    print("This version of the AI does not know that goal yet.")

print()
print("Congratulations! You combined several ideas from the course.")
