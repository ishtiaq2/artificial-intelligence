"""
01 – A Single Neuron (pure Python, no libraries)

This shows the basic math of ONE artificial neuron:
  inputs × weights → add them up → activation → output

Ages 10+ | Educational only
"""

def neuron(inputs, weights, bias=0.0):
    """
    A single neuron:
    1. Multiply each input by its weight
    2. Add everything together (+ bias)
    3. Apply a simple activation (here: ReLU-like, just max(0, value))
    """
    total = bias
    for x, w in zip(inputs, weights):
        total += x * w          # weighted sum
    # Simple activation: if the total is negative, output 0
    output = max(0.0, total)
    return total, output


# ---------- Demo ----------
# Imagine we want the neuron to fire when the sum is large enough
inputs  = [0.5, 1.0, 0.2]     # three input numbers
weights = [0.8, -0.4, 1.2]    # one weight per input
bias    = 0.1

raw, activated = neuron(inputs, weights, bias)

print("Inputs :", inputs)
print("Weights:", weights)
print("Bias   :", bias)
print()
print("Raw sum (before activation):", round(raw, 3))
print("Activated output           :", round(activated, 3))
print()
print("Try changing the weights and see how the output changes!")
