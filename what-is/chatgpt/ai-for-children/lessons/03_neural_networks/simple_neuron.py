# A simplified artificial neuron

x = float(input("Enter the input: "))
weight = float(input("Enter the weight: "))
bias = float(input("Enter the bias: "))

output = weight * x + bias

print(f"Neuron output: {output}")

if output > 0:
    print("Activation: ON")
else:
    print("Activation: OFF")

print("Try changing the weight and bias.")
