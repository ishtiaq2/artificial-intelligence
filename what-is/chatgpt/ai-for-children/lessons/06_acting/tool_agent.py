def calculator_tool():
    number1 = float(input("First number: "))
    number2 = float(input("Second number: "))
    print("Result:", number1 + number2)


def greeting_tool():
    name = input("What is your name? ")
    print(f"Hello, {name}! The agent used the greeting tool.")


goal = input("What do you want? (calculate/greet): ").lower()

print("Goal received:", goal)

if "calculate" in goal:
    print("Agent decision: use calculator tool")
    calculator_tool()
elif "greet" in goal or "hello" in goal:
    print("Agent decision: use greeting tool")
    greeting_tool()
else:
    print("The agent does not know which tool to use yet.")
