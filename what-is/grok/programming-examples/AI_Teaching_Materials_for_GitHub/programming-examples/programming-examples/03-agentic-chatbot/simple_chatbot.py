print("Hello! I am a simple chatbot. Type 'bye' to quit.")

while True:
    user = input("You: ").lower().strip()
    
    if user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break
    elif "hello" in user or "hi" in user:
        print("Bot: Hi! How can I help you today?")
    elif "how are you" in user:
        print("Bot: I am just code, but I feel great helping you!")
    elif "joke" in user:
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")
    elif "name" in user:
        print("Bot: I am ChatBot Junior. What is your name?")
    else:
        print("Bot: Hmm, I do not understand that yet. Try asking for a joke!")
