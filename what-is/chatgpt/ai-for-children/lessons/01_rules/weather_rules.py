# Lesson 1: Rule-Based AI

weather = input("What is the weather? (sunny/rainy/snowy): ").lower()
temperature = float(input("What is the temperature in Celsius? "))

if weather == "snowy":
    print("AI recommendation: Wear warm clothes and be careful of ice.")
elif weather == "rainy":
    print("AI recommendation: Take an umbrella.")
elif temperature < 5:
    print("AI recommendation: Wear a warm jacket.")
elif temperature < 20:
    print("AI recommendation: A light jacket may be useful.")
else:
    print("AI recommendation: Enjoy the warm weather!")

print("This system follows rules written by a human.")
