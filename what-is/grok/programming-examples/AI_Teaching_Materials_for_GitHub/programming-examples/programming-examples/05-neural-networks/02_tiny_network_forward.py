"""
02 – Tiny Neural Network – Forward Pass only

A network with:
  2 inputs → 3 hidden neurons → 1 output neuron

We only do the FORWARD pass (data goes left → right).
No learning yet.

Uses only pure Python lists.
"""

def relu(x):
    return max(0.0, x)

def forward(inputs, w_hidden, b_hidden, w_output, b_output):
    """
    inputs      : list of 2 numbers
    w_hidden    : 3x2 list  (weights into the 3 hidden neurons)
    b_hidden    : list of 3 biases for hidden layer
    w_output    : list of 3 weights into the output neuron
    b_output    : single bias for output
    """
    # ----- Hidden layer -----
    hidden = []
    for i in range(3):                       # 3 hidden neurons
        total = b_hidden[i]
        for j in range(2):                   # 2 inputs
            total += inputs[j] * w_hidden[i][j]
        hidden.append(relu(total))
    
    # ----- Output layer -----
    total = b_output
    for i in range(3):
        total += hidden[i] * w_output[i]
    output = relu(total)
    
    return hidden, output


# ---------- Demo ----------
# Fixed weights just so we can see numbers flow through the network
w_hidden = [
    [0.5, -0.2],   # weights for hidden neuron 0
    [0.3,  0.8],   # weights for hidden neuron 1
    [-0.4, 0.6],   # weights for hidden neuron 2
]
b_hidden = [0.1, -0.1, 0.2]
w_output = [0.7, -0.5, 0.3]
b_output = 0.0

# Two example inputs
examples = [
    [0.9, 0.1],
    [0.2, 0.8],
]

print("Tiny network: 2 inputs → 3 hidden → 1 output\n")
for inputs in examples:
    hidden, output = forward(inputs, w_hidden, b_hidden, w_output, b_output)
    print(f"Input  : {inputs}")
    print(f"Hidden : {[round(h, 3) for h in hidden]}")
    print(f"Output : {round(output, 3)}")
    print("-" * 30)
