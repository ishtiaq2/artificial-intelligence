"""
Module 7: THE FUTURE
A small "Narrow AI Sorter" -- prints a list of real AI systems and asks
students (via input()) to classify each as Narrow AI or "would need AGI."
Every correct answer today is Narrow AI -- that's the point of the exercise.

Run interactively, or read AI_SYSTEMS and discuss as a class without running
the input() loop.
"""

AI_SYSTEMS = [
    "A chess-playing AI that can beat grandmasters",
    "A self-driving car",
    "A spam email filter",
    "A voice assistant that sets timers and plays music",
    "A translation app",
    "A movie recommendation algorithm",
    "A medical AI that detects tumors in X-rays",
    "A chatbot that helps you write an essay",
    "A robot vacuum cleaner",
    "An AI that could learn to cook, paint, do your taxes, AND babysit -- all with zero retraining",
]

ANSWER_KEY = {
    "A chess-playing AI that can beat grandmasters": "Narrow AI",
    "A self-driving car": "Narrow AI",
    "A spam email filter": "Narrow AI",
    "A voice assistant that sets timers and plays music": "Narrow AI",
    "A translation app": "Narrow AI",
    "A movie recommendation algorithm": "Narrow AI",
    "A medical AI that detects tumors in X-rays": "Narrow AI",
    "A chatbot that helps you write an essay": "Narrow AI",
    "A robot vacuum cleaner": "Narrow AI",
    "An AI that could learn to cook, paint, do your taxes, AND babysit -- all with zero retraining": "AGI",
}


def run_quiz(interactive=True):
    print("Sort each AI system as 'Narrow AI' or 'AGI'.\n")
    score = 0
    for system in AI_SYSTEMS:
        correct = ANSWER_KEY[system]
        if interactive:
            answer = input(f"{system}\n  Your answer (Narrow AI / AGI): ").strip().lower()
            if answer in correct.lower():
                print("  Correct!\n")
                score += 1
            else:
                print(f"  The answer was: {correct}\n")
        else:
            print(f"{system}\n  -> {correct}\n")

    if interactive:
        print(f"Score: {score}/{len(AI_SYSTEMS)}")
    print("\nNotice: every real system today is Narrow AI. AGI remains hypothetical --")
    print("that's exactly the discussion to have for the class debate activity!")


if __name__ == "__main__":
    # Set interactive=False if running non-interactively (e.g. in an automated test)
    run_quiz(interactive=False)
