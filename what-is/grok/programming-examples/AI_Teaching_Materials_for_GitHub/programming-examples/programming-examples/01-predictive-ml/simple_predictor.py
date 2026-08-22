# Simple "predictor" – not real machine learning, just rules
# Run in any Python environment (Thonny, VS Code, or online)
# Ages 10+

def predict_sweetness(color, size):
    """Very simple rules a human might write"""
    if color == "yellow" and size == "medium":
        return "Probably a banana – sweet!"
    elif color == "red" and size == "small":
        return "Probably a strawberry – sweet!"
    elif color == "green" and size == "large":
        return "Probably a watermelon – sweet inside!"
    else:
        return "I am not sure. I need more examples!"

# Test it
print(predict_sweetness("yellow", "medium"))
print(predict_sweetness("red", "small"))
print(predict_sweetness("purple", "tiny"))
