"""
Module 1: RULES
A rule-based chatbot -- every response comes from a rule a human wrote by hand.
No learning, no data, no patterns. Just if/elif/else.

Try it, then try to "break" it by asking something it has no rule for.
"""


def simple_chatbot(user_message):
    message = user_message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you today?"
    elif "name" in message:
        return "I'm Rule-Bot! I only know exactly what I was told to say."
    elif "weather" in message:
        return "I can't check real weather -- I only know the rules I was given!"
    elif "bye" in message:
        return "Goodbye! Thanks for chatting."
    else:
        # This is the key limitation of rule-based systems: anything outside
        # the rules the programmer thought of simply fails.
        return "Sorry, I don't understand that yet. I only know a few phrases!"


# --- TODO for students: add your own rules below the existing elif chain! ---
# Example starter idea:
#   elif "joke" in message:
#       return "Why did the robot go on a diet? Too many byte-sized snacks!"


def run_demo():
    test_messages = [
        "Hi there!",
        "What's your name?",
        "What's the weather like?",
        "Can you tell me a joke?",   # <-- this will fail until a student adds a rule for it
        "Bye!",
    ]
    for msg in test_messages:
        print(f"You: {msg}")
        print(f"Rule-Bot: {simple_chatbot(msg)}\n")


if __name__ == "__main__":
    run_demo()
